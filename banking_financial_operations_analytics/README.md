# Banking & Financial Operations Analytics

## Project overview
This project analyses banking transaction data to understand transaction volume, value, success/failure rates, payment-method performance, regional trends, and operational issues.

## Business problem
The bank is experiencing failed transactions, processing delays, and customer complaints. The goal is to turn transaction-level data into actionable operational insights.

## Business questions
1. How many transactions were processed?
2. What was the total transaction value?
3. What were the success, failure, and pending rates?
4. Which payment methods had the highest failure rates?
5. Which regions generated the highest transaction volume and value?
6. How did transaction volume and value change over time?
7. Which transaction types need operational improvement?

## Tools
- Excel: initial inspection and validation
- MySQL: data storage and business analysis
- Python (Pandas, NumPy, Matplotlib): cleaning and exploratory analysis
- Power BI: interactive reporting
- GitHub: project documentation and version control

## Repository structure
```text
banking-financial-operations-analytics/
├── data/
│   ├── raw/                 # Original dataset (do not overwrite)
│   └── processed/           # Cleaned dataset
├── excel/                   # Excel checks and summaries
├── sql/
│   ├── 01_create_tables.sql
│   └── 02_business_analysis.sql
├── python/
│   └── 01_data_inspection.py
├── powerbi/                 # .pbix file and dashboard screenshots
├── reports/                 # Findings and recommendations
├── README.md
├── requirements.txt
└── .gitignore
```

## Dataset
Dataset not yet added. Add the downloaded CSV to `data/raw/` and document its source, license, and exact filename here before analysis.

### Expected fields
`Transaction_ID`, `Customer_ID`, `Transaction_Date`, `Transaction_Amount`, `Transaction_Type`, `Payment_Method`, `Transaction_Status`, `Branch`, `Region`

Actual dataset column names may differ. Update the scripts after confirming the downloaded file's schema.

## Key metrics
- Total transactions
- Total transaction amount
- Successful transactions
- Failed transactions
- Pending transactions
- Success rate = successful transactions / total transactions × 100
- Failure rate = failed transactions / total transactions × 100
- Pending rate = pending transactions / total transactions × 100

## Project workflow
1. Inspect the raw dataset and record its source.
2. Validate missing values, duplicates, data types, and invalid values.
3. Clean the data and save a separate processed copy.
4. Load the data into MySQL.
5. Answer business questions with SQL.
6. Perform exploratory analysis in Python.
7. Build a Power BI dashboard.
8. Write findings and practical recommendations.

## Current status
- [ ] Dataset selected and source documented
- [ ] Data quality assessment completed
- [ ] Cleaned dataset prepared
- [ ] SQL analysis completed
- [ ] Python EDA completed
- [ ] Power BI dashboard completed
- [ ] Business recommendations documented

## Important
Use a public, appropriately licensed dataset. Do not upload real customer data, account numbers, personal information, or confidential employer data to GitHub.
