from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB
from validation.email_validator import email_vali
from validation.pass_validator import password_vali
from getpass4 import getpass
from utils.pass_hash import password_hasher,check_password
from .manager_menu import managerMainMenu



#this object is for emp-repo
emp_db = EmployeeDB()

#this object is for emp-auth
emp_auth= EmployeeAuthentication(emp_db)

#For signing up new employee
def employeeSignup():
    print("Employee Signup")
    name = input("Enter your name:")
    email = input("Enter your email:")
    verify_email = emp_db.searchEmp(email)
    if verify_email is  None:
        if email_vali(email) is not None:
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
                    employeeSignup()
            else:
                print("Pasword doesn't match")
                employeeSignup()        
                    
        else:
            print("Email  is not valid")
            employeeSignup()   
    else:
        print("Email already exists")
        employeeLogin()        


def employeeLogin():
    print("Employee Login")
    email = input('Enter your email:')
    password = getpass("Enter your password:")
    data=emp_auth.empLogin(email)
    hashed_pw=data[3]
    is_manager=data[5]
    if check_password(password,hashed_pw):
        if is_manager==1:

            print('Manager Login successful')
            managerMainMenu(data[0])
        else:
            print('Employee Login Successful')    
    else:
        print('Login failed')    

