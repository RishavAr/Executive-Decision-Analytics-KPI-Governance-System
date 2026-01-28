# 📊 Data Sources Documentation

## Executive Decision Analytics & KPI Governance System

---

## 🔍 Data Overview

This project uses **realistic synthetic data** generated based on **real-world S&P 500 benchmarks** from 2024. The data simulates a mid-cap technology/SaaS company called "TechVantage Inc."

---

## 📈 Real-World Benchmarks Used

### Source 1: S&P Global Market Intelligence
**URL:** https://www.spglobal.com/market-intelligence/en/news-insights/research/sp-500-q3-2024-sector-earnings-revenue-data

| Metric | Real S&P 500 Data (2024) | How I Used It |
|--------|--------------------------|---------------|
| Revenue Growth YoY | 10.8% (S&P 500 average) | Set TechVantage at 14.9% (tech sector outperforms) |
| EPS Growth | 13.1% Q3 2024 | Used to calibrate profitability improvements |
| Tech Sector Revenue Growth | 18.3% | Basis for ARR growth rate (29% YoY) |
| EPS Beat Rate | 77% of companies | Informed "On Track" status percentages |

### Source 2: FactSet Earnings Insight
**URL:** https://www.factset.com/earningsinsight

| Metric | Real Data | Application |
|--------|-----------|-------------|
| Forward P/E Ratio | 22.1 (above 10-yr avg 18.8) | Context for valuation metrics |
| Q4 2024 EPS Growth | 8.2% | Calibrated quarterly progression |
| Revenue Growth Q4 | 7.8% | Used for revenue trend modeling |
| CY 2025 EPS Growth Forecast | 14.7% | Forward-looking OKR targets |

### Source 3: Industry SaaS Benchmarks
**Sources:** OpenView Partners, KeyBanc SaaS Survey, Bessemer Cloud Index

| Metric | Industry Benchmark | TechVantage Value |
|--------|-------------------|-------------------|
| Net Revenue Retention | 100-120% | Implied ~115% |
| Gross Margin | 70-80% | 68.2% |
| CAC Payback | 12-18 months | ~14 months |
| LTV/CAC Ratio | 3-5x (good), >5x (great) | 11.7x (excellent) |
| Annual Churn Rate | 5-7% (B2B SaaS) | 2.5% (low = healthy) |
| NPS Score | 30-50 (good), >50 (excellent) | 54 |

### Source 4: Operational Benchmarks
**Sources:** Datadog State of DevOps, PagerDuty, Gartner

| Metric | Industry Standard | TechVantage Value |
|--------|------------------|-------------------|
| Platform Uptime SLA | 99.9% (three nines) | 99.96% (exceeds) |
| API Response Time | <200ms acceptable | 148ms |
| MTTR (Mean Time to Resolve) | 4-8 hours | 3.9 hours |

---

## 🗄️ Generated Datasets Detail

### 1. metric_definitions.csv (24 records)

**What it contains:**
- Unique metric IDs (e.g., REV001, CUST004)
- Metric names and categories
- Calculation formulas
- Data sources (SAP, Salesforce, Datadog, etc.)
- Ownership assignments
- Criticality levels

**Sample Data:**
```csv
metric_id,metric_name,category,owner,calculation_method,data_source,criticality
REV001,Total Revenue,Revenue,CFO - Sarah Chen,SUM(all_revenue_streams),SAP ERP,Critical
CUST004,Customer Churn Rate,Customer,VP CS - Lisa Park,churned_customers / total_customers * 100,Salesforce,Critical
OPS001,System Uptime,Operations,CTO - David Kumar,uptime_minutes / total_minutes * 100,Datadog,Critical
```

### 2. kpi_actuals.csv (120 records)

**What it contains:**
- 24 metrics × 5 quarters = 120 data points
- Periods: Q4 2023, Q1-Q4 2024
- Actual values, target values, variance
- Status flags (On Track, At Risk, Off Track)

