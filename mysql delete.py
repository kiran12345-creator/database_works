import mysql.connector
con=mysql.connector.connect(
                    user='root',
                    password='root',
                    host='localhost',
                    database='school_db')
c=con.cursor()


query='delete from student where roll_no=%s'
data=(101,)
c.execute(query,data)
con.commit()


if c.rowcount>0:
    print('deleted')
else:
    print('no record found')


c.close()
con.close()
