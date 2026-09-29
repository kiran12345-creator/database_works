import mysql.connector

con = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost'
)

print(con)

# Cursor object — for executing SQL queries
c = con.cursor()

query = 'CREATE DATABASE IF NOT EXISTS school_db'
c.execute(query)

print('database created')

c.close()
con.close()


# CREATING TABLE

con = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='school_db'
)

c = con.cursor()

query = """CREATE TABLE student(
             roll_no INT NOT NULL PRIMARY KEY,
             name VARCHAR(20),
             age INT,
             place VARCHAR(25),
             phone VARCHAR(25),
             total_mark INT
          )"""

c.execute(query)

print('table created')


c.close()
con.close()