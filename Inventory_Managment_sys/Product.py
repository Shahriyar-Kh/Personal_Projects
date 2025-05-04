from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class ProductClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Shary")
        self.root.config(bg="White")
        self.root.focus_force()

        #============================= all variables ====================================================
        self.var_pid=StringVar()
        self.var_cat_type=StringVar()
        self.var_sup_type=StringVar()
        self.var_Name=StringVar()
        self.var_Price=IntVar()
        self.var_QTY=IntVar()
        self.var_stat_type=StringVar()

        # ============ search var ===============
        self.var_search_type=StringVar()
        self.var_txt_search=StringVar()

        #================= lists ================
        self.cat_list=[]
        self.sup_list=[]
        self.cat_sup()

        #========================   frame 1     ===============================
        mpd=Frame(self.root,relief=SUNKEN,bd=3,bg="white")
        mpd.place(x=10,y=10,width=450,height=480)

        #================== Columns 1 Labels ===================================
        Label(mpd,text="Manage Product Details",font="Lucida 13 bold ",bg="#0b45b2",fg="White").pack(side=TOP,fill=X)


        Label(mpd,text="Category",font="Lucida 14 bold",bg="white").place(x=30,y=60)
        Label(mpd,text="Supplier",font="Lucida 14 bold",bg="white").place(x=30,y=110)
        Label(mpd,text="Name",font="Lucida 14 bold",bg="white").place(x=30,y=160)
        Label(mpd,text="Price",font="Lucida 14 bold",bg="white").place(x=30,y=210)
        Label(mpd,text="QTY",font="Lucida 14 bold",bg="white").place(x=30,y=260)
        Label(mpd,text="Status",font="Lucida 14 bold",bg="white").place(x=30,y=310)
        #===========  Column 2 cambobox ===================================
        cat_type=ttk.Combobox(mpd,textvariable=self.var_cat_type,values=self.cat_list,state="readonly",justify=CENTER,font="Lucida 13 bold")
        cat_type.place(x=150,y=60,width=200)
        cat_type.current(0)


        sup_type=ttk.Combobox(mpd,textvariable=self.var_sup_type,values=self.sup_list,state="readonly",justify=CENTER,font="Lucida 13 bold")
        sup_type.place(x=150,y=110,width=200)
        sup_type.current(0)
        Entry(mpd,textvariable=self.var_Name,font="Lucida 14 bold",bg="lightyellow").place(x=150,y=160,width=200)

        Entry(mpd,textvariable=self.var_Price,font="Lucida 14 bold",bg="lightyellow").place(x=150,y=210,width=200)
        self.var_Price.set("")
        Entry(mpd,textvariable=self.var_QTY,font="Lucida 14 bold",bg="lightyellow").place(x=150,y=260,width=200)
        self.var_QTY.set(" ")
        s_type=ttk.Combobox(mpd,textvariable=self.var_stat_type,values=(("Active","InActive")),state="readonly",justify=CENTER,font="Lucida 13 bold")
        s_type.place(x=150,y=310,width=200)
        s_type.current(0)


        #================== buttons ================================
        btn_save=Button(mpd,text="Save",command=self.add,font="Lucida 13 bold",bg="blue",cursor="hand2",fg="white")
        btn_save.place(x=10,y=400,width=100,height=40)
        btn_update=Button(mpd,text="Update",command=self.update,font="Lucida 13 bold",bg="green",cursor="hand2",fg="white")
        btn_update.place(x=120,y=400,width=100,height=40)
        btn_delete=Button(mpd,text="Delete",command=self.delete,font="Lucida 13 bold",bg="red",cursor="hand2",fg="white")
        btn_delete.place(x=230,y=400,width=100,height=40)
        btn_Clear=Button(mpd,text="Clear",command=self.clear,font="Lucida 13 bold",bg="grey",cursor="hand2",fg="white")
        btn_Clear.place(x=340,y=400,width=100,height=40)
        #============================= end ===============================================================

        
        #=========== search Product fram =======================================================================
        search_prod=LabelFrame(self.root,text="Search Product",font=("gody old style",12,"bold"),bg="White",relief=SUNKEN,bd=2)
        search_prod.place(x=480,y=10,width=600,height=70)

        #=========== cambobox ================
        search_type=ttk.Combobox(search_prod,textvariable=self.var_search_type,values=(("Select by","Category","Supplier","Name")),state="readonly",justify=CENTER,font="Lucida 13 bold")
        search_type.place(x=10,y=10,width=180)
        #also 
        search_type.current(0)
        # cmb_search.set("Select by")

        #========== Search Entry and button ==============
        txt_search=Entry(search_prod,textvariable=self.var_txt_search,font="Lucida 14 bold",bg="lightyellow")
        txt_search.place(x=200,y=10)
        btn_search=Button(search_prod,text="Search",command=self.search,font="Lucida 13 bold",bg="#4caf50",cursor="hand2",fg="white")
        btn_search.place(x=430,y=9,width=130,height=30)
        #======================== end search frame ========================================================================


        #====================== Product Fram db Details ======================================================
        prod_frame=Frame(self.root,bd=3,relief=SUNKEN)
        prod_frame.place(x=480,y=100,width=600,height=390)

        #================== scrolling ==============================
        scolly=Scrollbar(prod_frame,orient=VERTICAL)
        scollx=Scrollbar(prod_frame,orient=HORIZONTAL)
        scolly.pack(side=RIGHT,fill=Y)
        scollx.pack(side=BOTTOM,fill=X)

        #============= Columns Headings  ======================================
        self.ProductTable=ttk.Treeview(prod_frame,columns=("pid","Category",'Supplier',"Name",'Price','QTY','Status'),yscrollcommand=scolly.set,xscrollcommand=scollx.set)
        # config the scrollbar on emptable set view
        scollx.config(command=self.ProductTable.xview)
        scolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading('pid',text='P ID')
        self.ProductTable.heading('Category',text='Category')
        self.ProductTable.heading('Supplier',text='Supplier')
        self.ProductTable.heading('Name',text='Name')
        self.ProductTable.heading('Price',text='Price')
        self.ProductTable.heading('QTY',text='QTY')
        self.ProductTable.heading('Status',text="Status")

        self.ProductTable.pack(fill=BOTH,expand=1)

        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)

        #using for column start from beginning
        self.ProductTable["show"]="headings"
        self.show()
        
        #========================== set Column width =========================
        self.ProductTable.column('pid',width=80)
        self.ProductTable.column('Category',width=80)
        self.ProductTable.column('Supplier',width=80)
        self.ProductTable.column('Name',width=80)
        self.ProductTable.column('Price',width=80)
        self.ProductTable.column('QTY',width=80)
        self.ProductTable.column('Status',width=80)


        #Call show function after running the program
        #=================== end Product frame =================================================================

    #======================= fetch Category and Supplier =======================
    def cat_sup(self):
        conn=sqlite3.connect(database=r"IMS.db") 
        cr=conn.cursor()

        try:
            self.cat_list.append("Empty")
            self.sup_list.append("Empty")

            cr.execute("select  Name from Category ")
            cat=cr.fetchall()
            if len(cat)>=0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cr.execute("select  Name from Supplier ")
            sup=cr.fetchall()
            if len(sup)>=0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

