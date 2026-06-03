-- 1-Top 5 Funds by AUM
SELECT scheme_name,fund_house,aum_crore
FROM fact_performance f
JOIN dim_fund d
    ON f.amfi_code = d.amfi_code
ORDER BY aum_crore DESC
LIMIT 5;

--2- Avg Nav per month
SELECT strftime('%Y-%m', date) AS month,ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY strftime('%Y-%m', date)
ORDER BY month;

--3-Transactions by State

SELECT state,COUNT(*) AS total_transactions,ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

--4-Funds with Expense Ratio < 1%
SELECT scheme_name,fund_house,expense_ratio_pct
FROM fact_performance f
JOIN dim_fund d
    ON f.amfi_code = d.amfi_code
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

--5-Top 5 Fund Houses by AUM
SELECT fund_house,ROUND(SUM(aum_crore),2) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

--6-Average Return by Risk Grade
SELECT risk_grade,ROUND(AVG(return_3yr_pct),2) AS avg_return_3yr
FROM fact_performance
GROUP BY risk_grade
ORDER BY avg_return_3yr DESC;

--7-Monthly SIP Trend
SELECT month,sip_inflow_crore,yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;

--8-Top 5 Categories by Net Inflow
SELECT category,ROUND(SUM(net_inflow_crore),2) AS total_inflow
FROM category_inflows
GROUP BY category
ORDER BY total_inflow DESC
LIMIT 5;


--9-Transaction Type Distribution
SELECT transaction_type,COUNT(*) AS total_transactions,ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;

--10-Top 10 Funds by 5-Year Return
SELECT scheme_name,fund_house,return_5yr_pct
FROM fact_performance f
JOIN dim_fund d
    ON f.amfi_code = d.amfi_code
ORDER BY return_5yr_pct DESC
LIMIT 10;