import mysql.connector
import pandas,numpy
db=mysql.connector.connect(host="localhost",user="root",password="Preksha$29",database="preksha")
curzor=db.cursor()
curzor.execute('insert into table1 values("animus",58745225)')
db.commit()
x=curzor.execute("select * from table1");
y=curzor.fetchall()
print(y)