#step 10  Product buttons functions ================================================================================================================
        

    def add(self):
        conn=sqlite3.connect(database=r"IMS.db") 
        cr=conn.cursor()

        try:
            if self.var_cat_type.get()=="Select By"  or self.var_cat_type.get()=="Empty" or self.var_sup_type.get()=="Select By" or self.var_stat_type.get()=="Select By": #when id field empty show message
                messagebox.showerror("Error","All Fields are Required ",parent=self.root)
            else:
                #executing the query to check the emplyee of the given id 
                cr.execute("Select * From Product where Name=?",(self.var_Name.get(),))
                #retrive the Products of the given id   
                row=cr.fetchone()
                if row!=None: #when row is not empty means there already this Product
                    messagebox.showerror("Error","This Product already Present,try different",parent=self.root)
                else:
                    cr.execute("insert into Product(Category,Supplier,Name,Price,QTY,Status) values (?,?,?,?,?,?)",( 
                            self.var_cat_type.get(),
                            self.var_sup_type.get(),
                            self.var_Name.get(),
                            self.var_Price.get(),
                            self.var_QTY.get(),
                            self.var_stat_type.get()
 
                            ))   
                    conn.commit()
                    messagebox.showinfo("Success","Product Added Successfully",parent=self.root)
                    self.clear()                          
                #Call show function after adding new items
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


    #================= Show function (data in treeview ) ========================
    def show(self):
        conn=sqlite3.connect(database=r"IMS.db")
        cr=conn.cursor()
        try:
            cr.execute("select * from Product")
            rows=cr.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


    #================== get data function for when we clicke on the row it gose in entries =========
    def get_data(self,event):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content["values"]        
        self.var_pid.set(row[0]),
        self.var_cat_type.set(row[1]),
        self.var_sup_type.set(row[2]),
        self.var_Name.set(row[3]),
        self.var_Price.set(row[4]),
        self.var_QTY.set(row[5]),
        self.var_stat_type.set(row[6])



    
    #================= Product Update =================================                
    def update(self):
        conn=sqlite3.connect(database=r"IMS.db") 
        cr=conn.cursor()

        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select Product from list",parent=self.root)
            else:
                cr.execute("Select * From Product where pid=?",(self.var_pid.get(),))   

                row=cr.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    cr.execute("Update Product set Category=?,Supplier=?,Name=?,Price=?,QTY=?,Status=? where pid=?",( 
                                        self.var_cat_type.get(),
                                        self.var_sup_type.get(),
                                        self.var_Name.get(),
                                        self.var_Price.get(),
                                        self.var_QTY.get(),
                                        self.var_stat_type.get(),
                                        self.var_pid.get()
                               ))   
                    conn.commit()
                    messagebox.showinfo("Success","Product Update Successfully",parent=self.root)                          
                #Call show function after adding new items
                self.clear()#clear fields
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    #================ Product delete  ==================================
    def delete(self):
        conn=sqlite3.connect(database=r"IMS.db") 
        cr=conn.cursor()

        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select Product from list",parent=self.root)
            else:
                cr.execute("Select * From Product where pid=?",(self.var_pid.get(),))   

                row=cr.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You Really Want to delete")
                    if op==True:
                        cr.execute("delete from Product where pid=?",(self.var_pid.get(),))
                        messagebox.showinfo("Success","Product Deleted Successfully")
                        conn.commit()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

        
    #============================  Product clear ===========================
    def clear(self):
        self.var_cat_type.set("Select By"),
        self.var_sup_type.set("Select By"),
        self.var_Name.set(""),
        self.var_Price.set(""),
        self.var_QTY.set(""),
        self.var_stat_type.set("Active"),
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
                cr.execute("select * from Product where "+self.var_search_type.get()+ " LIKE '%"+self.var_txt_search.get()+"%'")
                rows=cr.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert("",END,values=row)
                else:
                    messagebox.showerror("Error","Not Records Found in Database!!!!!")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")




if __name__=="__main__":
    root=Tk()
    #Create obj for my class IMS
    obj=ProductClass(root)
    root.mainloop()