#step 5 =============== Create Emplyee class ================================================================
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class EmployeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Shary")
        self.root.config(bg="White")
        self.root.focus_force()

        #step 8 ========== declare all variables =======================
        self.var_empno=StringVar()
        self.var_gender=StringVar()
        self.var_Contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_salary=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        
        self.var_doj=StringVar()

        # ============ search var ===============
        self.var_search_type=StringVar()
        self.var_txt_search=StringVar()
        

        #step 7 =========== search Employee fram =======================================================================
        search_emp=LabelFrame(self.root,text="Search Employee",font=("gody old style",12,"bold"),bg="White",relief=SUNKEN,bd=2)
        search_emp.place(x=250,y=20,width=600,height=70)

        #=========== cambobox ================
        search_type=ttk.Combobox(search_emp,textvariable=self.var_search_type,values=(("Select by","EID","Name","Email","Contact")),state="readonly",justify=CENTER,font="Lucida 13 bold")
        search_type.place(x=10,y=10,width=180)
        #also 
        search_type.current(0)
        # cmb_search.set("Select by")

        #========== Search Entry and button ==============
        txt_search=Entry(search_emp,textvariable=self.var_txt_search,font="Lucida 14 bold",bg="lightyellow")
        txt_search.place(x=200,y=10)
        btn_search=Button(search_emp,text="Search",command=self.search,font="Lucida 13 bold",bg="#4caf50",cursor="hand2",fg="white")
        btn_search.place(x=430,y=9,width=130,height=30)
        #======================== end search frame ========================================================================

        #Step 8 ======== Employee Details =================================================================================
        Label(self.root,text="Employee Details",font="Lucida 13 bold ",bg="blue",fg="White").place(x=50,y=100,width=1000)

        #=============== labels ==========================================
        #=========== column 1 labels ===================
        lbl_empno=Label(self.root,text="Emp ID",font="Lucida 14 bold",bg="white").place(x=50,y=150)
        Label(self.root,text="Name",font="Lucida 14 bold",bg="white").place(x=50,y=190)
        Label(self.root,text="Email",font="Lucida 14 bold",bg="white").place(x=50,y=230)
        Label(self.root,text="Address",font="Lucida 14 bold",bg="white").place(x=50,y=270)

        txt_empno=Entry(self.root,textvariable=self.var_empno,font="Lucida 14 bold",bg="lightyellow")
        txt_empno.place(x=150,y=150,width=180)
        txt_name=Entry(self.root,textvariable=self.var_name,font="Lucida 14 bold",bg="lightyellow")
        txt_name.place(x=150,y=190,width=180)
        txt_email=Entry(self.root,textvariable=self.var_email,font="Lucida 14 bold",bg="lightyellow")
        txt_email.place(x=150,y=230,width=180)
        self.txt_address=Text(self.root,font="Lucida 14 bold",bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        #=============== column 2 labes ======================
        Label(self.root,text="Gender",font="Lucida 14 bold",bg="white").place(x=350,y=150)
        Label(self.root,text="D.O.B",font="Lucida 14 bold",bg="white").place(x=350,y=190)
        Label(self.root,text="Password",font="Lucida 14 bold",bg="white").place(x=350,y=230)
        Label(self.root,text="Salary",font="Lucida 14 bold",bg="white").place(x=500,y=270)

        txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=(("Select by","Male","Female","Custom")),state="readonly",justify=CENTER,font="Lucida 13 bold")
        txt_gender.place(x=500,y=150,width=180)
        txt_gender.current(0)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font="Lucida 14 bold",bg="lightyellow")
        txt_dob.place(x=500,y=190,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font="Lucida 14 bold",bg="lightyellow")
        txt_pass.place(x=500,y=230,width=180)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font="Lucida 14 bold",bg="lightyellow")
        txt_salary.place(x=600,y=270,width=180)

        #================== column 3 labels & entry ===================
        Label(self.root,text="Contact No",font="Lucida 14 bold",bg="white").place(x=700,y=150)
        Label(self.root,text="D.O.J",font="Lucida 14 bold",bg="white").place(x=700,y=190)
        Label(self.root,text="User Type",font="Lucida 14 bold",bg="white").place(x=700,y=230)
       

        txt_contact=Entry(self.root,textvariable=self.var_Contact,font="Lucida 14 bold",bg="lightyellow")
        txt_contact.place(x=850,y=150,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font="Lucida 14 bold",bg="lightyellow")
        txt_doj.place(x=850,y=190,width=180)
        txt_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=(("Select by","Admin","Employee")),state="readonly",justify=CENTER,font="Lucida 13 bold")
        txt_utype.place(x=850,y=230,width=180)
        txt_utype.current(0)
        
        #================== buttons ================================
        btn_save=Button(self.root,text="Save",command=self.add,font="Lucida 13 bold",bg="blue",cursor="hand2",fg="white")
        btn_save.place(x=500,y=305,width=110,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font="Lucida 13 bold",bg="green",cursor="hand2",fg="white")
        btn_update.place(x=620,y=305,width=110,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font="Lucida 13 bold",bg="red",cursor="hand2",fg="white")
        btn_delete.place(x=740,y=305,width=110,height=30)
        btn_Clear=Button(self.root,text="Clear",command=self.clear,font="Lucida 13 bold",bg="grey",cursor="hand2",fg="white")
        btn_Clear.place(x=860,y=305,width=110,height=30)
        #============================= end ===============================================================
        
        #====================== Employee Fram db Details ======================================================
        emp_frame=Frame(self.root,bd=3,relief=SUNKEN)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        #================== scrolling ==============================
        scolly=Scrollbar(emp_frame,orient=VERTICAL)
        scollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        scolly.pack(side=RIGHT,fill=Y)
        scollx.pack(side=BOTTOM,fill=X)

        #============= Columns Headings  ======================================
        self.EmloyeeTable=ttk.Treeview(emp_frame,columns=("eid","name",'email',"gender",'contact','dob','doj','pass','utype','address','salary'),yscrollcommand=scolly.set,xscrollcommand=scollx.set)
        # config the scrollbar on emptable set view
        scollx.config(command=self.EmloyeeTable.xview)
        scolly.config(command=self.EmloyeeTable.yview)

        self.EmloyeeTable.heading('eid',text='EMP ID')
        self.EmloyeeTable.heading('name',text='Name')
        self.EmloyeeTable.heading('email',text='Email')
        self.EmloyeeTable.heading('gender',text='Gender')
        self.EmloyeeTable.heading('contact',text='Contact')
        self.EmloyeeTable.heading('dob',text='D.O.B')
        self.EmloyeeTable.heading('doj',text='D.O.J')
        self.EmloyeeTable.heading('pass',text='Password')
        self.EmloyeeTable.heading('utype',text='User Type')
        self.EmloyeeTable.heading('address',text='Address')
        self.EmloyeeTable.heading('salary',text='Salary')
        self.EmloyeeTable.pack(fill=BOTH,expand=1)

        self.EmloyeeTable.bind("<ButtonRelease-1>",self.get_data)

        #using for column start from beginning
        self.EmloyeeTable["show"]="headings"
        self.show()
        
        #========================== set Column width =========================
        self.EmloyeeTable.column('eid',width=100)
        self.EmloyeeTable.column('name',width=100)
        self.EmloyeeTable.column('email',width=100)
        self.EmloyeeTable.column('gender',width=100)
        self.EmloyeeTable.column('contact',width=100)
        self.EmloyeeTable.column('dob',width=100)
        self.EmloyeeTable.column('doj',width=100)
        self.EmloyeeTable.column('pass',width=100)
        self.EmloyeeTable.column('utype',width=100)
        self.EmloyeeTable.column('address',width=100)
        self.EmloyeeTable.column('salary',width=100)

        #Call show function after running the program
        #=================== end employee frame =================================================================


