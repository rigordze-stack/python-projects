CREATE DATABASE pythondb;

-- Crear la tabla sales_data
CREATE TABLE IF NOT EXISTS sales_data (
    id SERIAL PRIMARY KEY,
    categoria VARCHAR(100),
    producto VARCHAR(100),
    ventas INTEGER,
    unidades INTEGER
);