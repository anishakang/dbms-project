import cv2
import numpy as np

class queries(object):


                                    import mysql.connector
                                    db=mysql.connector.connect(host="localhost",user="root",password="dpsdpsdps",database="project")
                                    cursor=db.cursor()
                                    '''
                                    query="insert into highscore values(%s,%s,%s,%s,%s,%s)"
                                    data=(nam,score,s2,s3,ts,g)
                                    cursor.execute(query,data)
                                    db.commit()
                                    '''
                                    cursor.execute("select * from score")
                                    result=cursor.fetchall()
                                    for i in result:
                                        for k in i:
                                            str1=str(k)
                                            l=len(str1)
                                            if l==2:
                                                print(k,end="    ")
                                            else:
                                                print(k,end="     ")
                                            
                                        print()
                                    print(".........................................................")


                                                                                                                