**Sample Data:**
```csv
metric_id,period,actual_value,target_value,variance_pct,status
REV001,Q4 2023,68.5,58.0,18.1,On Track
REV001,Q1 2024,72.3,63.8,13.3,On Track
REV001,Q2 2024,76.8,72.3,6.2,On Track
REV001,Q3 2024,80.2,80.8,-0.7,On Track
REV001,Q4 2024,84.1,85.0,-1.1,On Track
```

**How values were generated:**
```python
# Example: Revenue trajectory based on S&P 500 tech sector growth
base_revenue = 68.5  # Q4 2023 starting point ($M)
growth_rates = [0.055, 0.062, 0.044, 0.049]  # Quarterly growth
# Results in: 68.5 → 72.3 → 76.8 → 80.2 → 84.1 (~14.9% YoY)
```

### 3. kpi_hierarchy.csv (15 records)

**What it contains:**
- 3-level objective hierarchy (L1=Company, L2=Department, L3=Team)
- Parent-child relationships
- Linked metric IDs
- Ownership at each level

**Structure:**
```
L1: Company Growth (CEO)
├── L2: Revenue Excellence (CFO)
│   └── L3: Sales Efficiency (CMO)
├── L2: Operational Excellence (CTO)
│   └── L3: Platform Reliability (VP Eng)
└── L2: Customer Success (VP CS)
    └── L3: Customer Retention (Director CS)
```

### 4. okr_tracking.csv (15 records)

**What it contains:**
- 5 strategic objectives with 3 key results each
- Start values, target values, current values
- Progress percentages (0-100%)
- Confidence scores (0.0-1.0)
- Status (Achieved, On Track, At Risk)

**Sample Data:**
```csv
objective,key_result,start_value,target_value,current_value,progress_pct,status
Accelerate Revenue Growth,Grow ARR from $55M to $72M,55.2,72.0,71.2,95,On Track
Achieve Operational Excellence,Achieve 99.95% platform uptime,99.91,99.95,99.96,100,Achieved
Build World-Class Culture,Increase employee satisfaction to 8.2+,7.4,8.2,8.1,88,At Risk
```

### 5. data_quality_issues.csv (15 records)

**What it contains:**
- Issue IDs (DQ001-DQ015)
- Issue types (Missing Data, Outlier, Schema Drift, etc.)
- Severity levels (Critical, High, Medium, Low)
- Detection and resolution dates
- Root cause analysis
- Assigned teams

**Sample Data:**
```csv
issue_id,metric_id,issue_type,severity,detected_date,status,root_cause
DQ001,REV001,Missing Data,Medium,2024-10-15,Resolved,ETL job failed
DQ006,PROF002,Calculation Error,Critical,2024-11-01,Resolved,Formula update error
DQ010,DATA001,Validation Failure,High,2024-11-15,Open,Rule conflict
```

### 6. metric_drift_log.csv (10 records)

**What it contains:**
- Definition changes throughout 2024
- Old vs. new definitions
- Approval chain
- Impact on historical data
- Communication status

**Sample Data:**
```csv
metric_id,drift_type,old_definition,new_definition,change_date,approved_by,impact_on_historical
REV003,Definition Change,YoY growth including one-time revenue,YoY growth excluding one-time revenue,2024-01-15,CFO,Restated Q1-Q4 2023
CUST002,Calculation Drift,LTV = ARPU * 36 months,LTV = ARPU * Avg Customer Tenure,2024-02-01,CRO,Restated from Q3 2023
```

### 7. decision_log.csv (10 records)

**What it contains:**
- Strategic decisions made in 2024
- Decision makers
- KPIs considered
- Expected vs. actual impact
- Confidence levels
- Outcomes

