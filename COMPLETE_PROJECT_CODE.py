# ============================================================================
# EXECUTIVE DECISION ANALYTICS & KPI GOVERNANCE SYSTEM
# COMPLETE PROJECT CODE
# ============================================================================

# ============================================================================
# FILE 1: data/company_kpis.py - DATA GENERATION SCRIPT
# ============================================================================

"""
Executive Decision Analytics & KPI Governance System
Generates realistic company-wide KPI data for a fictitious tech company: TechVantage Inc.
Based on real S&P 500 sector performance data from 2024
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

# Company: TechVantage Inc. - A mid-cap technology company
# Fiscal Year: 2024 (Q1-Q4) with historical comparison to 2023

# =============================================================================
# 1. METRIC DEFINITIONS & OWNERSHIP REGISTRY
# =============================================================================

metric_definitions = pd.DataFrame({
    'metric_id': ['REV001', 'REV002', 'REV003', 'PROF001', 'PROF002', 'PROF003', 
                  'CUST001', 'CUST002', 'CUST003', 'CUST004', 'OPS001', 'OPS002',
                  'OPS003', 'EMP001', 'EMP002', 'EMP003', 'PROD001', 'PROD002',
                  'FIN001', 'FIN002', 'MKT001', 'MKT002', 'DATA001', 'DATA002'],
    'metric_name': [
        'Total Revenue', 'Recurring Revenue (ARR)', 'Revenue Growth Rate YoY',
        'Gross Profit Margin', 'Operating Margin', 'EBITDA Margin',
        'Customer Acquisition Cost (CAC)', 'Customer Lifetime Value (LTV)', 
        'Net Promoter Score (NPS)', 'Customer Churn Rate',
        'System Uptime', 'Average Response Time', 'Incident Resolution Time',
        'Employee Satisfaction Score', 'Employee Turnover Rate', 'Training Completion Rate',
        'Sprint Velocity', 'Release Frequency',
        'Days Sales Outstanding (DSO)', 'Working Capital Ratio',
        'Marketing Qualified Leads (MQLs)', 'Conversion Rate',
        'Data Quality Score', 'Report Accuracy Rate'
    ],
    'category': [
        'Revenue', 'Revenue', 'Revenue',
        'Profitability', 'Profitability', 'Profitability',
        'Customer', 'Customer', 'Customer', 'Customer',
        'Operations', 'Operations', 'Operations',
        'People', 'People', 'People',
        'Product', 'Product',
        'Finance', 'Finance',
        'Marketing', 'Marketing',
        'Data Governance', 'Data Governance'
    ],
    'business_unit': [
        'Finance', 'Finance', 'Finance',
        'Finance', 'Finance', 'Finance',
        'Sales', 'Sales', 'Customer Success', 'Customer Success',
        'Engineering', 'Engineering', 'Engineering',
        'HR', 'HR', 'HR',
        'Product', 'Product',
        'Finance', 'Finance',
        'Marketing', 'Marketing',
        'Data', 'Data'
    ],
    'owner': [
        'CFO - Sarah Chen', 'CFO - Sarah Chen', 'CFO - Sarah Chen',
        'CFO - Sarah Chen', 'CFO - Sarah Chen', 'CFO - Sarah Chen',
        'CRO - Michael Torres', 'CRO - Michael Torres', 'VP CS - Lisa Park', 'VP CS - Lisa Park',
        'CTO - David Kumar', 'CTO - David Kumar', 'CTO - David Kumar',
        'CHRO - Amanda Foster', 'CHRO - Amanda Foster', 'CHRO - Amanda Foster',
        'CPO - James Wilson', 'CPO - James Wilson',
        'Controller - Robert Kim', 'Controller - Robert Kim',
        'CMO - Jennifer Lee', 'CMO - Jennifer Lee',
        'CDO - Maria Santos', 'CDO - Maria Santos'
    ],
    'data_steward': [
        'Finance Analytics', 'Finance Analytics', 'Finance Analytics',
        'Finance Analytics', 'Finance Analytics', 'Finance Analytics',
        'Sales Ops', 'Sales Ops', 'CS Analytics', 'CS Analytics',
        'Platform Team', 'Platform Team', 'Platform Team',
        'People Analytics', 'People Analytics', 'People Analytics',
        'Product Analytics', 'Product Analytics',
        'FP&A Team', 'FP&A Team',
        'Marketing Ops', 'Marketing Ops',
        'Data Governance Team', 'Data Governance Team'
    ],
    'unit_of_measure': [
        'USD (Millions)', 'USD (Millions)', 'Percentage',
        'Percentage', 'Percentage', 'Percentage',
        'USD', 'USD', 'Score (-100 to 100)', 'Percentage',
        'Percentage', 'Milliseconds', 'Hours',
        'Score (1-10)', 'Percentage', 'Percentage',
        'Story Points', 'Releases/Month',
        'Days', 'Ratio',
        'Count', 'Percentage',
        'Score (0-100)', 'Percentage'
    ],
    'calculation_method': [
        'SUM(all_revenue_streams)', 'SUM(subscription_revenue)', '(current_rev - prior_rev) / prior_rev * 100',
        '(revenue - cogs) / revenue * 100', 'operating_income / revenue * 100', '(ebit + depreciation + amortization) / revenue * 100',
        'total_sales_marketing_cost / new_customers', 'avg_revenue_per_customer * avg_customer_lifespan', 'promoters% - detractors%', 'churned_customers / total_customers * 100',
        'uptime_minutes / total_minutes * 100', 'AVG(response_time_ms)', 'AVG(time_to_resolution)',
        'AVG(survey_scores)', 'departed_employees / avg_headcount * 100', 'completed_trainings / assigned_trainings * 100',
        'AVG(story_points_completed)', 'COUNT(releases)', 
        'AVG(accounts_receivable / daily_sales)', 'current_assets / current_liabilities',
        'COUNT(qualified_leads)', 'conversions / total_leads * 100',
        'weighted_avg(completeness, accuracy, timeliness, consistency)', 'accurate_reports / total_reports * 100'
    ],
    'data_source': [
        'SAP ERP', 'Salesforce', 'SAP ERP',
        'SAP ERP', 'SAP ERP', 'SAP ERP',
        'Salesforce + Marketo', 'Salesforce', 'Medallia', 'Salesforce',
        'Datadog', 'Datadog', 'ServiceNow',
        'Workday + Culture Amp', 'Workday', 'Workday',
        'Jira', 'GitHub',
        'SAP ERP', 'SAP ERP',
        'Marketo', 'Salesforce',
        'Monte Carlo', 'Tableau Server Logs'
    ],
    'refresh_frequency': [
        'Monthly', 'Monthly', 'Quarterly',
        'Monthly', 'Monthly', 'Monthly',
        'Monthly', 'Quarterly', 'Quarterly', 'Monthly',
        'Real-time', 'Real-time', 'Daily',
        'Quarterly', 'Monthly', 'Monthly',
        'Bi-weekly', 'Monthly',
        'Monthly', 'Monthly',
        'Weekly', 'Monthly',
        'Daily', 'Daily'
    ],
    'target_q4_2024': [
        85.0, 72.0, 15.0,
        68.0, 22.0, 28.0,
        1200, 15000, 55, 2.5,
        99.95, 150, 4.0,
        8.2, 12.0, 95.0,
        45, 8,
        35, 2.0,
        850, 4.5,
        92.0, 98.5
    ],
    'criticality': [
        'Critical', 'Critical', 'Critical',
        'High', 'High', 'High',
        'High', 'High', 'Medium', 'Critical',
        'Critical', 'High', 'Medium',
        'Medium', 'High', 'Medium',
        'Medium', 'Medium',
        'High', 'Medium',
        'High', 'High',
        'High', 'High'
    ]
})

# =============================================================================
# 2. KPI HIERARCHY (Company -> Department -> Team -> Individual)
# =============================================================================

kpi_hierarchy = pd.DataFrame({
    'level': ['L1', 'L1', 'L1', 'L2', 'L2', 'L2', 'L2', 'L2', 'L2', 'L3', 'L3', 'L3', 'L3', 'L3', 'L3'],
    'parent_objective': [
        'Company Growth', 'Company Growth', 'Company Growth',
        'Revenue Excellence', 'Revenue Excellence', 'Operational Excellence', 
        'Operational Excellence', 'Customer Success', 'Customer Success',
        'Sales Efficiency', 'Sales Efficiency', 'Platform Reliability',
        'Platform Reliability', 'Customer Retention', 'Customer Retention'
    ],
    'objective_name': [
        'Increase Revenue 15% YoY', 'Achieve 25% EBITDA Margin', 'Reach 99.9% Platform Reliability',
        'Grow ARR to $72M', 'Reduce CAC by 10%', 'Maintain 99.95% Uptime',
        'Reduce Incident Resolution <4hrs', 'Achieve NPS >55', 'Reduce Churn <2.5%',
        'Generate 850+ MQLs/month', 'Improve Conversion to 4.5%', 'Response Time <150ms',
        'Zero Critical Incidents', 'Improve Customer Health Score', 'Proactive Outreach Program'
    ],
    'key_metrics': [
        'REV001, REV003', 'PROF003', 'OPS001',
        'REV002', 'CUST001', 'OPS001',
        'OPS003', 'CUST003', 'CUST004',
        'MKT001', 'MKT002', 'OPS002',
        'OPS003', 'CUST003, CUST002', 'CUST004'
    ],
    'owner': [
        'CEO', 'CEO', 'CEO',
        'CFO', 'CRO', 'CTO',
        'CTO', 'VP CS', 'VP CS',
        'CMO', 'CMO', 'VP Engineering',
        'VP Engineering', 'Director CS', 'Director CS'
    ],
    'weight': [40, 35, 25, 50, 50, 60, 40, 50, 50, 60, 40, 50, 50, 60, 40]
})

# =============================================================================
# 3. QUARTERLY KPI ACTUALS (Q1-Q4 2024 with Q4 2023 for comparison)
# =============================================================================

quarters = ['Q4 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']

# Based on real S&P 500 tech sector performance: ~17% revenue growth, strong margins
kpi_actuals = []

base_values = {
    'REV001': [68.5, 72.3, 76.8, 80.2, 84.1],  # Total Revenue growing ~15%
    'REV002': [55.2, 58.9, 63.1, 67.4, 71.2],  # ARR growing stronger
    'REV003': [12.8, 14.2, 15.8, 16.1, 14.9],  # Revenue Growth YoY
    'PROF001': [65.2, 66.1, 67.3, 67.8, 68.2], # Gross Margin improving
    'PROF002': [18.5, 19.2, 20.1, 21.3, 22.1], # Operating Margin
    'PROF003': [24.1, 25.2, 26.4, 27.1, 27.8], # EBITDA Margin
    'CUST001': [1450, 1380, 1320, 1280, 1210], # CAC improving (lower is better)
    'CUST002': [13200, 13800, 14200, 14600, 14900], # LTV increasing
    'CUST003': [48, 50, 52, 53, 54],  # NPS improving
    'CUST004': [3.2, 2.9, 2.7, 2.6, 2.5],  # Churn decreasing (lower is better)
    'OPS001': [99.91, 99.93, 99.94, 99.95, 99.96], # Uptime improving
    'OPS002': [185, 172, 162, 155, 148], # Response time improving (lower is better)
    'OPS003': [5.2, 4.8, 4.5, 4.2, 3.9], # Incident resolution improving
    'EMP001': [7.4, 7.6, 7.8, 8.0, 8.1], # Employee satisfaction
    'EMP002': [15.2, 14.1, 13.2, 12.8, 12.1], # Turnover decreasing
    'EMP003': [88, 90, 92, 94, 95], # Training completion
    'PROD001': [38, 40, 42, 44, 45], # Sprint velocity
    'PROD002': [5, 6, 7, 7, 8], # Release frequency
    'FIN001': [42, 40, 38, 36, 35], # DSO improving (lower is better)
    'FIN002': [1.8, 1.85, 1.9, 1.95, 2.0], # Working capital ratio
    'MKT001': [680, 720, 780, 820, 860], # MQLs growing
    'MKT002': [3.2, 3.5, 3.9, 4.2, 4.4], # Conversion rate
    'DATA001': [82, 85, 88, 90, 91], # Data quality score
    'DATA002': [95.2, 96.1, 97.0, 97.8, 98.2], # Report accuracy
}

for metric_id, values in base_values.items():
    for i, quarter in enumerate(quarters):
        # Add some variance
        variance = np.random.normal(0, 0.02)
        actual = values[i] * (1 + variance)
        target = metric_definitions[metric_definitions['metric_id'] == metric_id]['target_q4_2024'].values[0]
        
        kpi_actuals.append({
            'metric_id': metric_id,
            'period': quarter,
            'actual_value': round(actual, 2),
            'target_value': target if quarter == 'Q4 2024' else round(target * (0.85 + i * 0.04), 2),
            'variance_pct': round((actual - target) / target * 100, 2) if quarter == 'Q4 2024' else None,
            'status': 'On Track' if actual >= target * 0.95 else ('At Risk' if actual >= target * 0.85 else 'Off Track'),
            'last_updated': datetime.now().strftime('%Y-%m-%d'),
            'data_quality_flag': random.choice(['Valid', 'Valid', 'Valid', 'Valid', 'Needs Review'])
        })

kpi_actuals_df = pd.DataFrame(kpi_actuals)

# =============================================================================
# 4. DATA QUALITY CHECKS & ANOMALIES
# =============================================================================

data_quality_issues = pd.DataFrame({
    'issue_id': [f'DQ{str(i).zfill(3)}' for i in range(1, 16)],
    'metric_id': ['REV001', 'CUST001', 'OPS002', 'MKT001', 'CUST002', 
                  'PROF002', 'EMP002', 'PROD001', 'FIN001', 'DATA001',
                  'REV002', 'CUST003', 'OPS001', 'MKT002', 'EMP001'],
    'issue_type': ['Missing Data', 'Outlier', 'Data Latency', 'Duplicate Records', 'Schema Drift',
                   'Calculation Error', 'Source Disconnect', 'Incomplete Load', 'Freshness', 'Validation Failure',
                   'Missing Data', 'Outlier', 'Data Latency', 'Schema Drift', 'Source Disconnect'],
    'severity': ['Medium', 'High', 'Low', 'Medium', 'High',
                 'Critical', 'Medium', 'Low', 'Medium', 'High',
                 'Low', 'Medium', 'Low', 'Medium', 'Low'],
    'detected_date': [
        '2024-10-15', '2024-10-18', '2024-10-20', '2024-10-22', '2024-10-25',
        '2024-11-01', '2024-11-05', '2024-11-08', '2024-11-12', '2024-11-15',
        '2024-11-18', '2024-11-20', '2024-11-22', '2024-11-25', '2024-11-28'
    ],
    'resolution_date': [
        '2024-10-16', '2024-10-20', '2024-10-21', '2024-10-24', '2024-10-28',
        '2024-11-02', '2024-11-08', '2024-11-09', '2024-11-14', None,
        '2024-11-19', None, '2024-11-23', None, None
    ],
    'status': ['Resolved', 'Resolved', 'Resolved', 'Resolved', 'Resolved',
               'Resolved', 'Resolved', 'Resolved', 'Resolved', 'Open',
               'Resolved', 'Open', 'Resolved', 'Open', 'Open'],
    'impact_description': [
        'Missing 3 days of revenue data from EMEA region',
        'CAC value 3x higher than historical average - data entry error',
        'API response time data delayed by 6 hours',
        '12 duplicate MQL records from Marketo sync',
        'LTV calculation changed without documentation',
        'Operating margin formula excluded R&D costs incorrectly',
        'Workday connector failed for 2 hours',
        'Sprint data missing for Mobile team',
        'DSO data 24 hours stale',
        'Data quality score validation rules failing',
        '1 day of ARR data missing from APAC',
        'NPS score outlier from test survey responses',
        'Datadog metrics delayed 30 minutes',
        'Conversion rate schema changed in Salesforce',
        'Culture Amp integration down for maintenance'
    ],
    'root_cause': [
        'ETL job failed', 'Manual entry error', 'API rate limiting', 'Webhook duplication', 'Undocumented change',
        'Formula update error', 'Auth token expired', 'Timeout issue', 'Scheduler delay', 'Rule conflict',
        'Network timeout', 'Test data leaked', 'Provider issue', 'Salesforce update', 'Scheduled maintenance'
    ],
    'assigned_to': [
        'Finance Analytics', 'Sales Ops', 'Platform Team', 'Marketing Ops', 'Data Governance',
        'Finance Analytics', 'People Analytics', 'Product Analytics', 'FP&A Team', 'Data Governance',
        'Finance Analytics', 'CS Analytics', 'Platform Team', 'Marketing Ops', 'People Analytics'
    ]
})

# =============================================================================
# 5. METRIC DRIFT & INCONSISTENCIES LOG
# =============================================================================

metric_drift_log = pd.DataFrame({
    'drift_id': [f'MD{str(i).zfill(3)}' for i in range(1, 11)],
    'metric_id': ['REV003', 'CUST002', 'PROF002', 'CUST001', 'OPS001',
                  'MKT002', 'EMP002', 'FIN001', 'PROD001', 'DATA001'],
    'drift_type': [
        'Definition Change', 'Calculation Drift', 'Source Change', 'Methodology Update',
        'Threshold Change', 'Formula Update', 'Source Migration', 'Aggregation Change',
        'Unit Change', 'Weight Adjustment'
    ],
    'old_definition': [
        'YoY growth including one-time revenue',
        'LTV = ARPU * 36 months',
        'Op Margin = EBIT / Revenue',
        'CAC = (S&M spend) / new customers',
        'Uptime excludes planned maintenance',
        'Conversion = Won / Total Opps',
        'Turnover = Voluntary exits only',
        'DSO = AR / (Revenue/365)',
        'Velocity in hours',
        'Equal weight for all dimensions'
    ],
    'new_definition': [
        'YoY growth excluding one-time revenue',
        'LTV = ARPU * Avg Customer Tenure',
        'Op Margin = EBIT / Revenue (excl. restructuring)',
        'CAC = (S&M spend + overhead allocation) / new customers',
        'Uptime includes planned maintenance',
        'Conversion = Won / Qualified Opps only',
        'Turnover = All exits (vol + invol)',
        'DSO = AR / (Revenue/90) for quarterly',
        'Velocity in story points',
        'Weighted: Accuracy 40%, Completeness 30%, Timeliness 20%, Consistency 10%'
    ],
    'change_date': [
        '2024-01-15', '2024-02-01', '2024-03-01', '2024-04-15', '2024-05-01',
        '2024-06-01', '2024-07-01', '2024-08-01', '2024-09-01', '2024-10-01'
    ],
    'approved_by': [
        'CFO', 'CRO', 'CFO', 'CRO', 'CTO',
        'CMO', 'CHRO', 'Controller', 'CPO', 'CDO'
    ],
    'impact_on_historical': [
        'Restated Q1-Q4 2023', 'Restated from Q3 2023', 'No restatement needed', 
        'Restated Q1-Q4 2024', 'Restated from Q1 2024',
        'Restated from Q2 2024', 'No restatement - forward only', 'Restated from Q1 2024',
        'No restatement - different measure', 'Restated from Q3 2024'
    ],
    'communication_status': [
        'Board notified', 'Exec team notified', 'Finance team notified',
        'Sales team notified', 'Engineering notified', 'Marketing notified',
        'HR team notified', 'Finance team notified', 'Product team notified',
        'Data Council notified'
    ]
})

# =============================================================================
# 6. OKR TRACKING DATA
# =============================================================================

okr_data = pd.DataFrame({
    'okr_id': [f'OKR-2024-{str(i).zfill(2)}' for i in range(1, 16)],
    'objective': [
        'Accelerate Revenue Growth',
        'Accelerate Revenue Growth',
        'Accelerate Revenue Growth',
        'Achieve Operational Excellence',
        'Achieve Operational Excellence',
        'Achieve Operational Excellence',
        'Build World-Class Culture',
        'Build World-Class Culture',
        'Build World-Class Culture',
        'Deliver Product Innovation',
        'Deliver Product Innovation',
        'Deliver Product Innovation',
        'Strengthen Data Foundation',
        'Strengthen Data Foundation',
        'Strengthen Data Foundation'
    ],
    'key_result': [
        'Grow ARR from $55M to $72M',
        'Reduce customer churn from 3.2% to 2.5%',
        'Increase LTV/CAC ratio from 9.1 to 12.3',
        'Achieve 99.95% platform uptime',
        'Reduce mean time to resolution to <4 hours',
        'Reduce API response time to <150ms',
        'Increase employee satisfaction to 8.2+',
        'Reduce turnover rate to <12%',
        'Achieve 95% training completion rate',
        'Increase sprint velocity by 20%',
        'Release 8 major features per quarter',
        'Achieve 55+ NPS score',
        'Achieve 92%+ data quality score',
        'Reach 98.5% report accuracy',
        'Zero critical data incidents'
    ],
    'owner': [
        'CFO', 'VP CS', 'CRO',
        'CTO', 'VP Engineering', 'VP Engineering',
        'CHRO', 'CHRO', 'Director L&D',
        'CPO', 'VP Engineering', 'CPO',
        'CDO', 'CDO', 'VP Data Engineering'
    ],
    'start_value': [55.2, 3.2, 9.1, 99.91, 5.2, 185, 7.4, 15.2, 88, 38, 5, 48, 82, 95.2, 3],
    'target_value': [72.0, 2.5, 12.3, 99.95, 4.0, 150, 8.2, 12.0, 95, 45, 8, 55, 92, 98.5, 0],
    'current_value': [71.2, 2.5, 11.7, 99.96, 3.9, 148, 8.1, 12.1, 95, 45, 8, 54, 91, 98.2, 0],
    'progress_pct': [95, 100, 87, 100, 100, 100, 88, 97, 100, 100, 100, 86, 90, 94, 100],
    'status': [
        'On Track', 'Achieved', 'At Risk',
        'Achieved', 'Achieved', 'Achieved',
        'At Risk', 'On Track', 'Achieved',
        'Achieved', 'Achieved', 'At Risk',
        'On Track', 'On Track', 'Achieved'
    ],
    'confidence': [0.9, 1.0, 0.7, 1.0, 1.0, 1.0, 0.6, 0.85, 1.0, 1.0, 1.0, 0.7, 0.8, 0.85, 1.0],
    'linked_metric_ids': [
        'REV002', 'CUST004', 'CUST001,CUST002',
        'OPS001', 'OPS003', 'OPS002',
        'EMP001', 'EMP002', 'EMP003',
        'PROD001', 'PROD002', 'CUST003',
        'DATA001', 'DATA002', 'DATA001'
    ]
})

# =============================================================================
# 7. EXECUTIVE DECISION LOG
# =============================================================================

decision_log = pd.DataFrame({
    'decision_id': [f'DEC-2024-{str(i).zfill(3)}' for i in range(1, 11)],
    'decision_date': [
        '2024-01-25', '2024-02-15', '2024-03-20', '2024-04-18', '2024-05-22',
        '2024-06-15', '2024-07-25', '2024-08-20', '2024-09-18', '2024-10-24'
    ],
    'decision_title': [
        'Increase Q2 Marketing Budget by 15%',
        'Accelerate APAC Expansion',
        'Implement AI-Powered Customer Support',
        'Restructure Sales Territories',
        'Launch Enterprise Tier',
        'Hire 50 Additional Engineers',
        'Acquire DataSync Inc.',
        'Implement Hybrid Work Policy',
        'Launch Customer Success Platform',
        'Q4 Budget Reallocation'
    ],
    'decision_maker': [
        'CEO + CFO', 'CEO + Board', 'CEO + CTO', 'CEO + CRO', 'CEO + CPO',
        'CEO + CTO', 'CEO + Board', 'CEO + CHRO', 'CEO + VP CS', 'CEO + CFO'
    ],
    'kpis_considered': [
        'MKT001, MKT002, CUST001', 'REV001, REV002, REV003', 'OPS002, OPS003, CUST003',
        'MKT002, CUST001, REV002', 'REV001, REV002, CUST002', 'PROD001, PROD002, OPS001',
        'DATA001, DATA002, REV002', 'EMP001, EMP002, EMP003', 'CUST003, CUST004, CUST002',
        'REV001, PROF002, PROF003'
    ],
    'expected_impact': [
        '+20% MQLs, +0.5% conversion', '+$8M ARR from APAC by Q4', '-30% response time, +5 NPS points',
        '+15% territory coverage, -$100 CAC', '+$15M enterprise revenue', '+25% sprint velocity',
        '+10 points data quality score', '+0.5 employee satisfaction', '-0.3% churn rate',
        'Maintain 25% EBITDA while growing revenue'
    ],
    'actual_impact': [
        '+22% MQLs, +0.6% conversion', '+$7.2M ARR from APAC', '-35% response time, +4 NPS points',
        '+12% territory coverage, -$80 CAC', 'In progress - tracking +$12M', '+22% sprint velocity',
        '+9 points data quality score', '+0.5 employee satisfaction', '-0.4% churn rate',
        'Pending Q4 close'
    ],
    'confidence_level': [
        'High (90%)', 'High (85%)', 'High (92%)', 'Medium (75%)', 'Medium (70%)',
        'High (88%)', 'High (85%)', 'High (90%)', 'High (88%)', 'Pending'
    ],
    'status': [
        'Completed - Exceeded', 'Completed - Met', 'Completed - Exceeded', 'Completed - Partial',
        'In Progress', 'Completed - Met', 'Completed - Met', 'Completed - Met', 'Completed - Exceeded', 'In Progress'
    ]
})

# =============================================================================
# SAVE ALL DATA
# =============================================================================

if __name__ == "__main__":
    metric_definitions.to_csv('data/metric_definitions.csv', index=False)
    kpi_hierarchy.to_csv('data/kpi_hierarchy.csv', index=False)
    kpi_actuals_df.to_csv('data/kpi_actuals.csv', index=False)
    data_quality_issues.to_csv('data/data_quality_issues.csv', index=False)
    metric_drift_log.to_csv('data/metric_drift_log.csv', index=False)
    okr_data.to_csv('data/okr_tracking.csv', index=False)
    decision_log.to_csv('data/decision_log.csv', index=False)

    print("Data generation complete!")
    print(f"Metric Definitions: {len(metric_definitions)} records")
    print(f"KPI Hierarchy: {len(kpi_hierarchy)} records")
    print(f"KPI Actuals: {len(kpi_actuals_df)} records")
    print(f"Data Quality Issues: {len(data_quality_issues)} records")
    print(f"Metric Drift Log: {len(metric_drift_log)} records")
    print(f"OKR Tracking: {len(okr_data)} records")
    print(f"Decision Log: {len(decision_log)} records")


# ============================================================================
# FILE 2: scripts/kpi_analysis.py - VISUALIZATION SCRIPT
# ============================================================================

"""
Executive Decision Analytics & KPI Governance System
Comprehensive Analysis & Visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['figure.facecolor'] = 'white'

