from enum import auto
from tkinter import *
from tkinter import messagebox
import mysql.connector
db=mysql.connector.connect(host="localhost",port=3306,username="root",password="root",database="forminfo")
cursor=db.cursor()
def insert():
    choice=""
    if var1.get()==1:
        choice+=" music"
    if var2.get()==1:
        choice+=" dance"
    if var3.get()==1:
        choice+=" gaming"
    sql="INSERT INTO info VALUES(%s,%s,%s,%s,%s)"
    val=((sroll.get(),s.get(),s1.get(),svar.get(),choice))
    cursor.execute(sql,val)
    messagebox.showinfo("info","inserted succesfully")
    db.commit()

win=Tk()
win.title="form"
foo1=Label(win,text="STUDENT INFORMATION",fg="red")
foo1.pack()
# foo2=Label(win,text="the program shows different types of gui programming")
# foo2.pack()
Label(win,text="ROLL NO :").pack(anchor=W)
sroll=IntVar()
foo9=Entry(win,textvariable=sroll,width=3)
foo9.pack(anchor=W)
#name section
Label(win,text="name :").pack(anchor=W)
s=StringVar()
foo3=Entry(win,textvariable=s,width=30)
foo3.pack(anchor=W)
#checkbox
Label(win,text="hobbies :").pack(anchor=W)
var1=IntVar()
var2=IntVar()
var3=IntVar()
c1=Checkbutton(win,text="music",variable=var1,onvalue=1,offvalue=0)
c1.pack(anchor=W)
c2=Checkbutton(win,text="dance",variable=var2,onvalue=1,offvalue=0)
c2.pack(anchor=W)
c3=Checkbutton(win,text="gaming",variable=var3,onvalue=1,offvalue=0)
c3.pack(anchor=W)
#radiio
Label(win,text="gender").pack(anchor=W)
s1=StringVar()
r1=Radiobutton(win,text="male",variable=s1,value='male')
r1.pack(anchor=W)
r2=Radiobutton(win,text="female",variable=s1,value='female')
r2.pack(anchor=W)
#scalebar
Label(win,text="age").pack(anchor=W)
svar=IntVar()
scale=Scale(win,variable=svar,orient=HORIZONTAL)
scale.pack(anchor=W)
def fun_when_pressed():
    choice=""
    if var1.get()==1:
        choice+="music "
    if var2.get()==1:
        choice+=" dance "
    if var3.get()==1:
        choice+="gaming"
    messagebox.showinfo("information","your name is %s.\nyour choice is %s.\nyou are %s\nyour age is %s"%(s.get(),choice,s1.get(),svar.get()))
#button
b1=Button(win,text="print",command=fun_when_pressed)
b1.pack(anchor=W)
b2=Button(win,text="insert",command=insert)
b2.pack(anchor=W)
win.mainloop()
db.close()