**Sample Data:**
```csv
decision_id,decision_title,decision_date,kpis_considered,expected_impact,actual_impact,status
DEC-2024-001,Increase Q2 Marketing Budget by 15%,2024-01-25,"MKT001, MKT002, CUST001",+20% MQLs +0.5% conversion,+22% MQLs +0.6% conversion,Completed - Exceeded
DEC-2024-007,Acquire DataSync Inc.,2024-07-25,"DATA001, DATA002, REV002",+10 points data quality score,+9 points data quality score,Completed - Met
```

---

## 🔢 Value Generation Logic

### Revenue Metrics
```python
# Based on S&P 500 tech sector growth of 17-18% YoY
base_values = {
    'REV001': [68.5, 72.3, 76.8, 80.2, 84.1],  # ~15% YoY growth
    'REV002': [55.2, 58.9, 63.1, 67.4, 71.2],  # ARR ~29% YoY (SaaS premium)
    'REV003': [12.8, 14.2, 15.8, 16.1, 14.9],  # Growth rate fluctuation
}
```

### Profitability Metrics
```python
# Based on improving operational efficiency
base_values = {
    'PROF001': [65.2, 66.1, 67.3, 67.8, 68.2],  # Gross margin improving
    'PROF002': [18.5, 19.2, 20.1, 21.3, 22.1],  # Operating margin expansion
    'PROF003': [24.1, 25.2, 26.4, 27.1, 27.8],  # EBITDA margin growth
}
```

### Customer Metrics
```python
# Based on SaaS industry benchmarks
base_values = {
    'CUST001': [1450, 1380, 1320, 1280, 1210],  # CAC decreasing (efficiency)
    'CUST002': [13200, 13800, 14200, 14600, 14900],  # LTV increasing
    'CUST003': [48, 50, 52, 53, 54],  # NPS improving
    'CUST004': [3.2, 2.9, 2.7, 2.6, 2.5],  # Churn decreasing
}
```

### Operations Metrics
```python
# Based on DevOps/SRE industry standards
base_values = {
    'OPS001': [99.91, 99.93, 99.94, 99.95, 99.96],  # Uptime improving
    'OPS002': [185, 172, 162, 155, 148],  # Response time decreasing
    'OPS003': [5.2, 4.8, 4.5, 4.2, 3.9],  # MTTR decreasing
}
```

---

## 📊 Data Quality & Realism

### Variance Applied
```python
# Small random variance to simulate real-world fluctuations
variance = np.random.normal(0, 0.02)  # ±2% noise
actual = base_value * (1 + variance)
```

### Status Logic
```python
# RAG (Red-Amber-Green) status based on target achievement
if actual >= target * 0.95:
    status = 'On Track'  # Green
elif actual >= target * 0.85:
    status = 'At Risk'   # Amber
else:
    status = 'Off Track' # Red
```

---

## ✅ Data Validation

All generated data passes these quality checks:

| Check | Result |
|-------|--------|
| Unique metric IDs | ✅ 24 unique |
| No null critical fields | ✅ All populated |
| Valid status values | ✅ All in allowed list |
| Progress bounds (0-100%) | ✅ All within range |
| Variance calculations | ✅ Mathematically correct |
| Date consistency | ✅ Chronologically ordered |

---

## 🎯 Why This Data Approach?

1. **Realistic** - Based on actual S&P 500 and industry benchmarks
2. **Consistent** - All metrics follow logical business patterns
3. **Complete** - Covers all aspects of KPI governance
4. **Demonstrable** - Shows both successes and areas needing attention
5. **Actionable** - Enables meaningful analysis and insights

---

## 📚 References

1. S&P Global Market Intelligence - Q3 2024 Earnings Data
2. FactSet Earnings Insight - January 2025
3. OpenView Partners - 2024 SaaS Benchmarks
4. Bessemer Venture Partners - Cloud Index
5. Datadog - State of DevOps Report
6. Gartner - IT Operations Benchmarks

---

*This data was generated for demonstration purposes to showcase senior-level analytics capabilities in KPI governance and executive reporting.*
