from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB
from validation.email_validator import email_vali
from validation.pass_validator import password_vali
from getpass4 import getpass
from utils.pass_hash import password_hasher,check_password


#this object is for emp-repo
emp_db = EmployeeDB()

#this object is for emp-auth
emp_auth= EmployeeAuthentication(emp_db)

def employeeUsername():
    name=input("enter your name:")
    return name


def employeeEmail(name):
    email=input("Enter your email:")
    verify_email=emp_db.searchEmp(email)
    if verify_email is None:
        if email_vali(email) is not None:
            employeePassword(name,email)
        else:
            print("Enter valid eamil-id:")
            employeeEmail(name)
    else:
        print("email already exists")
        employeeLogin()            


def employeePassword(name,email): 
    password = getpass("Enter your password:")
    confirm_pw =getpass("Enter your password:")
    if password == confirm_pw:
        if password_vali(password):
            password=password_hasher(password)
            emp_auth.createEmployee(name,email,password)
        else:
                    print("""password is not valid
                        password should be min length of 5
                        password should contain atleast one uppercase characters
                        password should contain atleast onelowercase characters
                        password should contain atlease one special character
                        password should contain atlest one digit
                        """)
                    employeePassword(name,email)
    else:
                print("Pasword doesn't match")
                employeePassword(name,email)    

def employeeSignup():
     print("Employee Signup")
     name1=employeeUsername()
     employeeEmail(name1)             


def employeeEmailLogin():
     
     email = input("Enter your email:")
     if email_vali(email) is not None:
            employeePassLogin(email)
     else:
          print("Enter valid eamil-id:")
          employeeEmailLogin()



def employeePassLogin(email):
               
     password = getpass("Enter password:")
     hashed_pw = emp_auth.empLogin(email)
     if check_password(password,hashed_pw):
          print("Login successful")
     else:
          print("Login failed")  
          employeePassLogin(email) 

def employeeLogin():
     print("Employee  login")
     employeeEmailLogin()             