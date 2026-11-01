-- Run after importing and validating the dataset.

USE banking_analytics;

-- 1. Transaction count and total value
SELECT
    COUNT(*) AS total_transactions,
    SUM(transaction_amount) AS total_transaction_value
FROM transactions;

-- 2. Transaction status distribution
SELECT
    transaction_status,
    COUNT(*) AS transaction_count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM transactions), 2) AS percentage
FROM transactions
GROUP BY transaction_status
ORDER BY transaction_count DESC;

-- 3. Payment method performance
SELECT
    payment_method,
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN LOWER(transaction_status) = 'failed' THEN 1 ELSE 0 END) AS failed_transactions,
    ROUND(
        100.0 * SUM(CASE WHEN LOWER(transaction_status) = 'failed' THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0), 2
    ) AS failure_rate_pct
FROM transactions
GROUP BY payment_method
ORDER BY failure_rate_pct DESC;

-- 4. Regional transaction volume and value
SELECT
    region,
    COUNT(*) AS transaction_count,
    SUM(transaction_amount) AS transaction_value
FROM transactions
GROUP BY region
ORDER BY transaction_value DESC;

-- 5. Monthly transaction trend
SELECT
    DATE_FORMAT(transaction_date, '%Y-%m') AS transaction_month,
    COUNT(*) AS transaction_count,
    SUM(transaction_amount) AS transaction_value
FROM transactions
GROUP BY DATE_FORMAT(transaction_date, '%Y-%m')
ORDER BY transaction_month;
