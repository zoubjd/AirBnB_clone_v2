-- grants all prevliges to user

CREATE DATABASE hbnb_dev_db IF NOT EXISTS;
CREATE USER hbnb_dev @'localhost' IF NOT EXISTS;
GRANT ALL PRIVILEGES ON DATABASE hbnb_dev_db TO hbnb_dev;