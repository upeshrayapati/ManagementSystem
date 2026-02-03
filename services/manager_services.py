

def viewAllEmp(mgr_id,mgr_obj):
    datas =mgr_obj.mgr_db.getEmp(mgr_id)
    if datas:
        print('YOUR TEAM')
        for data in datas:
            print(f'''h
                employee_id:{data[0]}
                employee_name:{data[1]}
                employee_email:{data[2]}             
                ''')
    else:
        print("No Employees assigned yet")
        mgrOption(mgr_id,mgr_obj)


def mgrRequest(mgr_obj,mgr_id):
    input("Press enter to request an employee for a team")
    mgr_obj.req_db.createRequest(mgr_id)
    print("request sent successfully")        


def mgrOption(mgr_id,mgr_obj):        
        print("""Enter 1 for requesting an employee from Admin
        Enter 2 to go back main menu""")
        choice=int(input("Enter your option:"))
        if choice==1:
             mgrRequest(mgr_obj,mgr_id)
        elif choice==2:
             return
        else:
             print("Invalid choice")
             mgrOption()


