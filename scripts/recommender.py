import pandas as pd
import numpy as np
nav = pd.read_csv("Data/Processed/02_nav_history_cleaned.csv")
fund_master = pd.read_csv("Data/Processed/01_fund_master_cleaned.csv")

nav = nav.sort_values(['amfi_code', 'date'])
nav['daily_return'] = (
    nav.groupby('amfi_code')['nav']
    .pct_change()
)


sharpe_table = (
    nav.groupby('amfi_code')['daily_return']
    .agg(['mean', 'std'])
    .reset_index()
)

sharpe_table['sharpe_ratio'] = (
    sharpe_table['mean']
    / sharpe_table['std']
) * np.sqrt(252)

sharpe_table = sharpe_table.merge(
    fund_master[
        ['amfi_code',
         'scheme_name',
         'risk_category']
    ],
    on='amfi_code',
    how='left'
)

def recommend_funds(risk_appetite):

    risk_map = {
        "Low": ["Low"],
        "Moderate": ["Moderate", "Moderately High"],
        "High": ["High", "Very High"]
    }

    return (
        sharpe_table[
            sharpe_table['risk_category']
            .isin(risk_map[risk_appetite])
        ]
        .sort_values(
            'sharpe_ratio',
            ascending=False
        )
        [
            ['scheme_name',
             'risk_category',
             'sharpe_ratio']
        ]
        .head(3)
    )
print("\nLow Risk Funds")
print(recommend_funds("Low"))

print("\nModerate Risk Funds")
print(recommend_funds("Moderate"))

print("\nHigh Risk Funds")
print(recommend_funds("High"))