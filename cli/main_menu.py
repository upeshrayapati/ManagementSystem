from .employee_menu import employeeSignup,employeeLogin
def menu():
    while True:
        print('''Welcome
              Press 1 for Admin Login
              Press 2 for Employee Signup
              Press 3 for Employee Login''')
        choice=int(input("Enter your Option:"))
        if choice==1:
            pass
        elif choice==2:
            employeeSignup()
        elif choice==3:
            employeeLogin()
        else:
            print("Select Valid Option!")

        

        
