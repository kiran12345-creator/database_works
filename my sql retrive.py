import mysql.connector
con=mysql.connector.connect(
                    user='root',
                    password='root',
                    host='localhost',
                    database='school_db'
)
c=con.cursor()
query='select * from student where roll_no = %s'
data=(101,)
c.execute(query,data)
records=c.fetchone()
if records:
    print(records)
else:
    print('no record found')
c.close()
con.close()
