from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB

#this object is for emp-repo
emp_db = EmployeeDB()

#this object is for emp-auth
emp_auth= EmployeeAuthentication(emp_db)

#For signing up new employee
def employeeSignup():
    print("Employee Signup")
    name = input("Enter your name:")
    email = input("Enter your email:")
    password = input("Enter your password:")
    emp_auth.createEmployee(name,email,password)

def employeeLogin():
    print("Employee Login")
   