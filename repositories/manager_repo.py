from db_pool.connection import connect,cursor

class ManagerDB:
    def getAllMgr(id):
        query = 'select * from user where is_manager=%s'
        cursor.execute(query,(1,))
        data = cursor.fetchall()
        return data
    def getEmp(self,id):
        query = 'select * from user where mgr_id=%s '
        cursor.execute(query,(id,))
        datas=cursor.fetchall()
        return datas
