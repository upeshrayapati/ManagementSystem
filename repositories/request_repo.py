from db_pool import connection

class RequestDB:
    def createRequest(self,mgr_id):
        query = 'insert into mgr_req (req_by) values(%s)'
        values  = (mgr_id,)
        connection.cursor.execute(query,values)
        connection.connect.commit()
    def getAllReq(self):
        query ='select * from mgr_req'
        connection.cursor.execute(query)
        datas = connection.cursor.fetchall()
        return datas   

    def  deleteReq(self,id):
        query = 'delete from mgr_req where req_id=%s'
        connection.cursor.execute(query,(id,))
        connection.connect.commit()
        print("request handled successfully")
    
# req_db=RequestDB()
# req_db.createRequest(7)    