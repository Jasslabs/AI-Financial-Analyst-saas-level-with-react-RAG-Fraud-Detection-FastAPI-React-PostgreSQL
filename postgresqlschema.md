CREATE TABLE documents (
id SERIAL PRIMARY KEY,
filename TEXT NOT NULL,
file_path TEXT NOT NULL,
uploaded_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE transactions (
id SERIAL PRIMARY KEY,
customer_id INT,
amount NUMERIC(12,2),
transaction_date DATE,
merchant TEXT,
is_fraud BOOLEAN DEFAULT FALSE,
fraud_score FLOAT
);

CREATE TABLE chat_logs (
id SERIAL PRIMARY KEY,
question TEXT,
answer TEXT,
created_at TIMESTAMP DEFAULT NOW()
);
