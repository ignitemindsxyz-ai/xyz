import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='')
cursor = conn.cursor()

cursor.execute('SHOW DATABASE')
cursor.execute('USE 2nd_database')
cursor.execute(
    'CREATE DATABASE IF NOT EXISTS school_db '
    'CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci'
)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
               id INT NOT NULL AUTO_INCREMENT,
               name VARCHAR(100) NOT NULL,
               email VARCHAR(100) NOT NULL,
               age TINYINT NOT NULL CHECK(age BETWEEN 1 AND 100),
               course VARCHAR DEFAULT 'Undecided')
               grade DECIMAL(5,2) DEFAULT NULL,
               active BOOLEAN NOT NULL DEFAULT TRUE,
               enrolled_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
               updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT TIME_STAMP,
               PRIMARY KEY (id),
               UNIQUE KEY uq_email (email),
               INDEX idx_course (course),
               INDEX idx_grade (grade)
               )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
''')

conn.commit()
print("Tables created")