# Load data
metric_definitions = pd.read_csv('data/metric_definitions.csv')
kpi_hierarchy = pd.read_csv('data/kpi_hierarchy.csv')
kpi_actuals = pd.read_csv('data/kpi_actuals.csv')
data_quality_issues = pd.read_csv('data/data_quality_issues.csv')
metric_drift_log = pd.read_csv('data/metric_drift_log.csv')
okr_data = pd.read_csv('data/okr_tracking.csv')
decision_log = pd.read_csv('data/decision_log.csv')

# Color palette
colors = {
    'primary': '#1a365d',
    'secondary': '#2c5282',
    'success': '#38a169',
    'warning': '#dd6b20',
    'danger': '#e53e3e',
    'info': '#3182ce',
    'light': '#e2e8f0',
    'dark': '#2d3748',
    'revenue': '#3182ce',
    'profitability': '#38a169',
    'customer': '#805ad5',
    'operations': '#dd6b20',
    'people': '#d53f8c',
    'product': '#00b5d8',
    'finance': '#319795',
    'marketing': '#ed8936',
    'data_governance': '#667eea'
}

category_colors = {
    'Revenue': colors['revenue'],
    'Profitability': colors['profitability'],
    'Customer': colors['customer'],
    'Operations': colors['operations'],
    'People': colors['people'],
    'Product': colors['product'],
    'Finance': colors['finance'],
    'Marketing': colors['marketing'],
    'Data Governance': colors['data_governance']
}

