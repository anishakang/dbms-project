from flask import Flask, Response, render_template, jsonify, request



from flask import Flask

import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="dpsdpsdps",database="project")
cursor=db.cursor()
cursor.execute("select count(acc_no) from customer")
result=cursor.fetchall()

i=result[0]
list(i)

global acc_no
acc_no=i[0]+1
print(acc_no)
'''
cursor.execute("select * from score")
result=cursor.fetchall()
alist=[]
for i in result:
   for k in i:
      alist.append(k)

<table>
	<tr><th>output<th></tr>
	{% for item in alist %}
	<tr><td>{{item}}</td><tr>
	{% endfor %}
</table>
'''     
app = Flask(__name__)
  


@app.route('/')
def index():
   return render_template("index.html")
'''
def index() :
   return render_template("index.html",alist=alist)
'''
@app.route('/',methods=["POST"])
def getvalue():
   cname=request.form["cname"]
   ph_no=request.form["ph_no"]
   p_type=request.form["p_type"]
   if (p_type=="Gold"):
         
         cursor.execute("select * from slot1 where p_type='Gold'")
         result=cursor.fetchall()
         
         alist=[]
         for i in result:
            for k in i:
               alist.append(k)
         cursor.execute("select * from slot2 where p_type='Gold'")
         result=cursor.fetchall()
         
         blist=[]
         for i in result:
            for k in i:
               blist.append(k)
         cursor.execute("select * from slot3 where p_type='Gold'")
         result=cursor.fetchall()
         
         clist=[]
         for i in result:
            for k in i:
               clist.append(k)
         cursor.execute("select * from slot4 where p_type='Gold'")
         result=cursor.fetchall()
         
         dlist=[]
         for i in result:
            for k in i:
               dlist.append(k)
         cursor.execute("select * from pay where p_type='Classic'")
         result=cursor.fetchall()
         
         elist=[]
         for i in result:
            for k in i:
               elist.append(k)
               
   if (p_type=="Classic"):
         
         cursor.execute("select * from slot1 where p_type='Classic'")
         result=cursor.fetchall()
         
         alist=[]
         for i in result:
            for k in i:
               alist.append(k)
         cursor.execute("select * from slot2 where p_type='Classic'")
         result=cursor.fetchall()
         
         blist=[]
         for i in result:
            for k in i:
               blist.append(k)
         cursor.execute("select * from slot3 where p_type='Classic'")
         result=cursor.fetchall()
         
         clist=[]
         for i in result:
            for k in i:
               clist.append(k)
         cursor.execute("select * from slot4 where p_type='Classic'")
         result=cursor.fetchall()
         
         dlist=[]
         for i in result:
            for k in i:
               dlist.append(k)
         cursor.execute("select * from pay where p_type='Classic'")
         result=cursor.fetchall()
         
         elist=[]
         for i in result:
            for k in i:
               elist.append(k)
         
   if (p_type=="Silver"):
         
         cursor.execute("select * from slot1 where p_type='Silver'")
         result=cursor.fetchall()
         
         alist=[]
         for i in result:
            for k in i:
               alist.append(k)
         cursor.execute("select * from slot2 where p_type='Silver'")
         result=cursor.fetchall()
         
         blist=[]
         for i in result:
            for k in i:
               blist.append(k)
         cursor.execute("select * from slot3 where p_type='Silver'")
         result=cursor.fetchall()
         
         clist=[]
         for i in result:
            for k in i:
               clist.append(k)
         cursor.execute("select * from slot4 where p_type='Silver'")
         result=cursor.fetchall()
         
         dlist=[]
         for i in result:
            for k in i:
               dlist.append(k)
         cursor.execute("select * from pay where p_type='Silver'")
         result=cursor.fetchall()
         
         elist=[]
         for i in result:
            for k in i:
               elist.append(k)
   if (p_type=="Platinum"):
         
         cursor.execute("select * from slot1 where p_type='Platinum'")
         result=cursor.fetchall()
         
         alist=[]
         for i in result:
            for k in i:
               alist.append(k)
         cursor.execute("select * from slot2 where p_type='Platinum'")
         result=cursor.fetchall()
         
         blist=[]
         for i in result:
            for k in i:
               blist.append(k)
         cursor.execute("select * from slot3 where p_type='Platinum'")
         result=cursor.fetchall()
         
         clist=[]
         for i in result:
            for k in i:
               clist.append(k)
         cursor.execute("select * from slot4 where p_type='Platinum'")
         result=cursor.fetchall()
         
         dlist=[]
         for i in result:
            for k in i:
               dlist.append(k)
         cursor.execute("select * from pay where p_type='Platinum'")
         result=cursor.fetchall()
         
         elist=[]
         for i in result:
            for k in i:
               elist.append(k)
   if (p_type=="Diamond"):
         
         cursor.execute("select * from slot1 where p_type='Diamond'")
         result=cursor.fetchall()
         
         alist=[]
         for i in result:
            for k in i:
               alist.append(k)
         cursor.execute("select * from slot2 where p_type='Diamond'")
         result=cursor.fetchall()
         
         blist=[]
         for i in result:
            for k in i:
               blist.append(k)
         cursor.execute("select * from slot3 where p_type='Diamond'")
         result=cursor.fetchall()
         
         clist=[]
         for i in result:
            for k in i:
               clist.append(k)
         cursor.execute("select * from slot4 where p_type='Diamond'")
         result=cursor.fetchall()
         
         dlist=[]
         for i in result:
            for k in i:
               dlist.append(k)
         cursor.execute("select * from pay where p_type='Diamond'")
         result=cursor.fetchall()
         
         elist=[]
         for i in result:
            for k in i:
               elist.append(k)   
      
   query="insert into customer values(%s,%s,%s,%s)"
   data=(acc_no,cname,ph_no,p_type)
   
   cursor.execute(query,data)
   db.commit()

  
   

   
   
   return render_template("pass.html",cname=cname,ph_no=ph_no,p_type=p_type,alist=alist,blist=blist,clist=clist,dlist=dlist,elist=elist)
   
if __name__ == '__main__':
  
    
    app.run()
