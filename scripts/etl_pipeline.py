"""
ETL Pipeline Validation Script

This script loads all raw datasets used in the
Mutual Fund Analytics Platform and performs
basic validation checks before data cleaning
and transformation.
"""

import pandas as pd



fund_master = pd.read_csv("Data/Raw/01_fund_master.csv")
nav_history = pd.read_csv("Data/Raw/02_nav_history.csv")
aum_data = pd.read_csv("Data/Raw/03_aum_by_fund_house.csv")
sip_inflows = pd.read_csv("Data/Raw/04_monthly_sip_inflows.csv")
category_inflows = pd.read_csv("Data/Raw/05_category_inflows.csv")
folio_count = pd.read_csv("Data/Raw/06_industry_folio_count.csv")
scheme_performance = pd.read_csv("Data/Raw/07_scheme_performance.csv")
investor_transactions = pd.read_csv("Data/Raw/08_investor_transactions.csv")
portfolio_holdings = pd.read_csv("Data/Raw/09_portfolio_holdings.csv")
benchmark_indices = pd.read_csv("Data/Raw/10_benchmark_indices.csv")

# Validation Checks

total_schemes = fund_master["amfi_code"].nunique()

missing_amfi_codes = (
    set(fund_master["amfi_code"])
    - set(nav_history["amfi_code"])
)

# Project Observations

print("\nETL Validation Summary")
print("-" * 40)

print(f"Total Mutual Fund Schemes : {total_schemes}")
print(f"Missing AMFI Codes in NAV Dataset : {len(missing_amfi_codes)}")

if len(missing_amfi_codes) == 0:
    print("All AMFI codes are available in NAV history dataset.")

print("\nDataset Overview")
print("-" * 40)

print(f"Fund Master Records : {len(fund_master)}")
print(f"NAV Records : {len(nav_history)}")
print(f"AUM Records : {len(aum_data)}")
print(f"SIP Inflow Records : {len(sip_inflows)}")
print(f"Category Inflow Records : {len(category_inflows)}")
print(f"Folio Count Records : {len(folio_count)}")
print(f"Scheme Performance Records : {len(scheme_performance)}")
print(f"Investor Transaction Records : {len(investor_transactions)}")
print(f"Portfolio Holding Records : {len(portfolio_holdings)}")
print(f"Benchmark Records : {len(benchmark_indices)}")

print("\nETL validation completed successfully.")

if __name__ == "__main__":
    print("\nPipeline Ready")