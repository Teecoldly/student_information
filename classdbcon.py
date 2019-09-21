import sqlite3
from tkinter import *
class dbconnettest:
    def __init__(self):
        self.con = sqlite3.connect('data.db')
    def opendb(self):
        return  self.con
    def close(self):
        return self.con.close
    def execute(self,sql):
        result = self.con.execute(sql)
        return  result
    def executewhere(self,sql,wheredata):
        cur = self.con.cursor()
        result = cur.execute(sql,(wheredata))
        return  result
    def executewhere1(self,sql,wheredata):
        cur = self.con.cursor()
        result = cur.execute(sql,(wheredata,))
        return  result
    def commit(self):
        self.con.commit
class controldata:
    def __init__(self):
        self.con = dbconnettest()
        self.value= 0 
    def addlistview(self,obj):
        self.con.opendb()
        data = self.con.execute("select Student_ID from student")
        indexview = 1
        obj.delete(0,END)
        for i in data:
            obj.insert(indexview,i)
            indexview+=1
        self.con.close()
    def onselect(self,e):
        try:
            w = e.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            self.value= value
       
        except :
            return
    def showdata(self,obj):
        self.con.opendb()
        if(self.value!=0 ):
            arraydata=[]
            indexobj =0
            data= self.con.executewhere('select sd.* ,dm.Department_Description from student as sd inner join Department as dm  on sd.Department_ID = dm.Department_ID where Student_ID = ? ',self.value)
            for i in data: 
                for j in i:
                    arraydata.append(j)
            for i in obj:
                if indexobj == 4:
                    self.set_text(i,arraydata[6])
                elif indexobj ==5:
                    self.set_text(i,arraydata[5])
                elif indexobj ==6:
                    self.set_text(i,arraydata[4])
                else:
                    self.set_text(i,arraydata[indexobj])
                indexobj+=1
            self.con.close()
 
    def savedata(self,obj,Listbox):
        datainobj =[]
        self.con.opendb()
        for i in obj:
            datainobj.append(i.get())
       
        result  = self.con.executewhere1('select count(Department_ID) from Department where Department_ID = ?',str(datainobj[3]))
        for i in result:
            for j in i :
                data = j
        if(data==0):
            sql="INSERT INTO Department values('"+ datainobj[3] +"','"+ datainobj[4]+"')"
            self.con.execute(sql)
            self.con.commit()
            sql="INSERT INTO student values('"+ datainobj[0] +"','"+ datainobj[1] +"','"+ datainobj[2] +"','"+ datainobj[3] +"','"+ datainobj[6] +"','"+ datainobj[5] +"')"
            self.con.execute(sql)
            self.con.commit()
        else:
            result  = self.con.executewhere1('select count(*) from student where Student_ID = ?',str(datainobj[0]))
            for i in result:
                for j in i :
                    data = j
            if(data==0):
                sql="INSERT INTO student values('"+ datainobj[0] +"','"+ datainobj[1] +"','"+ datainobj[2] +"','"+ datainobj[3] +"','"+ datainobj[6] +"','"+ datainobj[5] +"')"
                self.con.execute(sql)
                self.con.commit()
            else:
                return
        self.addlistview(Listbox)
         
        self.con.close()
    def deletedata(self,obj,where,objlistbox):
        self.con.opendb()
        self.con.executewhere1("delete from student where student_Id = ?  ",where)
        for i in obj:
            self.set_text(i,'')
        self.addlistview(objlistbox)
    def updatedata(self,obj,objlistbox):
        datainobj =[]
        self.con.opendb()
        for i in obj:
            datainobj.append(i.get())
        try:
            sql="update student set name = '"+ datainobj[1] +"',Surname ='"+ datainobj[2] +"',Department_ID = '"+ datainobj[3] +"',Email='"+ datainobj[6] +"',Record_Date='"+ datainobj[5] +"' where Student_ID='"+datainobj[0] +"'"
            self.con.execute(sql)
            self.con.commit()
            self.con.close()
        except :
            return
        
    def set_text(self,obj,text):
        
        try:
            obj.delete(0,END)
            obj.insert(0,text)
        except :
            return
        
        return
    def closefrom(self, root):
        root.destroy()
        


        
    
        
 
 
 