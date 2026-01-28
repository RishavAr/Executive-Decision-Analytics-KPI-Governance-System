-- =============================================================================
-- EXECUTIVE DECISION ANALYTICS & KPI GOVERNANCE SYSTEM
-- SQL Layer: Semantic Models & Data Quality Checks
-- Company: TechVantage Inc.
-- =============================================================================

-- =============================================================================
-- PART 1: STAGING MODELS (dbt-style)
-- =============================================================================

-- stg_metrics.sql
-- Staging layer for metric definitions with standardization
CREATE OR REPLACE VIEW stg_metrics AS
SELECT 
    metric_id,
    metric_name,
    UPPER(category) AS category,
    business_unit,
    owner,
    data_steward,
    unit_of_measure,
    calculation_method,
    data_source,
    refresh_frequency,
    target_q4_2024 AS current_target,
    CASE 
        WHEN criticality = 'Critical' THEN 1
        WHEN criticality = 'High' THEN 2
        WHEN criticality = 'Medium' THEN 3
        ELSE 4
    END AS criticality_rank,
    criticality
FROM metric_definitions;

-- stg_kpi_actuals.sql
-- Staging layer for KPI actuals with period parsing
CREATE OR REPLACE VIEW stg_kpi_actuals AS
SELECT 
    metric_id,
    period,
    CASE 
        WHEN period LIKE 'Q1%' THEN 1
        WHEN period LIKE 'Q2%' THEN 2
        WHEN period LIKE 'Q3%' THEN 3
        WHEN period LIKE 'Q4%' THEN 4
    END AS quarter_num,
    CAST(SUBSTR(period, -4) AS INTEGER) AS fiscal_year,
    actual_value,
    target_value,
    variance_pct,
    status,
    last_updated,
    data_quality_flag
FROM kpi_actuals;

-- =============================================================================
-- PART 2: INTERMEDIATE MODELS
-- =============================================================================

-- int_metric_performance.sql
-- Calculate performance metrics with trend analysis
CREATE OR REPLACE VIEW int_metric_performance AS
SELECT 
    a.metric_id,
    m.metric_name,
    m.category,
    m.owner,
    a.period,
    a.fiscal_year,
    a.quarter_num,
    a.actual_value,
    a.target_value,
    a.actual_value - a.target_value AS variance_absolute,
    ROUND((a.actual_value - a.target_value) / NULLIF(a.target_value, 0) * 100, 2) AS variance_pct,
    CASE 
        WHEN a.actual_value >= a.target_value THEN 'Met'
        WHEN a.actual_value >= a.target_value * 0.95 THEN 'On Track'
        WHEN a.actual_value >= a.target_value * 0.85 THEN 'At Risk'
        ELSE 'Off Track'
    END AS performance_status,
    LAG(a.actual_value) OVER (
        PARTITION BY a.metric_id 
        ORDER BY a.fiscal_year, a.quarter_num
    ) AS prior_period_value,
    ROUND((a.actual_value - LAG(a.actual_value) OVER (
        PARTITION BY a.metric_id 
        ORDER BY a.fiscal_year, a.quarter_num
    )) / NULLIF(LAG(a.actual_value) OVER (
        PARTITION BY a.metric_id 
        ORDER BY a.fiscal_year, a.quarter_num
    ), 0) * 100, 2) AS qoq_change_pct,
    m.criticality_rank,
    a.data_quality_flag
FROM stg_kpi_actuals a
JOIN stg_metrics m ON a.metric_id = m.metric_id;

