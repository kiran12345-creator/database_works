import mysql.connector

con = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='school_db'
)

print(con)

# Cursor object — for executing SQL queries
c = con.cursor()

query='select * from student'
c.execute(query)
records=c.fetchall()
if records:
    for record in records:
        print(record)
else:
    print('no record found')

c.close()
con.close()