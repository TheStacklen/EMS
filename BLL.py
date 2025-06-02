import DBAL
class Employee:
    def __init__(self,empID=1,empname="EmployeeName",DOJ="2024-01-01",salary=900,departmentID=10,age=19,country="India",contact=7879794548):
        self.empID=empID
        self.empName=empname
        self.DOJ=DOJ
        self.salary=salary
        self.depID=departmentID
        self.age=age
        self.country=country
        self.contact=contact
    def get(self):
        data=DBAL.getData()
        return data
    def post(self):
        DBAL.insertData(self)
    def put(self):
        DBAL.updateData(self)
    def delete(self):
        DBAL.deleteData(self)
        
        
