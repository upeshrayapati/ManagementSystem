from repositories import request_repo,manager_repo
from services import manager_services
from services.auth import ManagerAuthentication


mgr_db=manager_repo.ManagerDB()
req_db = request_repo.RequestDB()
mgr_auth=ManagerAuthentication(mgr_db,req_db)

def managerWelcome(mgr_id):
    print(f'Welcome {mgr_id}')


def managerMainMenu(mgr_id):
    managerWelcome(mgr_id)
    choice=int(input('''
                    Press 1 to view your team
                    Press 2 to view project assigned by Admin
                    Press 3 to give task for Employee
                    Press 4 to request an Employee 
                    Press 5 to verify the task '''))
    
    if choice==1:
        manager_services.viewAllEmp(mgr_id,mgr_auth)
    elif choice==2:
        pass
    elif choice==3:
        pass
    elif choice==4:
        manager_services.mgrRequest(mgr_auth,mgr_id)
        managerMainMenu(mgr_id)
    elif choice==5:
        pass
     