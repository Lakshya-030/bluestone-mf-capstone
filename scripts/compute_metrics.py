"""
Compute financial metrics such as VaR, CVaR, Sharpe Ratio,
and HHI for mutual fund analysis.
"""



import pandas as pd
import numpy as np

def calculate_var_cvar(nav):

    nav['daily_return'] = (nav.groupby('amfi_code')['nav'].pct_change())

    var_report = (
        nav.groupby('amfi_code')['daily_return']
        .quantile(0.05)
        .reset_index()
    )

    return var_report

def calculate_sharpe(nav):

    sharpe = (
        nav.groupby('amfi_code')['daily_return']
        .agg(['mean', 'std'])
        .reset_index()
    )

    sharpe['sharpe_ratio'] = (
        sharpe['mean']
        / sharpe['std']
    ) * np.sqrt(252)

    return sharpe


def calculate_hhi(holdings):

    sector_weights = (
        holdings.groupby(
            ['amfi_code', 'sector']
        )['weight_pct']
        .sum()
        .reset_index()
    )

    hhi = (
        sector_weights.groupby('amfi_code')['weight_pct']
        .apply(lambda x: ((x/100)**2).sum())
        .reset_index(name='HHI')
    )

    return hhi

if __name__ == "__main__":
    print("Metrics module is ready")