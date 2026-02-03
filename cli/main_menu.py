from .employee_menuu import employeeSignup,employeeLogin
from .admin_menu import adminLogin
from repositories.employee_repo import EmployeeDB

emp_db = EmployeeDB()

def menu():
    while True:
        print('''Welcome
              Press 1 for Admin Login
              Press 2 for Employee Signup
              Press 3 for Employee Login''')
        choice=int(input("Enter your Option:"))
        if choice==1:
            adminLogin()
        elif choice==2:
            employeeSignup()
        elif choice==3:
            employeeLogin()
        else:
            print("Select Valid Option!")

        

        
