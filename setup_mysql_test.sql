-- script preparing a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* to 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* to 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
