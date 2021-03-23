DROP DATABASE IF EXISTS property_db;
CREATE DATABASE property_db;
CREATE USER property_user WITH PASSWORD 'property_pass';
ALTER ROLE property_user SET client_encoding TO 'utf8';
ALTER ROLE property_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE property_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE property_db TO property_user;
