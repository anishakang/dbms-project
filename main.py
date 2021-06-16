from flask import Flask, Response, render_template, jsonify, request



from flask import Flask

import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="dpsdpsdps",database="project")
cursor=db.cursor()
cursor.execute("select * from score")
result=cursor.fetchall()
alist=[]
for i in result:
   for k in i:
      alist.append(k)
      
app = Flask(__name__)
  


@app.route('/')

def index() :
   return render_template("index.html",alist=alist)

@app.route('/',methods=["POST"])
def getvalue():
   name=request.form["name"]
   roll=request.form["roll"]
   print(name)
   print(roll)
   query="insert into score values(%s,%s)"
   data=(name,roll)
   cursor.execute(query,data)
   db.commit()
   return render_template("pass.html",name=name,roll=roll)

if __name__ == '__main__':
  
    
    app.run()
