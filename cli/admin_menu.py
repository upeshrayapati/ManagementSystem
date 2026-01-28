from getpass4 import getpass
from dotenv import load_dotenv
import os

load_dotenv()

def adminMenu():
    print("Welcome back Admin")


def adminLogin():
    password = getpass("Enter your password:")
    print(os.getenv('ADMIN_PW'))

adminLogin()