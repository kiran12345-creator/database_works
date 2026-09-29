

# define a class to perform database operations on vehicle table
# create a class named VehicleListCreateRetriveUpdateDelete
# with methods:
#     list()
#     create()
#     retrive()
#     delete()
#     update()
#
# db_file:vehicle_db
# table:vehicle
# id,brand,model,type,price,year
import mysql.connector
class VehicleListCreateRetriveUpdateDelete:

    def __init__(self):
        self.con= mysql.connector.connect(user='root',
                            password='root',
                            host='localhost',
                            database='vehicle_db')
        print(self.con)
        self.cursor=self.con.cursor()
        print("successfully connected")

    def list(self):
        query="select * from vehicle"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("no records found")
    def create(self,brand,model,type,price,year):
        query="insert into vehicle(brand,model,type,price,year)values(%s,%s,%s,%s,%s);"
        data=(brand,model,type,price,year)
        self.cursor.execute(query,data)
        self.con.commit()
    def update(self, id, new_price):
        query = "update vehicle set price=%s where id=%s"
        data = (new_price, id)
        self.cursor.execute(query, data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            print("Updation done ")
        else:
            print("No records updated ")

    def retrive(self, id):
        query = "select * from vehicle where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        record = self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("no record found")

    def delete(self,id):
        query="delete from vehicle where id=%s;"
        data=(id,)
        self.cursor.execute(query,data)
        self.con.commit()
        if self.cursor.rowcount>0:
            print("deleted data successfully")
        else:
            print("no record found")

v=VehicleListCreateRetriveUpdateDelete()
v.list()
#v.create('tata','nano','car',200000,'2014')
#v.retrive(3)
#v.delete(1)
#v.update(1,100000)
