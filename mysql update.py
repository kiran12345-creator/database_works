import mysql.connector
con=mysql.connector.connect(
                    user='root',
                    password='root',
                    host='localhost',
                    database='school_db'
)
c=con.cursor()

query=' update student set name=%s where roll_no=%s'
data=('arun',101)
c.execute(query,data)
con.commit()
if c.rowcount>0:
    print('updated sucessfully')

else:
    print('no record found')


c.close()
con.close()


