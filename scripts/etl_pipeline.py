import pandas as pd
df1 = pd.read_csv("Data/Raw/01_fund_master.csv")
df1.head()
df1.shape
df1.columns
df1.dtypes
df1.isnull().sum()
df1.duplicated().sum()
df1['fund_house'].unique()
df1['sub_category'].unique()
df1['category'].unique()
df1['risk_category'].unique()
df1['amfi_code'].head(10)
df1['amfi_code'].nunique()
df1[["amfi_code", "scheme_name"]].head(10)
df1["amfi_code"].duplicated().sum()
df2 = pd.read_csv("Data/Raw/02_nav_history.csv")
df2.head()
df2.dtypes
df2.shape
df2.isnull().sum()
set(df1['amfi_code'])-set(df2['amfi_code'])
df3 = pd.read_csv("Data/Raw/03_aum_by_fund_house.csv")
df3.head()
df3.shape
df3.dtypes
df3.duplicated().sum()
df3.isnull().sum()
df4 = pd.read_csv("Data/Raw/04_monthly_sip_inflows.csv")
df4.head()
df4.shape
df4.dtypes
df4.isnull().sum()
df4.duplicated().sum()
df5 = pd.read_csv("Data/Raw/05_category_inflows.csv")
df5.head()
df5.shape
df5.dtypes
df5.isnull().sum()
df5.duplicated().sum()
df6 = pd.read_csv("Data/Raw/06_industry_folio_count.csv")
df6.head()
df6.shape
df6.dtypes
df6.isnull().sum()
df6.duplicated().sum()
df7 = pd.read_csv("Data/Raw/07_scheme_performance.csv")
df7.head()
df7.shape
df7.dtypes
df7.isnull().sum()
df7.duplicated().sum()
df8 = pd.read_csv("Data/Raw/08_investor_transactions.csv")
df8.head()
df8.shape
df8.dtypes
df8.isnull().sum()
df8.duplicated().sum()
df9 = pd.read_csv("Data/Raw/09_portfolio_holdings.csv")
df9.head()
df9.shape
df9.dtypes
df9.isnull().sum()
df9.duplicated().sum()
df10 = pd.read_csv("Data/Raw/10_benchmark_indices.csv")
df10.head()
df10.shape
df10.dtypes
df10.isnull().sum()
df10.duplicated().sum()



# OBSERVATIONS---

# -- Fund Master contains 40 unique amfi schemes.
# -- Categories Present - Equity and Dept .
# -- 12 different Sub Categories Found .
# -- Risk Categories - 5 found(Low , Moderate , High , Moderately High , Very High ) .
# -- All AMFI codes from fund_master exist in nav_history - no code is missing .
# -- Live NAV data successfully fetched from mfapi and saved as live_nav_125497.CSV.
# -- NAV history contains date and NAV values for each scheme.
# -- API and master data mismatch observed for AMFI code 125497:
#    - fund_master.csv → HDFC Top 100 Fund - Direct Plan - Growth
#    - mfapi response → SBI Small Cap Fund - Direct Plan - Growth