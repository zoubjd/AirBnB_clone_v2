--grants select priv to test user
CREATE DATABASE hbnb_test_db IF NOT EXISTS;
CREATE USER hbnb_test @'localhost' IF NOT EXISTS;
GRANT SELECT ON DATABASE hbnb_test_db TO hbnb_test;
