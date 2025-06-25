DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS health_metrics;

CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT
);

CREATE TABLE health_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    timestamp TEXT,
    heart_rate INTEGER,
    temperature REAL,
    FOREIGN KEY (patient_id) REFERENCES patients (id)
);

INSERT INTO patients (name, age, gender) VALUES ('John Doe', 30, 'Male');
INSERT INTO health_metrics (patient_id, timestamp, heart_rate, temperature)
VALUES (1, datetime('now'), 72, 98.6);