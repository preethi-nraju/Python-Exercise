#this is db file
import mysql.connector

def connectdb():
    db = mysql.connector.connect(host="localhost", user="root", password="Preksha$29", database="task")
    curzor = db.cursor()
    print("""
         *-------------------------------------------------*
         ||||||||||Database Connected Successfully||||||||||
         *-------------------------------------------------*
         ||||||||||USER==root       DATABASE==task||||||||||
         *-------------------------------------------------*
         """)

def showtableval():
    db = mysql.connector.connect(host="localhost", user="root", password="Preksha$29", database="task")
    curzor = db.cursor()
    y=curzor.execute("select * from task")
    x=curzor.fetchall()
    for i in x:
        print(i)
    print("No. of rows are: ")
    curzor.execute("select Count(*) from task")
    print(curzor.fetchall())
def insert(taskid, taskname, description, status, priority, notes, bookmark, ownerid, creatorid, createdon, modifiedon):
    db = mysql.connector.connect(host="localhost", user="root", password="Preksha$29", database="task")
    curzor = db.cursor()
    command = ("insert into task(taskid,taskname,descript,stats,priority,notes,bookmark,ownerid,creatorid,createdon,modifiedon)""values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data = (taskid, taskname, description, status, priority, notes, bookmark, ownerid, creatorid, createdon, modifiedon)
    curzor.execute(command, data)
    db.commit()
def search(preethi):
    print("searching.....")
    #time.sleep(3)
    db = mysql.connector.connect(host="localhost", user="root", password="Preksha$29", database="task")
    curzor = db.cursor()
    print("connected")
    command="select descript from task where taskid=%s"%(preethi)
    #data=(taskid)
    curzor.execute(command)
    print(curzor.fetchall())