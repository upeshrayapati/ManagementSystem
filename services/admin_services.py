


def seeMgrReq(admin_obj):
    datas=admin_obj.req_db.getAllReq()
    emp_datas=admin_obj.db.getEmpwoMgr()
    if datas:
        for data in datas:
            print(f'request_id {data[0]}: Manager id with {data[1]} is requesting an employee for the team')
        choice=int(input("""
                        Press 1 for assigning the Employee
                        Press 2 to Reject the request
                        Press 3 for Main Menu
                        Enter your option:"""))    
        if choice==1:
            print("Employees without having manager")
            for emp_data in emp_datas:
                print(f'''
              emp_id:{emp_data[0]}
            emp_name:{emp_data[1]}''')
            req_id=int(input("Emter request id:"))    
            mgr_id= int(input("Enter manager id:"))
            emp_id=int(input("Enter employee id:"))
            admin_obj.db.updateMgr(emp_id,mgr_id)
            admin_obj.req_db.deleteReq(req_id) 
            print("Requested handled successfully")   
            seeMgrReq(admin_obj)   

        elif choice ==2:
            req_id=int(input("Emter request id to reject:"))
            admin_obj.req_db.deleteReq(req_id)
            print("Requested rejected successfully")
            seeMgrReq(admin_obj)

        elif choice==3:
            return    
        
        else:
            print("invalid option selected")
            seeMgrReq()
    else:
        print("---No Request----")
        return        