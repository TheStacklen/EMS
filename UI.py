import BLL
user_input=input("Enter G to get data, I to insert data, U to update data, D to delete data")
if user_input=="G":
    obj=BLL.Employee()
    data=obj.get()
    for d in data:
        print(d)
elif user_input=="I":
    id=int(input("Enter ID :"))
    name=input("Enter Name :")
    doj=input("Enter Date Of Joing :")
    salary=float(input("Enter Salary :"))
    depId=int(input("Enter Department Id :"))
    age=int(input("Enter Age :"))
    country=input("Enter Country :")
    contact=int(input("Enter Contact :"))
    obj=BLL.Employee(id,name,doj,salary,depId,age,country,contact)
    obj.post()  
    print("Data Sumbitted Successfully")
elif user_input=="U":
    ID=int(input("Enter ID :"))
    name=input("Enter name :")
    obj2=BLL.Employee(empID=ID,empname=name)
    obj2.put()
    print("Update successfully")
elif user_input=="D":
    id=int(input("Enter ID :"))
    obj3=BLL.Employee(id)
    obj3.delete()
    print("Delete successfully")


        

        
