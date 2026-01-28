from mysql import connector 
from dotenv import load_dotenv
import os

load_dotenv()

connect = connector.connect(
    user='root',
    password=os.getenv('DATABASE_PW'),
    host='localhost',
    database='management_db'
)
# if connect.is_connected():
#     print("Success")
# else:
#     print("Not connected")    
cursor=connect.cursor()