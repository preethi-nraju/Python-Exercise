import dbconnect#module import
from service import task#from the package
import time

def run(t):#taking obj from mainfile
    print("<<<<<<<<<<<<      WELCOME TO TASK TRACKER      >>>>>>>>>>>>")
    time.sleep(2)#its just to show
    print("connecting to Database........... ")
    time.sleep(2)
#these values are passed to obj para to insert these to the table
    dbconnect.connectdb()#connecting db
    print("Inserting the values.....")
    time.sleep(2)#task object is created here
    print("Inserted Successfully,getting tables ready with newly inserted values....")
    time.sleep(2)
    dbconnect.showtableval()
    print("All values are commited successfully..")#showing table from dbconnect module

