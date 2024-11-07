import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="sharon@04",database="comproject")
cursor=mycon.cursor()
print("Thank's for contacting corona helpdesk")
print("please register to continue")
import random
code=random.randint(1000,5000)
print(code)
verify=int(input("please enter the above code:"))
ans='y'
if code==verify:
     print("successfully registered")
     while ans.lower()=='y':
         print("How can I help you\n 1-symptoms of corona virus\n 2-docter cunsultation\n 3-appoinment for vaccination\n 4-downloading certificate")
         choice=int(input("enter your chice:"))
         if choice==1:
             print("symptoms of corona virus:")
             print("refer this link to konw the symptoms of coronavirus:\nhttps://www.cdc.gov/coronavirus/2019-ncov/symptoms-testing/symptoms.html")
         elif choice==2:
             print("docter cunsultation:")
             print("what is your query?\n 1-regarding symptoms\n2-confusion in vaccinating\n 3-methods to manage with kidsfor social distancing\n 4-how to manage the effects of coronavirus")
             query=int(input("yor choice?:"))
             if query==1:
                 cursor.execute("select*from consultation")
                 data=cursor.fetchone()
                 for row in data:
                     print(row)
             elif query==2:
                 data=cursor.fetchone()
                 for row in data:
                     print(row)
             elif query==3:
                 data=cursor.fetchone()
                 for row in data:
                     print(row)
             elif query==4:
                 data=cursor.fetchone()
                 for row in data:
                     print(row)
         elif choice==3:
             print("appoinment for vaccination:")
             age=int(input("enter your age:"))
             if age>=15 and age<=40:
                 city=input("enter your city:")
                 if city=="chennai":
                     cursor.execute("select*from appoinment1")
                     data=cursor.fetchall()
                     for row in data:
                         print(row)
                 elif city=="madhurai":
                     cursor.execute("select*from appoinment2")
                     data=cursor.fetchall()
                     for row in data:
                         print(row)
                 elif city=="coimbatore":
                     cursor.execute("select*from appoinment3")
                     data=cursor.fetchall()
                     for row in data:
                         print(row)
                 else:
                     print("sorry vaccination is not available for your age")
         elif choice==4:
             print("downloading certificate:")
             name=input("enter your name:")
             cursor.execute("select*from certificate")
             data=cursor.fetchall()
             for row in data:
                 if row[1]==name:
                     print(row)
                 else:
                     continue
         else:
            print("invalid choice")
         ans=input("do you want to continue?(y/n):")
else:
    print("invalid code")
print("*******************THANK YOU**************************")
