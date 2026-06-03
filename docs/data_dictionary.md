# Data Dictionary

## dim_fund

 Column | Description |

 amfi_code | Unique code assigned to each mutual fund scheme |
 fund_house | Name of the fund house managing the scheme |
 scheme_name | Name of the mutual fund scheme |
 category | Broad category of the scheme (Equity, Debt, Hybrid etc.) |
 sub_category | Detailed classification within the category |
 plan | Indicates whether the scheme is Direct or Regular |
 launch_date | Date on which the scheme was launched |
 benchmark | Index used to compare fund performance |
 expense_ratio_pct | Annual expense charged by the fund |
 exit_load_pct | Charges applied on early redemption |
 min_sip_amount | Minimum amount required for SIP investment |
 min_lumpsum_amount | Minimum one-time investment amount |
 fund_manager | Person responsible for managing the fund |
 risk_category | Risk level assigned to the scheme |
 sebi_category_code | SEBI classification code |


 ## fact_nav

 | Column | Description |
|--------|-------------|
| amfi_code | Fund identifier |
| date | NAV date |
| nav | Daily Net Asset Value of the scheme |

## fact_transactions

| Column | Description |
|--------|-------------|
| investor_id | Unique identifier for an investor |
| transaction_date | Date on which the transaction was made |
| amfi_code | Fund identifier |
| transaction_type | SIP, Lumpsum or Redemption |
| amount_inr | Transaction amount in Indian Rupees |
| state | State of the investor |
| city | City of the investor |
| city_tier | Tier classification of the city |
| age_group | Investor age group |
| gender | Investor gender |
| annual_income_lakh | Annual income in lakhs |
| payment_mode | Mode of payment used |
| kyc_status | KYC verification status |

## fact_performance

| Column | Description |
|--------|-------------|
| amfi_code | Fund identifier |
| return_1yr_pct | Fund return over the last 1 year (%) |
| return_3yr_pct | Fund return over the last 3 years (%) |
| return_5yr_pct | Fund return over the last 5 years (%) |
| benchmark_3yr_pct | Benchmark return over 3 years (%) |
| alpha | Excess return generated over benchmark |
| beta | Measure of fund volatility compared to market |
| sharpe_ratio | Risk-adjusted return metric |
| sortino_ratio | Downside risk-adjusted return metric |
| std_dev_ann_pct | Annualized standard deviation (%) |
| max_drawdown_pct | Maximum decline from peak value (%) |
| aum_crore | Assets under management (crores) |
| expense_ratio_pct | Annual expense charged by the fund (%) |
| morningstar_rating | Morningstar fund rating |
| risk_grade | Overall risk grade assigned to the fund |