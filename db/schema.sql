PRAGMA foreign_keys = ON;

CREATE TABLE customer (
    customer_id INTEGER PRIMARY_KEY,
    customer_type VARCHAR(50),
    Gender VARCHAR(50)
);

CREATE TABLE payment (
    payment_id INTEGER PRIMARY_KEY,
    payment VARCHAR(50),
    branch VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE invoice (
    invoice_id VARCHAR PRIMARY_KEY,
    branch VARCHAR(50),
    city VARCHAR(50),
    customer_id INTEGER NOT NULL,
    product_line VARCHAR(50),
    unit_prie DECIMAL(2),
    quantity INTEGER,
    tax FLOAT,
    total FLOAT,
    invoice_date DATE,
    invoice_time TIMESTAMP,
    payment_id INTEGER NOT NULL,
    cogd DECIMAL(2),
    gross_margin FLOAT,
    gross_income FLOAT,
    rating DECIMAL(1),
    FOREIGN KEY (customer_id) REFERENCES store (store_id),
    FOREIGN KEY (payment_id) REFERENCES customer (customer_id)
);