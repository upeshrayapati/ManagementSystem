from getpass4 import getpass
from dotenv import load_dotenv
import os
from services.auth import AdminAuthentication
from repositories.employee_repo import EmployeeDB
from repositories.manager_repo import ManagerDB
from repositories.request_repo import RequestDB
from services import admin_services
emp_db = EmployeeDB()
mgr_db = ManagerDB()
req_db= RequestDB()
admin_auth = AdminAuthentication(emp_db,mgr_db,req_db)




load_dotenv()

def adminWelcome():
    print("Welcome back Admin")




def adminLogin():
    password = getpass("Enter your password:")
    if password==os.getenv('ADMIN_PW'):
        adminWelcome()
        adminMainMenu()
    else:
        print("password is incorrect try to login again")    
        
        adminLogin()

def managerPromotion():
        id = int(input("Enter the employee id to promote to manager:"))
        data=admin_auth.db.getEmp(id)
        if data[5]==0:           
            if data is not None:
                admin_auth.db.modifyEmptoMgr(id)
                adminMainMenu()
            else:
                print(f"employee with{id} is not present!.Enter valid ID")
                managerPromotion()    
        else:
            print(f"employee with {id} is already a manager ")
            managerPromotion()


def adminMainMenu():   
    choice = int(input("""
                    __________________________________________________
                    |Press 1 to view all employee data               |
                    |Press 2 to view all manager data                |
                    |Press 3 for promoting an Employee to Manager    |
                    |Press 4 to assign project to manager            |
                    |Press 5 to see the manager request from employee|
                    |Press 6 for assigning an Employee to Manager    |
                    |Press 7 to check an update of project           |
                    |Press 8 to Logout                               |
                    |________________________________________________|                  
                    Enter your choice:"""))
    if choice ==1:
        emp_datas=admin_auth.db.getAllEmp()
        for emp_data in emp_datas:
            print(f"""
                 _____________________________________
                 | employee_id:{emp_data[0]}         |
                 | employee name:{emp_data[1]}       |
                 | employee email:{emp_data[2]}      |
                 | employee manager id:{emp_data[4]} |
                 |___________________________________|
                """)
        adminMainMenu()
    elif choice==2:
        mgr_datas = admin_auth.mgr_db.getAllMgr()
        for mgr_data in mgr_datas:
            print(f"""
                 _____________________________________
                 | manager id:{mgr_data[0]}          |
                 | manager name:{mgr_data[1]}        |
                 | manager email:{mgr_data[2]}       |
                 |___________________________________|
                """)
        adminMainMenu()
    elif choice==3:
        managerPromotion()        
    elif choice==4:
        pass
    elif choice==5:
        admin_services.seeMgrReq(admin_auth)
        adminMainMenu()
    elif choice==6:
        pass
    elif choice==7:
        pass 
    elif choice==8:
        return
    else :
        print("Enter valid option")
        adminMainMenu()    