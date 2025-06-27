-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;

-- Use the database
USE hbtn_0e_6_usa;

-- Create table states
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

-- Insert some test data
INSERT INTO states (name) VALUES ('California'), ('Texas'), ('Louisiana');
