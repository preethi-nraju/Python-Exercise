import dbconnect
class Task:
    """taskid=priority=ownerid=creatorid=0
    taskname=description=status=notes=bookmark=createdon=modifiedon=''"""
    def __init__(self,taskid,taskname,description,status,priority,notes,bookmark,ownerid,creatorid,createdon,modifiedon):
        self.taskid=taskid
        self.taskname=taskname
        self.description=description
        self.status=status
        self.priority=priority
        self.notes=notes
        self.bookmark=bookmark
        self.ownerid=ownerid
        self.creatorid=creatorid
        self.createdon=createdon
        self.modifiedon=modifiedon
        dbconnect.insert(taskid,taskname,description,status,priority,notes,bookmark,ownerid,creatorid,createdon,modifiedon)
    #def showvalues(self):
     #   print("Given Values are : ")
       # print(self.taskid,self.taskname,self.description,self.status,self.priority,self.notes,self.bookmark,self.ownerid,self.creatorid,self.createdon,self.modifiedon)