-- int_data_quality_summary.sql
-- Aggregate data quality issues by metric and severity
CREATE OR REPLACE VIEW int_data_quality_summary AS
SELECT 
    metric_id,
    COUNT(*) AS total_issues,
    SUM(CASE WHEN severity = 'Critical' THEN 1 ELSE 0 END) AS critical_issues,
    SUM(CASE WHEN severity = 'High' THEN 1 ELSE 0 END) AS high_issues,
    SUM(CASE WHEN severity = 'Medium' THEN 1 ELSE 0 END) AS medium_issues,
    SUM(CASE WHEN severity = 'Low' THEN 1 ELSE 0 END) AS low_issues,
    SUM(CASE WHEN status = 'Open' THEN 1 ELSE 0 END) AS open_issues,
    SUM(CASE WHEN status = 'Resolved' THEN 1 ELSE 0 END) AS resolved_issues,
    ROUND(SUM(CASE WHEN status = 'Resolved' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS resolution_rate,
    AVG(JULIANDAY(resolution_date) - JULIANDAY(detected_date)) AS avg_resolution_days
FROM data_quality_issues
GROUP BY metric_id;

-- =============================================================================
-- PART 3: MART MODELS (Final Business Views)
-- =============================================================================

-- mart_executive_kpi_dashboard.sql
-- Executive-level KPI summary for dashboards
CREATE OR REPLACE VIEW mart_executive_kpi_dashboard AS
SELECT 
    m.category,
    m.metric_id,
    m.metric_name,
    m.owner,
    p.period,
    p.actual_value,
    p.target_value,
    p.variance_pct,
    p.performance_status,
    p.qoq_change_pct,
    CASE 
        WHEN p.performance_status = 'Met' THEN '🟢'
        WHEN p.performance_status = 'On Track' THEN '🟡'
        WHEN p.performance_status = 'At Risk' THEN '🟠'
        ELSE '🔴'
    END AS status_indicator,
    COALESCE(dq.open_issues, 0) AS data_quality_alerts,
    m.criticality
FROM stg_metrics m
JOIN int_metric_performance p ON m.metric_id = p.metric_id
LEFT JOIN int_data_quality_summary dq ON m.metric_id = dq.metric_id
WHERE p.period = 'Q4 2024'
ORDER BY m.criticality_rank, m.category;

-- mart_okr_scorecard.sql
-- OKR tracking with linked metrics
CREATE OR REPLACE VIEW mart_okr_scorecard AS
SELECT 
    o.okr_id,
    o.objective,
    o.key_result,
    o.owner,
    o.start_value,
    o.target_value,
    o.current_value,
    o.progress_pct,
    o.status,
    o.confidence,
    CASE 
        WHEN o.confidence >= 0.9 THEN 'High'
        WHEN o.confidence >= 0.7 THEN 'Medium'
        ELSE 'Low'
    END AS confidence_level,
    CASE 
        WHEN o.status = 'Achieved' THEN '✅'
        WHEN o.status = 'On Track' THEN '🟢'
        WHEN o.status = 'At Risk' THEN '🟠'
        ELSE '🔴'
    END AS status_icon,
    o.linked_metric_ids
FROM okr_tracking o;

-- mart_metric_governance.sql
-- Complete metric governance view for auditing
CREATE OR REPLACE VIEW mart_metric_governance AS
SELECT 
    m.metric_id,
    m.metric_name,
    m.category,
    m.business_unit,
    m.owner,
    m.data_steward,
    m.calculation_method,
    m.data_source,
    m.refresh_frequency,
    m.criticality,
    COALESCE(drift.drift_count, 0) AS definition_changes_ytd,
    drift.last_change_date,
    COALESCE(dq.total_issues, 0) AS total_quality_issues,
    COALESCE(dq.open_issues, 0) AS open_quality_issues,
    COALESCE(dq.resolution_rate, 100) AS issue_resolution_rate,
    CASE 
        WHEN dq.open_issues > 0 AND m.criticality = 'Critical' THEN 'URGENT'
        WHEN dq.open_issues > 0 THEN 'ATTENTION'
        WHEN drift.drift_count > 2 THEN 'REVIEW'
        ELSE 'HEALTHY'
    END AS governance_status
FROM stg_metrics m
LEFT JOIN (
    SELECT 
        metric_id,
        COUNT(*) AS drift_count,
        MAX(change_date) AS last_change_date
    FROM metric_drift_log
    GROUP BY metric_id
) drift ON m.metric_id = drift.metric_id
LEFT JOIN int_data_quality_summary dq ON m.metric_id = dq.metric_id;

-- =============================================================================
-- PART 4: DATA QUALITY TESTS (dbt-style)
-- =============================================================================

-- test_unique_metric_id.sql
-- Test: All metric_ids should be unique
SELECT 
    metric_id,
    COUNT(*) AS occurrences
FROM metric_definitions
GROUP BY metric_id
HAVING COUNT(*) > 1;

-- test_not_null_critical_fields.sql
-- Test: Critical fields should not be null
SELECT 
    metric_id,
    'metric_name' AS field_name
FROM metric_definitions WHERE metric_name IS NULL
UNION ALL
SELECT 
    metric_id,
    'owner' AS field_name
FROM metric_definitions WHERE owner IS NULL
UNION ALL
SELECT 
    metric_id,
    'calculation_method' AS field_name
FROM metric_definitions WHERE calculation_method IS NULL;

-- test_valid_status.sql
-- Test: All KPI statuses should be valid values
SELECT 
    metric_id,
    period,
    status
FROM kpi_actuals
WHERE status NOT IN ('On Track', 'At Risk', 'Off Track', 'Met', 'Achieved');

-- test_variance_calculation.sql
-- Test: Variance should be correctly calculated
SELECT 
    metric_id,
    period,
    actual_value,
    target_value,
    variance_pct,
    ROUND((actual_value - target_value) / target_value * 100, 2) AS expected_variance
FROM kpi_actuals
WHERE variance_pct IS NOT NULL
  AND ABS(variance_pct - ROUND((actual_value - target_value) / target_value * 100, 2)) > 0.5;

-- test_okr_progress_bounds.sql
-- Test: OKR progress should be between 0 and 100
SELECT 
    okr_id,
    key_result,
    progress_pct
FROM okr_tracking
WHERE progress_pct < 0 OR progress_pct > 100;

-- =============================================================================
-- PART 5: ANALYTICAL QUERIES
-- =============================================================================

-- Query: Category Performance Summary
SELECT 
    category,
    COUNT(*) AS metric_count,
    ROUND(AVG(CASE WHEN performance_status IN ('Met', 'On Track') THEN 1 ELSE 0 END) * 100, 1) AS pct_on_track,
    ROUND(AVG(variance_pct), 2) AS avg_variance_pct,
    ROUND(AVG(qoq_change_pct), 2) AS avg_qoq_improvement
FROM int_metric_performance
WHERE period = 'Q4 2024'
GROUP BY category
ORDER BY pct_on_track DESC;

-- Query: Data Quality Risk Assessment
SELECT 
    m.metric_id,
    m.metric_name,
    m.criticality,
    COALESCE(dq.open_issues, 0) AS open_issues,
    CASE 
        WHEN m.criticality = 'Critical' AND dq.open_issues > 0 THEN 'HIGH RISK'
        WHEN m.criticality = 'High' AND dq.open_issues > 0 THEN 'MEDIUM RISK'
        WHEN dq.open_issues > 0 THEN 'LOW RISK'
        ELSE 'NO RISK'
    END AS risk_level
FROM stg_metrics m
LEFT JOIN int_data_quality_summary dq ON m.metric_id = dq.metric_id
WHERE dq.open_issues > 0 OR m.criticality = 'Critical'
ORDER BY 
    CASE 
        WHEN m.criticality = 'Critical' AND dq.open_issues > 0 THEN 1
        WHEN m.criticality = 'High' AND dq.open_issues > 0 THEN 2
        ELSE 3
    END;

-- Query: Decision Impact Analysis
SELECT 
    d.decision_id,
    d.decision_title,
    d.decision_date,
    d.expected_impact,
    d.actual_impact,
    d.status,
    COUNT(DISTINCT SUBSTR(d.kpis_considered, 1, 
        INSTR(d.kpis_considered || ',', ',') - 1)) AS primary_kpis_tracked
FROM decision_log d
GROUP BY d.decision_id, d.decision_title, d.decision_date, 
         d.expected_impact, d.actual_impact, d.status
ORDER BY d.decision_date DESC;
