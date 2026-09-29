import mysql.connector
con = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='school_db'
)

c = con.cursor()

query =('insert into student(roll_no,name,age,place,phone,total_mark) '
        'values(%s,%s,%s,%s,%s,%s) ')
data=(101,'arun',11,'ekm','1234567891',149)
c.execute(query,data)
con.commit()


print('table created')


c.close()
con.close()