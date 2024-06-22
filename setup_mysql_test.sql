--grants select priv to test user
CREATE DATABASE hbnb_test_db IF NOT EXISTS;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
GRANT ALL ON hbnb_test_db TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