#step 10  employee buttons functions ================================================================================================================
        
    def add(self):
        conn=sqlite3.connect(database=r"IMS.db") 
        cr=conn.cursor()

        try:
            if self.var_empno.get()=="" or self.var_pass.get()=="" or self.var_doj.get()=="" or self.var_name.get()=="": #when id field empty show message
                messagebox.showerror("Error","Emp Id,Name,D.O.J and Password must be required ",parent=self.root)
            else:
                #executing the query to check the emplyee of the given id 
                cr.execute("Select * From Employee where eid=?",(self.var_empno.get(),))
                #retrive the employees of the given id   
                row=cr.fetchone()
                if row!=None: #when row is not empty means there already this employee
                    messagebox.showerror("Error","This Employee ID already assigned,try different ID",parent=self.root)
                else:
                    #check the 
                    if self.var_utype.get()=="Admin":
                        cr.execute("Select COUNT(*) from Employee where utype=?",("Admin",))
                        count_adm=cr.fetchone()[0]
                        if count_adm > 0:
                            messagebox.showerror("Error","There only one Admin in the Store!")
                            return
                    else:
                            cr.execute("insert into Employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values (?,?,?,?,?,?,?,?,?,?,?)",( 
                            self.var_empno.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_Contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get("1.0",END),
                            self.var_salary.get()
                            ))   
                    conn.commit()
                    messagebox.showinfo("Success","Employee Added Successfully",parent=self.root)
                    self.clear()                          
                #Call show function after adding new items
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)} in btn add")


    #================= Show function (data in treeview ) ========================
    def show(self):
        conn=sqlite3.connect(database=r"IMS.db")
        cr=conn.cursor()
        try:
            cr.execute("select * from Employee")
            rows=cr.fetchall()
            self.EmloyeeTable.delete(*self.EmloyeeTable.get_children())
            for row in rows:
                self.EmloyeeTable.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


    #================== get data function for when we clicke on the row it gose in entries =========
    def get_data(self,event):
        f=self.EmloyeeTable.focus()
        content=(self.EmloyeeTable.item(f))
        row=content["values"]        
        self.var_empno.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_Contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_address.delete("1.0",END),
        self.txt_address.insert(END,row[9]),
        self.var_salary.set(row[10])


    
    #================= Employee Update =================================                
    def update(self):
        conn=sqlite3.connect(database=r"IMS.db") 
        cr=conn.cursor()

        try:
            if self.var_empno.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cr.execute("Select * From Employee where eid=?",(self.var_empno.get(),))   

                row=cr.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cr.execute("Update Employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",( 
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_Contact.get(),
                                        self.var_dob.get(),
                                        self.var_doj.get(),
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get("1.0",END),
                                        self.var_salary.get(),
                                        self.var_empno.get()
                               ))   
                    conn.commit()
                    messagebox.showinfo("Success","Employee Added Successfully",parent=self.root)                          
                #Call show function after adding new items
                self.clear()#clear fields
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    #================ Employee delete  ==================================
    def delete(self):
        conn=sqlite3.connect(database=r"IMS.db") 
        cr=conn.cursor()

        try:
            if self.var_empno.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cr.execute("Select * From Employee where eid=?",(self.var_empno.get(),))   

                row=cr.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You Really Want to delete")
                    if op==True:
                        cr.execute("delete from Employee where eid=?",(self.var_empno.get()),)
                        messagebox.showinfo("Success","Employee Deleted Successfully")
                        conn.commit()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

        
    #============================  employee clear ===========================
    def clear(self):
        self.var_empno.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select By"),
        self.var_Contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set("Select By"),
        self.txt_address.delete("1.0",END),
        self.var_salary.set("")
        self.var_search_type.set("Select by")
        self.var_txt_search.set("")
        self.show()

#================ search btn ============================
    def search(self):
        conn=sqlite3.connect(database=r"IMS.db")
        cr=conn.cursor()
        try:
            if self.var_search_type.get()=="Select by":
                messagebox.showerror("Error","Select Search By Option ",parent=self.root)
            elif self.var_txt_search.get()=="":
                messagebox.showerror("Error","Search input should be required ",parent=self.root)
            else:
                cr.execute("select * from Employee where "+self.var_search_type.get()+ " LIKE '%"+self.var_txt_search.get()+"%'")
                rows=cr.fetchall()
                if len(rows)!=0:
                    self.EmloyeeTable.delete(*self.EmloyeeTable.get_children())
                    for row in rows:
                        self.EmloyeeTable.insert("",END,values=row)
                else:
                    messagebox.showerror("Error","Not Records Found in Database!!!!!")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


#create obj of Tk() to inherit all the classes of Tk

if __name__=="__main__":
    root=Tk()
    #Create obj for my class IMS
    obj=EmployeeClass(root)
    root.mainloop()