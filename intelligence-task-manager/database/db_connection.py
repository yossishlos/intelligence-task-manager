import mysql.connector

class DB_connection:
    def __init__(self, config: dict={
        "host" : "localhost",
        "user" : "root",
        "password" : "1234",
        "database" : "Intelligence_db"
    }):
        self.config = config
        self.connection = None
        self.cursor = None

    def get_connection(self):
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor(dictionary=True)

    def create_database(self):
        self.cursor.execute("""
create database if not exists Intelligence_db
""")

    def create_tables(self):
        self.cursor.execute("""
CREATE TABLE if NOT exists agents(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialty VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    completed_missions INT DEFAULT 0,
    failed_missions INT DEFAULT 0,
    agent_rank ENUM("Junior", "Senior", "Commander") DEFAULT "Junior"
    )
""")
        self.cursor.execute("""
CREATE Table if NOT exists missions(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    difficulty INT,
    importance INT,
    status ENUM("NEW", "ASSIGNED", "PROGRESS_IN", "COMPLETED", "FAILED", "CANCELLED") DEFAULT "NEW",
    risk_level ENUM("LOW", "MEDIUM", "HIGH", "CRITICAL"),
    assigned_agent_id INT DEFAULT NULL
    )
""")