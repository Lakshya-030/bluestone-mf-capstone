# Bluestock MF Capstone Project

## Project Overview

This project focuses on building an end-to-end Mutual Fund Analytics solution using Python, SQLite, SQL, and Power BI. The workflow covers data ingestion, data cleaning, exploratory data analysis, performance analytics, advanced analytics, and dashboard development.

The objective of the project is to analyze mutual fund industry trends, fund performance, investor behavior, SIP growth patterns, benchmark performance, and NAV movements. The final output is an interactive Power BI dashboard that provides insights for investors and fund managers.

## Tech Stack

* Python
* Pandas
* NumPy
* SQLite
* SQL
* Power BI
* Git & GitHub

## Data Sources

The analysis was performed using the following datasets:

1. Fund Master Data
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

In addition to the historical datasets, live NAV data was collected using MFAPI and integrated into the analysis pipeline.

## Database

All processed datasets were stored in an SQLite database:

* bluestock_mf.db

## Project Structure

```text
BLUESTONE_MF_CAPSTONE/
│
├── dashboard/
│   └── bluestock_mf.pbix
│
├── Data/
│   ├── Raw/
│   ├── Processed/
│   └── db/
│
├── Notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_EDA_Analysis.ipynb
│   ├── 04_Performance_analytics.ipynb
│   └── 05_Advanced_Analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── compute_metrics.py
│   ├── live_nav_fetch.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── reports/
├── screenshots/
└── README.md
```

## ETL Pipeline

### Data Extraction

The project begins with loading 10 mutual fund datasets from CSV files. Historical NAV information, fund performance data, SIP inflows, portfolio holdings, benchmark indices, and investor transaction datasets were collected and organized in the raw data layer. Live NAV data was also fetched through MFAPI.

### Data Transformation

The raw datasets were cleaned and standardized before analysis. Missing values, inconsistent formats, and duplicate records were reviewed and handled wherever required. Column names and data types were standardized to ensure consistency across datasets.

Separate processed datasets were generated for downstream analysis and reporting.

### Data Loading

The cleaned datasets were loaded into the SQLite database (bluestock_mf.db). SQL schema definitions and analytical queries were created to support reporting and dashboard requirements.

### Analytics Layer

The processed data was used for:

* Exploratory Data Analysis (EDA)
* Fund Performance Analysis
* Investor Analytics
* SIP Trend Analysis
* Portfolio Analysis
* Risk and Drawdown Analysis

## Dashboard Overview

The Power BI dashboard consists of five analytical pages:

### 1. Industry Overview

Provides a high-level view of the mutual fund industry, including fund distribution, AUM trends, and category-level insights.

### 2. Fund Performance

Analyzes scheme returns, benchmark comparisons, alpha-beta metrics, and overall fund performance.

### 3. Investor Analytics

Focuses on investor participation, transaction activity, and behavioral trends across mutual fund schemes.

### 4. SIP & Market Trends

Tracks SIP inflows, category inflows, market movements, and long-term investment trends.

### 5. Fund NAV Details

Provides drill-through from fund table 

## Key Outputs

The project generated several analytical outputs, including:

* Alpha-Beta Analysis
* Fund Scorecards
* Cohort Analysis
* Drawdown Reports
* Tracking Error Analysis
* Sector Concentration Reports
* SIP Continuity Analysis
* Value at Risk (VaR) and Conditional VaR Reports

## How to Run the Project

1. Clone the repository.
2. Install the required Python packages.
3. Execute the ETL pipeline scripts.
4. Verify that the processed CSV datasets are generated successfully.
5. Open the Power BI dashboard file.
6. Explore the analytical dashboards and reports.

## Deliverables

* SQLite Database
* SQL Scripts
* Python ETL Scripts
* Power BI Dashboard
* Final Project Report
* Presentation Slides
* Project Documentation

## Master Execution Script

The project workflow can be executed using the master script:

```bash
python scripts/run_pipeline.py

## Author

Lakshya Arora
