from db_pool.connection import connect,cursor


class EmployeeDB:
    def createEmp(self,name,email,password):
        query = 'insert into user(user_name,user_email,password) values(%s,%s,%s)'
        values = (name,email,password)
        cursor.execute(query,values)
        connect.commit()