# =============================================================================
# FIGURE 1: EXECUTIVE KPI DASHBOARD
# =============================================================================

def create_executive_dashboard():
    fig1 = plt.figure(figsize=(16, 12))
    fig1.suptitle('TechVantage Inc. - Executive KPI Dashboard Q4 2024', 
                  fontsize=16, fontweight='bold', y=0.98)

    gs = GridSpec(3, 3, figure=fig1, hspace=0.3, wspace=0.3)

    # 1.1 KPI Performance Overview by Category
    ax1 = fig1.add_subplot(gs[0, :2])
    q4_actuals = kpi_actuals[kpi_actuals['period'] == 'Q4 2024'].merge(
        metric_definitions[['metric_id', 'category', 'target_q4_2024']], on='metric_id'
    )
    q4_actuals['performance'] = np.where(
        q4_actuals['actual_value'] >= q4_actuals['target_q4_2024'] * 0.95, 
        'On Track', 
        np.where(q4_actuals['actual_value'] >= q4_actuals['target_q4_2024'] * 0.85, 'At Risk', 'Off Track')
    )

    category_performance = q4_actuals.groupby('category').agg({
        'metric_id': 'count',
        'performance': lambda x: (x == 'On Track').sum() / len(x) * 100
    }).reset_index()
    category_performance.columns = ['Category', 'Metric Count', 'Pct On Track']
    category_performance = category_performance.sort_values('Pct On Track', ascending=True)

    bars = ax1.barh(category_performance['Category'], category_performance['Pct On Track'],
                    color=[category_colors.get(c, colors['primary']) for c in category_performance['Category']])
    ax1.axvline(x=80, color=colors['warning'], linestyle='--', label='80% Threshold', alpha=0.7)
    ax1.axvline(x=95, color=colors['success'], linestyle='--', label='95% Target', alpha=0.7)

    for i, (v, c) in enumerate(zip(category_performance['Pct On Track'], category_performance['Metric Count'])):
        ax1.text(v + 1, i, f'{v:.0f}% ({c} KPIs)', va='center', fontsize=9)

    ax1.set_xlabel('% Metrics On Track')
    ax1.set_title('KPI Performance by Category', fontweight='bold')
    ax1.set_xlim(0, 110)
    ax1.legend(loc='lower right')

    # 1.2 Critical KPIs Status
    ax2 = fig1.add_subplot(gs[0, 2])
    critical_kpis = q4_actuals[q4_actuals['metric_id'].isin(
        metric_definitions[metric_definitions['criticality'] == 'Critical']['metric_id']
    )]
    status_counts = critical_kpis['performance'].value_counts()
    status_colors_list = [colors['success'] if s == 'On Track' else colors['warning'] if s == 'At Risk' else colors['danger'] 
                     for s in status_counts.index]
    wedges, texts, autotexts = ax2.pie(status_counts.values, labels=status_counts.index, autopct='%1.0f%%',
                                        colors=status_colors_list, startangle=90, explode=[0.02]*len(status_counts))
    ax2.set_title('Critical KPIs Status', fontweight='bold')

    # 1.3 Revenue Trend
    ax3 = fig1.add_subplot(gs[1, 0])
    revenue_data = kpi_actuals[kpi_actuals['metric_id'] == 'REV001'].sort_values('period')
    ax3.plot(revenue_data['period'], revenue_data['actual_value'], 'o-', color=colors['revenue'], 
             linewidth=2, markersize=8, label='Actual')
    ax3.fill_between(revenue_data['period'], revenue_data['actual_value'], alpha=0.3, color=colors['revenue'])
    target = metric_definitions[metric_definitions['metric_id'] == 'REV001']['target_q4_2024'].values[0]
    ax3.axhline(y=target, color=colors['success'], linestyle='--', label=f'Q4 Target: ${target}M')
    ax3.set_ylabel('Revenue ($M)')
    ax3.set_title('Total Revenue Trend', fontweight='bold')
    ax3.legend(loc='upper left', fontsize=8)
    ax3.tick_params(axis='x', rotation=45)

    # 1.4 Profitability Metrics
    ax4 = fig1.add_subplot(gs[1, 1])
    profit_metrics = ['PROF001', 'PROF002', 'PROF003']
    profit_names = ['Gross Margin', 'Op Margin', 'EBITDA']
    q4_profit = kpi_actuals[(kpi_actuals['metric_id'].isin(profit_metrics)) & 
                            (kpi_actuals['period'] == 'Q4 2024')]
    q4_profit = q4_profit.merge(metric_definitions[['metric_id', 'target_q4_2024']], on='metric_id')

    x = np.arange(len(profit_names))
    width = 0.35
    bars1 = ax4.bar(x - width/2, q4_profit['actual_value'], width, label='Actual', color=colors['profitability'])
    bars2 = ax4.bar(x + width/2, q4_profit['target_q4_2024'], width, label='Target', color=colors['light'], edgecolor=colors['profitability'])
    ax4.set_xticks(x)
    ax4.set_xticklabels(profit_names)
    ax4.set_ylabel('Margin (%)')
    ax4.set_title('Profitability Metrics', fontweight='bold')
    ax4.legend()

    for bar, val in zip(bars1, q4_profit['actual_value']):
        ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f'{val:.1f}%', 
                 ha='center', va='bottom', fontsize=9)

    # 1.5 Customer Health
    ax5 = fig1.add_subplot(gs[1, 2])
    customer_metrics = ['CUST003', 'CUST004']
    cust_data = kpi_actuals[kpi_actuals['metric_id'].isin(customer_metrics)]
    cust_pivot = cust_data.pivot(index='period', columns='metric_id', values='actual_value')

    ax5_twin = ax5.twinx()
    ax5.plot(cust_pivot.index, cust_pivot['CUST003'], 'o-', color=colors['customer'], 
             linewidth=2, label='NPS Score')
    ax5_twin.plot(cust_pivot.index, cust_pivot['CUST004'], 's--', color=colors['danger'], 
                  linewidth=2, label='Churn Rate %')
    ax5.set_ylabel('NPS Score', color=colors['customer'])
    ax5_twin.set_ylabel('Churn Rate %', color=colors['danger'])
    ax5.set_title('Customer Health Indicators', fontweight='bold')
    ax5.tick_params(axis='x', rotation=45)
    ax5.legend(loc='upper left', fontsize=8)
    ax5_twin.legend(loc='upper right', fontsize=8)

    # 1.6 Operations Performance
    ax6 = fig1.add_subplot(gs[2, 0])
    ops_data = kpi_actuals[kpi_actuals['metric_id'] == 'OPS001'].sort_values('period')
    ax6.bar(ops_data['period'], ops_data['actual_value'], color=colors['operations'], alpha=0.8)
    ax6.axhline(y=99.95, color=colors['success'], linestyle='--', label='Target: 99.95%')
    ax6.set_ylabel('Uptime %')
    ax6.set_ylim(99.85, 100)
    ax6.set_title('Platform Uptime', fontweight='bold')
    ax6.legend()
    ax6.tick_params(axis='x', rotation=45)

    # 1.7 Data Quality Trend
    ax7 = fig1.add_subplot(gs[2, 1])
    dq_data = kpi_actuals[kpi_actuals['metric_id'] == 'DATA001'].sort_values('period')
    ax7.fill_between(dq_data['period'], dq_data['actual_value'], alpha=0.3, color=colors['data_governance'])
    ax7.plot(dq_data['period'], dq_data['actual_value'], 'o-', color=colors['data_governance'], 
             linewidth=2, markersize=8)
    ax7.axhline(y=92, color=colors['success'], linestyle='--', label='Target: 92%')
    ax7.set_ylabel('Data Quality Score')
    ax7.set_title('Data Quality Score Trend', fontweight='bold')
    ax7.legend()
    ax7.tick_params(axis='x', rotation=45)

    # 1.8 Key Metrics Summary Table
    ax8 = fig1.add_subplot(gs[2, 2])
    ax8.axis('off')
    summary_data = [
        ['Total Revenue', '$84.1M', '+14.9% YoY', '✅'],
        ['ARR', '$71.2M', '+29.0% YoY', '✅'],
        ['EBITDA Margin', '27.8%', '+3.7pp', '✅'],
        ['NPS Score', '54', '+6 pts', '🔶'],
        ['Churn Rate', '2.5%', '-0.7pp', '✅'],
        ['Uptime', '99.96%', '+0.05pp', '✅'],
    ]
    table = ax8.table(cellText=summary_data,
                      colLabels=['Metric', 'Value', 'Change', 'Status'],
                      loc='center',
                      cellLoc='center',
                      colColours=[colors['light']]*4)
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.2, 1.5)
    ax8.set_title('Q4 2024 Key Metrics Summary', fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig('outputs/01_executive_dashboard.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✅ Figure 1: Executive Dashboard created")

# =============================================================================
# FIGURE 2: OKR TRACKING & PERFORMANCE
# =============================================================================

def create_okr_dashboard():
    fig2 = plt.figure(figsize=(16, 10))
    fig2.suptitle('TechVantage Inc. - OKR Tracking Dashboard 2024', 
                  fontsize=16, fontweight='bold', y=0.98)

    gs2 = GridSpec(2, 3, figure=fig2, hspace=0.35, wspace=0.3)

    # 2.1 OKR Progress by Objective
    ax1 = fig2.add_subplot(gs2[0, :2])
    obj_progress = okr_data.groupby('objective').agg({
        'progress_pct': 'mean',
        'key_result': 'count',
        'status': lambda x: (x == 'Achieved').sum()
    }).reset_index()
    obj_progress.columns = ['Objective', 'Avg Progress', 'KRs', 'Achieved']
    obj_progress = obj_progress.sort_values('Avg Progress', ascending=True)

    colors_obj = [colors['success'] if p >= 90 else colors['warning'] if p >= 70 else colors['danger'] 
                  for p in obj_progress['Avg Progress']]
    bars = ax1.barh(obj_progress['Objective'], obj_progress['Avg Progress'], color=colors_obj)
    ax1.axvline(x=70, color=colors['warning'], linestyle='--', alpha=0.5, label='70% Threshold')
    ax1.axvline(x=90, color=colors['success'], linestyle='--', alpha=0.5, label='90% Target')

    for i, (prog, krs, ach) in enumerate(zip(obj_progress['Avg Progress'], obj_progress['KRs'], obj_progress['Achieved'])):
        ax1.text(prog + 1, i, f'{prog:.0f}% ({ach}/{krs} KRs)', va='center', fontsize=9)

    ax1.set_xlabel('Average Progress %')
    ax1.set_title('OKR Progress by Strategic Objective', fontweight='bold')
    ax1.set_xlim(0, 115)
    ax1.legend(loc='lower right')

    # 2.2 OKR Status Distribution
    ax2 = fig2.add_subplot(gs2[0, 2])
    status_dist = okr_data['status'].value_counts()
    status_colors_map = {'Achieved': colors['success'], 'On Track': colors['info'], 
                         'At Risk': colors['warning'], 'Off Track': colors['danger']}
    wedges, texts, autotexts = ax2.pie(status_dist.values, 
                                        labels=[f"{k}\n({v})" for k,v in status_dist.items()], 
                                        autopct='%1.0f%%',
                                        colors=[status_colors_map.get(s, colors['light']) for s in status_dist.index],
                                        startangle=90, explode=[0.03]*len(status_dist))
    ax2.set_title('OKR Status Distribution', fontweight='bold')

    # 2.3 Key Results Progress Detail
    ax3 = fig2.add_subplot(gs2[1, :])
    kr_data = okr_data[['key_result', 'start_value', 'current_value', 'target_value', 'progress_pct', 'status']].copy()
    kr_data = kr_data.sort_values('progress_pct', ascending=False).head(12)

    y_pos = np.arange(len(kr_data))
    progress_colors = [colors['success'] if s == 'Achieved' else colors['info'] if s == 'On Track' 
                       else colors['warning'] for s in kr_data['status']]

    bars = ax3.barh(y_pos, kr_data['progress_pct'], color=progress_colors, height=0.6)
    ax3.axvline(x=100, color=colors['dark'], linestyle='-', alpha=0.3)

    for i, (kr, prog, status) in enumerate(zip(kr_data['key_result'], kr_data['progress_pct'], kr_data['status'])):
        ax3.text(2, i, kr[:50] + ('...' if len(kr) > 50 else ''), va='center', fontsize=8, fontweight='bold')
        icon = '✅' if status == 'Achieved' else '🟢' if status == 'On Track' else '🟠'
        ax3.text(prog + 1, i, f'{prog:.0f}% {icon}', va='center', fontsize=8)

    ax3.set_yticks([])
    ax3.set_xlabel('Progress %')
    ax3.set_title('Key Results Progress (Top 12)', fontweight='bold')
    ax3.set_xlim(0, 115)

    legend_elements = [mpatches.Patch(facecolor=colors['success'], label='Achieved'),
                       mpatches.Patch(facecolor=colors['info'], label='On Track'),
                       mpatches.Patch(facecolor=colors['warning'], label='At Risk')]
    ax3.legend(handles=legend_elements, loc='lower right')

    plt.tight_layout()
    plt.savefig('outputs/02_okr_tracking.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✅ Figure 2: OKR Tracking Dashboard created")

# =============================================================================
# FIGURE 3: DATA QUALITY & GOVERNANCE
# =============================================================================

def create_data_governance_dashboard():
    fig3 = plt.figure(figsize=(16, 10))
    fig3.suptitle('TechVantage Inc. - Data Quality & Governance Report', 
                  fontsize=16, fontweight='bold', y=0.98)

    gs3 = GridSpec(2, 3, figure=fig3, hspace=0.35, wspace=0.3)

    # 3.1 Data Quality Issues by Severity
    ax1 = fig3.add_subplot(gs3[0, 0])
    severity_counts = data_quality_issues['severity'].value_counts()
    severity_order = ['Critical', 'High', 'Medium', 'Low']
    severity_counts = severity_counts.reindex(severity_order)
    severity_colors = [colors['danger'], colors['warning'], colors['info'], colors['success']]
    bars = ax1.bar(severity_counts.index, severity_counts.values, color=severity_colors)
    for bar, val in zip(bars, severity_counts.values):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, str(val), 
                 ha='center', va='bottom', fontweight='bold')
    ax1.set_ylabel('Number of Issues')
    ax1.set_title('Data Quality Issues by Severity', fontweight='bold')

    # 3.2 Issue Resolution Status
    ax2 = fig3.add_subplot(gs3[0, 1])
    status_counts = data_quality_issues['status'].value_counts()
    colors_status = [colors['success'] if s == 'Resolved' else colors['warning'] for s in status_counts.index]
    wedges, texts, autotexts = ax2.pie(status_counts.values, labels=status_counts.index, 
                                        autopct='%1.0f%%', colors=colors_status,
                                        startangle=90, explode=[0.02, 0.02])
    ax2.set_title('Issue Resolution Status', fontweight='bold')
    center_text = f'{status_counts.get("Resolved", 0)}/{status_counts.sum()}\nResolved'
    ax2.text(0, 0, center_text, ha='center', va='center', fontsize=10, fontweight='bold')

    # 3.3 Issues by Type
    ax3 = fig3.add_subplot(gs3[0, 2])
    type_counts = data_quality_issues['issue_type'].value_counts().head(8)
    ax3.barh(type_counts.index, type_counts.values, color=colors['data_governance'])
    for i, v in enumerate(type_counts.values):
        ax3.text(v + 0.1, i, str(v), va='center')
    ax3.set_xlabel('Count')
    ax3.set_title('Issues by Type', fontweight='bold')

    # 3.4 Metric Definition Changes (Drift)
    ax4 = fig3.add_subplot(gs3[1, 0])
    drift_by_type = metric_drift_log['drift_type'].value_counts()
    ax4.barh(drift_by_type.index, drift_by_type.values, color=colors['secondary'])
    for i, v in enumerate(drift_by_type.values):
        ax4.text(v + 0.05, i, str(v), va='center')
    ax4.set_xlabel('Count')
    ax4.set_title('Metric Definition Changes by Type', fontweight='bold')

    # 3.5 Governance Health by Metric
    ax5 = fig3.add_subplot(gs3[1, 1:])
    gov_health = metric_definitions.merge(
        data_quality_issues.groupby('metric_id')['status'].apply(lambda x: (x == 'Open').sum()).reset_index(),
        on='metric_id', how='left'
    ).fillna(0)
    gov_health.columns = list(gov_health.columns[:-1]) + ['open_issues']
    gov_health['health_status'] = np.where(
        (gov_health['criticality'] == 'Critical') & (gov_health['open_issues'] > 0), 'URGENT',
        np.where(gov_health['open_issues'] > 0, 'ATTENTION', 'HEALTHY')
    )

    health_summary = gov_health.groupby(['category', 'health_status']).size().unstack(fill_value=0)
    health_summary = health_summary.reindex(columns=['HEALTHY', 'ATTENTION', 'URGENT'], fill_value=0)

    x = np.arange(len(health_summary.index))
    width = 0.25
    bars1 = ax5.bar(x - width, health_summary['HEALTHY'], width, label='Healthy', color=colors['success'])
    bars2 = ax5.bar(x, health_summary['ATTENTION'], width, label='Attention', color=colors['warning'])
    bars3 = ax5.bar(x + width, health_summary['URGENT'], width, label='Urgent', color=colors['danger'])

    ax5.set_xticks(x)
    ax5.set_xticklabels(health_summary.index, rotation=45, ha='right')
    ax5.set_ylabel('Number of Metrics')
    ax5.set_title('Metric Governance Health by Category', fontweight='bold')
    ax5.legend()

    plt.tight_layout()
    plt.savefig('outputs/03_data_governance.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✅ Figure 3: Data Quality & Governance Report created")

# =============================================================================
# FIGURE 4: DECISION ANALYTICS
# =============================================================================

def create_decision_analytics_dashboard():
    fig4 = plt.figure(figsize=(16, 10))
    fig4.suptitle('TechVantage Inc. - Executive Decision Analytics', 
                  fontsize=16, fontweight='bold', y=0.98)

    gs4 = GridSpec(2, 2, figure=fig4, hspace=0.35, wspace=0.3)

    # 4.1 Decision Outcomes
    ax1 = fig4.add_subplot(gs4[0, 0])
    outcome_counts = decision_log['status'].value_counts()
    outcome_colors = {
        'Completed - Exceeded': colors['success'],
        'Completed - Met': colors['info'],
        'Completed - Partial': colors['warning'],
        'In Progress': colors['light']
    }
    wedges, texts, autotexts = ax1.pie(outcome_counts.values, 
                                        labels=outcome_counts.index,
                                        autopct='%1.0f%%',
                                        colors=[outcome_colors.get(s, colors['light']) for s in outcome_counts.index],
                                        startangle=90)
    ax1.set_title('Decision Outcomes Distribution', fontweight='bold')

    # 4.2 Decisions Timeline
    ax2 = fig4.add_subplot(gs4[0, 1])
    decision_log_copy = decision_log.copy()
    decision_log_copy['decision_date'] = pd.to_datetime(decision_log_copy['decision_date'])
    decision_log_copy['month'] = decision_log_copy['decision_date'].dt.to_period('M')
    monthly_decisions = decision_log_copy.groupby('month').size()
    ax2.bar(range(len(monthly_decisions)), monthly_decisions.values, color=colors['primary'])
    ax2.set_xticks(range(len(monthly_decisions)))
    ax2.set_xticklabels([str(m) for m in monthly_decisions.index], rotation=45, ha='right')
    ax2.set_ylabel('Number of Decisions')
    ax2.set_title('Strategic Decisions by Month (2024)', fontweight='bold')

    # 4.3 KPIs Most Frequently Considered
    ax3 = fig4.add_subplot(gs4[1, 0])
    kpi_mentions = []
    for kpis in decision_log['kpis_considered']:
        kpi_mentions.extend([k.strip() for k in kpis.split(',')])
    kpi_mention_counts = pd.Series(kpi_mentions).value_counts().head(10).reset_index()
    kpi_mention_counts.columns = ['metric_id', 'count']
    kpi_mention_counts = kpi_mention_counts.merge(
        metric_definitions[['metric_id', 'metric_name']], 
        on='metric_id', how='left'
    )
    bars = ax3.barh(kpi_mention_counts['metric_name'], kpi_mention_counts['count'], color=colors['secondary'])
    for i, v in enumerate(kpi_mention_counts['count']):
        ax3.text(v + 0.1, i, str(v), va='center')
    ax3.set_xlabel('Mentions in Decisions')
    ax3.set_title('Top KPIs Considered in Strategic Decisions', fontweight='bold')

    # 4.4 Decision Details Table
    ax4 = fig4.add_subplot(gs4[1, 1])
    ax4.axis('off')
    recent_decisions = decision_log.sort_values('decision_date', ascending=False).head(5)
    table_data = []
    for _, row in recent_decisions.iterrows():
        status_icon = '✅' if 'Exceeded' in row['status'] else '🟢' if 'Met' in row['status'] else '🟡' if 'Partial' in row['status'] else '⏳'
        table_data.append([
            row['decision_date'][:7] if isinstance(row['decision_date'], str) else str(row['decision_date'])[:7],
            row['decision_title'][:30] + '...' if len(row['decision_title']) > 30 else row['decision_title'],
            row['confidence_level'][:10] if pd.notna(row['confidence_level']) else 'N/A',
            status_icon
        ])

    table = ax4.table(cellText=table_data,
                      colLabels=['Date', 'Decision', 'Confidence', 'Status'],
                      loc='center',
                      cellLoc='left',
                      colColours=[colors['light']]*4)
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.2, 1.8)
    ax4.set_title('Recent Strategic Decisions', fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig('outputs/04_decision_analytics.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✅ Figure 4: Decision Analytics created")

# =============================================================================
# FIGURE 5: METRIC OWNERSHIP & HIERARCHY
# =============================================================================

def create_metric_ownership_dashboard():
    fig5 = plt.figure(figsize=(16, 12))
    fig5.suptitle('TechVantage Inc. - Metric Ownership & KPI Hierarchy', 
                  fontsize=16, fontweight='bold', y=0.98)

    gs5 = GridSpec(2, 2, figure=fig5, hspace=0.35, wspace=0.3)

    # 5.1 Metrics by Owner
    ax1 = fig5.add_subplot(gs5[0, 0])
    owner_counts = metric_definitions['owner'].value_counts()
    ax1.barh(owner_counts.index, owner_counts.values, color=colors['primary'])
    for i, v in enumerate(owner_counts.values):
        ax1.text(v + 0.1, i, str(v), va='center')
    ax1.set_xlabel('Number of Metrics')
    ax1.set_title('Metrics by Owner', fontweight='bold')

    # 5.2 Metrics by Business Unit
    ax2 = fig5.add_subplot(gs5[0, 1])
    bu_counts = metric_definitions['business_unit'].value_counts()
    colors_bu = [category_colors.get(bu, colors['primary']) for bu in bu_counts.index]
    wedges, texts, autotexts = ax2.pie(bu_counts.values, labels=bu_counts.index,
                                        autopct='%1.0f%%', colors=colors_bu,
                                        startangle=90)
    ax2.set_title('Metrics by Business Unit', fontweight='bold')

    # 5.3 Data Sources Distribution
    ax3 = fig5.add_subplot(gs5[1, 0])
    source_counts = metric_definitions['data_source'].value_counts()
    ax3.barh(source_counts.index, source_counts.values, color=colors['info'])
    for i, v in enumerate(source_counts.values):
        ax3.text(v + 0.1, i, str(v), va='center')
    ax3.set_xlabel('Number of Metrics')
    ax3.set_title('Metrics by Data Source', fontweight='bold')

    # 5.4 Criticality & Refresh Frequency Matrix
    ax4 = fig5.add_subplot(gs5[1, 1])
    matrix_data = metric_definitions.groupby(['criticality', 'refresh_frequency']).size().unstack(fill_value=0)
    crit_order = ['Critical', 'High', 'Medium']
    freq_order = ['Real-time', 'Daily', 'Weekly', 'Bi-weekly', 'Monthly', 'Quarterly']
    matrix_data = matrix_data.reindex(index=crit_order, columns=[f for f in freq_order if f in matrix_data.columns], fill_value=0)

    im = ax4.imshow(matrix_data.values, cmap='Blues', aspect='auto')
    ax4.set_xticks(range(len(matrix_data.columns)))
    ax4.set_yticks(range(len(matrix_data.index)))
    ax4.set_xticklabels(matrix_data.columns, rotation=45, ha='right')
    ax4.set_yticklabels(matrix_data.index)

    for i in range(len(matrix_data.index)):
        for j in range(len(matrix_data.columns)):
            val = matrix_data.iloc[i, j]
            color = 'white' if val > matrix_data.values.max()/2 else 'black'
            ax4.text(j, i, str(val), ha='center', va='center', color=color, fontweight='bold')

    ax4.set_title('Criticality vs Refresh Frequency', fontweight='bold')
    plt.colorbar(im, ax=ax4, label='Count')

    plt.tight_layout()
    plt.savefig('outputs/05_metric_ownership.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✅ Figure 5: Metric Ownership & Hierarchy created")

# =============================================================================
# FIGURE 6: FINANCIAL PERFORMANCE DEEP DIVE
# =============================================================================

def create_financial_dashboard():
    fig6 = plt.figure(figsize=(16, 10))
    fig6.suptitle('TechVantage Inc. - Financial Performance Analysis', 
                  fontsize=16, fontweight='bold', y=0.98)

    gs6 = GridSpec(2, 3, figure=fig6, hspace=0.35, wspace=0.3)

    # 6.1 Revenue Components
    ax1 = fig6.add_subplot(gs6[0, 0])
    rev_metrics = kpi_actuals[kpi_actuals['metric_id'].isin(['REV001', 'REV002'])]
    rev_pivot = rev_metrics.pivot(index='period', columns='metric_id', values='actual_value')
    rev_pivot['Non-Recurring'] = rev_pivot['REV001'] - rev_pivot['REV002']

    ax1.bar(rev_pivot.index, rev_pivot['REV002'], label='ARR', color=colors['revenue'])
    ax1.bar(rev_pivot.index, rev_pivot['Non-Recurring'], bottom=rev_pivot['REV002'], 
            label='Non-Recurring', color=colors['light'], edgecolor=colors['revenue'])
    ax1.set_ylabel('Revenue ($M)')
    ax1.set_title('Revenue Composition', fontweight='bold')
    ax1.legend()
    ax1.tick_params(axis='x', rotation=45)

    # 6.2 Revenue Growth YoY
    ax2 = fig6.add_subplot(gs6[0, 1])
    growth_data = kpi_actuals[kpi_actuals['metric_id'] == 'REV003'].sort_values('period')
    colors_growth = [colors['success'] if g >= 15 else colors['warning'] if g >= 10 else colors['danger'] 
                     for g in growth_data['actual_value']]
    bars = ax2.bar(growth_data['period'], growth_data['actual_value'], color=colors_growth)
    ax2.axhline(y=15, color=colors['success'], linestyle='--', label='15% Target')
    ax2.axhline(y=10, color=colors['warning'], linestyle='--', label='10% Baseline')
    for bar, val in zip(bars, growth_data['actual_value']):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, f'{val:.1f}%', 
                 ha='center', va='bottom', fontsize=9)
    ax2.set_ylabel('Growth Rate %')
    ax2.set_title('Revenue Growth YoY', fontweight='bold')
    ax2.legend(fontsize=8)
    ax2.tick_params(axis='x', rotation=45)

    # 6.3 Margin Trends
    ax3 = fig6.add_subplot(gs6[0, 2])
    margin_metrics = ['PROF001', 'PROF002', 'PROF003']
    margin_names = {'PROF001': 'Gross', 'PROF002': 'Operating', 'PROF003': 'EBITDA'}
    for metric in margin_metrics:
        data = kpi_actuals[kpi_actuals['metric_id'] == metric].sort_values('period')
        ax3.plot(data['period'], data['actual_value'], 'o-', label=margin_names[metric], linewidth=2)
    ax3.set_ylabel('Margin %')
    ax3.set_title('Margin Trends', fontweight='bold')
    ax3.legend()
    ax3.tick_params(axis='x', rotation=45)

    # 6.4 LTV/CAC Analysis
    ax4 = fig6.add_subplot(gs6[1, 0])
    cac_data = kpi_actuals[kpi_actuals['metric_id'] == 'CUST001'].sort_values('period')
    ltv_data = kpi_actuals[kpi_actuals['metric_id'] == 'CUST002'].sort_values('period')
    ltv_cac_ratio = ltv_data['actual_value'].values / cac_data['actual_value'].values

    ax4.bar(cac_data['period'], ltv_cac_ratio, color=colors['customer'])
    ax4.axhline(y=12, color=colors['success'], linestyle='--', label='12x Target')
    for i, (period, ratio) in enumerate(zip(cac_data['period'], ltv_cac_ratio)):
        ax4.text(i, ratio + 0.2, f'{ratio:.1f}x', ha='center', fontsize=9)
    ax4.set_ylabel('LTV/CAC Ratio')
    ax4.set_title('LTV/CAC Ratio Trend', fontweight='bold')
    ax4.legend()
    ax4.tick_params(axis='x', rotation=45)

    # 6.5 Working Capital & DSO
    ax5 = fig6.add_subplot(gs6[1, 1])
    dso_data = kpi_actuals[kpi_actuals['metric_id'] == 'FIN001'].sort_values('period')
    wc_data = kpi_actuals[kpi_actuals['metric_id'] == 'FIN002'].sort_values('period')

    ax5_twin = ax5.twinx()
    ax5.bar(dso_data['period'], dso_data['actual_value'], alpha=0.7, color=colors['finance'], label='DSO (Days)')
    ax5_twin.plot(wc_data['period'], wc_data['actual_value'], 'o-', color=colors['danger'], 
                  linewidth=2, label='Working Capital Ratio')
    ax5.set_ylabel('Days Sales Outstanding', color=colors['finance'])
    ax5_twin.set_ylabel('Working Capital Ratio', color=colors['danger'])
    ax5.set_title('Financial Health Indicators', fontweight='bold')
    ax5.legend(loc='upper left', fontsize=8)
    ax5_twin.legend(loc='upper right', fontsize=8)
    ax5.tick_params(axis='x', rotation=45)

    # 6.6 Financial KPI Scorecard
    ax6 = fig6.add_subplot(gs6[1, 2])
    ax6.axis('off')
    fin_kpis = kpi_actuals[
        (kpi_actuals['metric_id'].isin(['REV001', 'REV002', 'REV003', 'PROF003', 'FIN001', 'FIN002'])) &
        (kpi_actuals['period'] == 'Q4 2024')
    ].merge(metric_definitions[['metric_id', 'metric_name', 'target_q4_2024', 'unit_of_measure']], on='metric_id')

    table_data = []
    for _, row in fin_kpis.iterrows():
        variance = (row['actual_value'] - row['target_q4_2024']) / row['target_q4_2024'] * 100
        status = '✅' if abs(variance) <= 5 else ('🔶' if variance > -15 else '❌')
        table_data.append([
            row['metric_name'][:25],
            f"{row['actual_value']:.1f}",
            f"{row['target_q4_2024']:.1f}",
            f"{variance:+.1f}%",
            status
        ])

    table = ax6.table(cellText=table_data,
                      colLabels=['Metric', 'Actual', 'Target', 'Var %', ''],
                      loc='center',
                      cellLoc='center',
                      colColours=[colors['light']]*5)
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.2, 1.5)
    ax6.set_title('Financial KPI Scorecard', fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig('outputs/06_financial_performance.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✅ Figure 6: Financial Performance Analysis created")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    import os
    os.makedirs('outputs', exist_ok=True)
    
    create_executive_dashboard()
    create_okr_dashboard()
    create_data_governance_dashboard()
    create_decision_analytics_dashboard()
    create_metric_ownership_dashboard()
    create_financial_dashboard()
    
    # Print Summary
    print("\n" + "="*60)
    print("EXECUTIVE SUMMARY - TECHVANTAGE INC. Q4 2024")
    print("="*60)
    
    q4_data = kpi_actuals[kpi_actuals['period'] == 'Q4 2024']
    q4_merged = q4_data.merge(metric_definitions[['metric_id', 'metric_name', 'target_q4_2024', 'criticality']], on='metric_id')
    
    total_metrics = len(q4_merged)
    on_track = len(q4_merged[q4_merged['actual_value'] >= q4_merged['target_q4_2024'] * 0.95])
    at_risk = len(q4_merged[(q4_merged['actual_value'] >= q4_merged['target_q4_2024'] * 0.85) & 
                             (q4_merged['actual_value'] < q4_merged['target_q4_2024'] * 0.95)])
    off_track = total_metrics - on_track - at_risk
    
    print(f"\n📊 KPI PERFORMANCE SUMMARY")
    print(f"   Total KPIs Tracked: {total_metrics}")
    print(f"   ✅ On Track: {on_track} ({on_track/total_metrics*100:.0f}%)")
    print(f"   🟡 At Risk: {at_risk} ({at_risk/total_metrics*100:.0f}%)")
    print(f"   🔴 Off Track: {off_track} ({off_track/total_metrics*100:.0f}%)")
    
    okr_achieved = len(okr_data[okr_data['status'] == 'Achieved'])
    okr_total = len(okr_data)
    avg_progress = okr_data['progress_pct'].mean()
    
    print(f"\n🎯 OKR PERFORMANCE SUMMARY")
    print(f"   Total Key Results: {okr_total}")
    print(f"   ✅ Achieved: {okr_achieved} ({okr_achieved/okr_total*100:.0f}%)")
    print(f"   📈 Average Progress: {avg_progress:.1f}%")
    
    open_issues = len(data_quality_issues[data_quality_issues['status'] == 'Open'])
    resolved_issues = len(data_quality_issues[data_quality_issues['status'] == 'Resolved'])
    total_issues = len(data_quality_issues)
    
    print(f"\n🔍 DATA QUALITY SUMMARY")
    print(f"   Total Issues Detected: {total_issues}")
    print(f"   ✅ Resolved: {resolved_issues} ({resolved_issues/total_issues*100:.0f}%)")
    print(f"   ⚠️  Open: {open_issues} ({open_issues/total_issues*100:.0f}%)")
    
    completed_decisions = len(decision_log[decision_log['status'].str.contains('Completed')])
    exceeded_decisions = len(decision_log[decision_log['status'].str.contains('Exceeded')])
    
    print(f"\n📋 DECISION ANALYTICS")
    print(f"   Strategic Decisions Made: {len(decision_log)}")
    print(f"   ✅ Completed: {completed_decisions}")
    print(f"   🌟 Exceeded Expectations: {exceeded_decisions}")
    
    print("\n" + "="*60)
    print("All visualizations saved to outputs/")
    print("="*60)
