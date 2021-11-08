from dao import taskdao
import dbconnect
taskid=1028
taskname='add'
description='preksha'
status='completed'
priority=1
notes='notes 1'
bookmark='bookm13'
ownerid=115
creatorid=213
createdon='2021-02-03'
modifiedon='2021-02-14'
#creating obj with para
#tsk = taskdao.task.Task(taskid, taskname, description, status, priority, notes, bookmark, ownerid, creatorid, createdon,modifiedon)
#taskdao.run(tsk)#passing obj as param
dbconnect.search(1028)