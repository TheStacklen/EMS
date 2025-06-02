#CONNECTION
import pymysql
def Connection():
    conn=pymysql.connect(host="Localhost",
                           user="root",
                           password="sakln7794",
                           db="EMS")
    return conn
def getData():
    con=Connection()
    cursor=con.cursor()
    cursor.execute("select * from Employee")
    data=cursor.fetchall()
    return data
def insertData(obj):
    con=Connection()
    cursor=con.cursor()
    cursor.execute(f" INSERT INTO Employee (EmpID,EmpName,Date_of_joining,Sallary,DepartmentId,Age,Country,Contact) values({obj.empID},'{obj.empName}','{obj.DOJ}',{obj.salary},{obj.depID},{obj.age},'{obj.country}',{obj.contact})")
    con.commit()
    con.close()
def updateData(obj2):
    con=Connection()
    cursor=con.cursor()
    cursor.execute(f"update Employee set EmpName= '{obj2.empName}' where EmpID={obj2.empID}")
    con.commit()
    con.close()
def deleteData(obj3):
    con=Connection()
    cursor=con.cursor()
    cursor.execute(f"delete from Employee where EmpId={obj3.empID}")
    con.commit()
    
    
    
    
    
