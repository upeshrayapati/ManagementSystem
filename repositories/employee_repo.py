from db_pool.connection import connect,cursor


class EmployeeDB:
    def createEmp(self,name,email,password):
        query = 'insert into user(user_name,user_email,password) values(%s,%s,%s)'
        values = (name,email,password)
        cursor.execute(query,values)
        connect.commit()
        print('user created successfully')


    def searchEmp(self,email):
        query = 'select password from user where user_email= %s'
        values = email,
        data=cursor.execute(query,values)
        data = cursor.fetchone()
        return data[0]
    
    def searchEmail(self,email):
        query = 'select user_email from user where user_email=%s'
        values = email,
        data=cursor.execute(query,values)
        data = cursor.fetchall()
        return data[0]
    