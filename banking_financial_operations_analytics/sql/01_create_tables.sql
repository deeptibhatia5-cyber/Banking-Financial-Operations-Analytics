-- Banking & Financial Operations Analytics
-- Update column types/names after inspecting the actual dataset.

CREATE DATABASE IF NOT EXISTS banking_analytics;
USE banking_analytics;

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id   VARCHAR(50) PRIMARY KEY,
    customer_id      VARCHAR(50),
    transaction_date DATETIME,
    transaction_amount DECIMAL(12, 2),
    transaction_type VARCHAR(50),
    payment_method   VARCHAR(50),
    transaction_status VARCHAR(30),
    branch           VARCHAR(100),
    region           VARCHAR(50)
);

-- After importing the CSV, run validation queries before analysis.
SELECT COUNT(*) AS row_count FROM transactions;
SELECT COUNT(DISTINCT transaction_id) AS unique_transaction_ids
FROM transactions;
