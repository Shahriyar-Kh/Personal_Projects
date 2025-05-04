from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class SupplierClass:

    global cr,conn
    conn=sqlite3.connect(database=r"IMS.db")
    cr=conn.cursor()


    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Shary")
        self.root.config(bg="White")
        self.root.focus_force()

        #================== Declare Varaibles ===========================
        self.var_invoiceNo=StringVar()
        self.var_supplierName=StringVar()
        self.var_contact=StringVar()

        self.var_search_type=StringVar()
        self.var_txt_search=StringVar()


        #======== Supplier Details =================================================================================
        Label(self.root,text="Manage Supplier Details",font="Lucida 13 bold ",bg="blue",fg="White").place(x=20,y=10,width=1050,height=30)

        #=========== column 1 labels and Entries ===================
        Label(self.root,text="Invoice No:",font="Lucida 14 bold",bg="white").place(x=20,y=50)
        Label(self.root,text="Supplier Name",font="Lucida 14 bold",bg="white").place(x=20,y=100)
        Label(self.root,text="Contact",font="Lucida 14 bold",bg="white").place(x=20,y=150)
        Label(self.root,text="Description",font="Lucida 14 bold",bg="white").place(x=20,y=200)

        Entry(self.root,textvariable=self.var_invoiceNo,font="Lucida 14 bold",bg="lightyellow").place(x=170,y=50,width=180)
        Entry(self.root,textvariable=self.var_supplierName,font="Lucida 14 bold",bg="lightyellow").place(x=170,y=100,width=180)
        Entry(self.root,textvariable=self.var_contact,font="Lucida 14 bold",bg="lightyellow").place(x=170,y=150,width=180)
        self.txt_desc=Text(self.root,font="Lucida 14 bold",bg="lightyellow")
        self.txt_desc.place(x=170,y=200,width=400,height=120)
        #======================= end of labels and entries =========================================
        #====================== buttons ============================================================
        btn_save=Button(self.root,text="Save",command=self.add,font="Lucida 13 bold",bg="blue",cursor="hand2",fg="white")
        btn_save.place(x=170,y=400,width=100,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font="Lucida 13 bold",bg="green",cursor="hand2",fg="white")
        btn_update.place(x=280,y=400,width=100,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font="Lucida 13 bold",bg="red",cursor="hand2",fg="white")
        btn_delete.place(x=390,y=400,width=100,height=30)
        btn_Clear=Button(self.root,text="Clear",command=self.clear,font="Lucida 13 bold",bg="grey",cursor="hand2",fg="white")
        btn_Clear.place(x=500,y=400,width=100,height=30)
        #============================= end ===============================================================
        #============================= Search lbl combobox button ===============================================================
        search_type=ttk.Combobox(self.root,textvariable=self.var_search_type,values=("Select By","InvoiceNo","Name"),font="Lucida 13 bold")
        search_type.place(x=610,y=50,width=130)
        #current value
        search_type.current(0)

        txt_search=Entry(self.root,textvariable=self.var_txt_search,font="Lucida 14 bold",bg="lightyellow")
        txt_search.place(x=750,y=50,width=170)
        btn_search=Button(self.root,text="Search",command=self.search,font="Lucida 13 bold",bg="#4caf50",cursor="hand2",fg="white")
        btn_search.place(x=930,y=48,width=130,height=30)

        #============= Column2 Treeview  ======================================
        sup_frame=Frame(self.root,bd=3,relief=SUNKEN)
        sup_frame.place(x=640,y=100,width=420,height=330)

        scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly=Scrollbar(sup_frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.SupplierTable=ttk.Treeview(sup_frame,columns=("InvoiceNo","Name","Contact","Description"),yscrollcommand=scrolly,xscrollcommand=scrollx)
        # config the scrollbar on emptable set view
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

   
        self.SupplierTable.heading('InvoiceNo',text='Invoice No')
        self.SupplierTable.heading('Name',text='Name')
        self.SupplierTable.heading('Contact',text='Contact')
        self.SupplierTable.heading('Description',text='Description')
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)


        #================== Column width ===========================
        #using for column start from begining
        self.SupplierTable["show"]="headings"
        self.SupplierTable.column("InvoiceNo",width=100)
        self.SupplierTable.column("Name",width=100)
        self.SupplierTable.column("Contact",width=100)
        self.SupplierTable.column("Description",width=100)

        self.show()

    #======================  Buttons Function =======================================

    def add(self):
        try:
            if self.var_invoiceNo.get()=="":
                messagebox.showerror("Error","Supplier must be required Invoice No")
            else:
                cr.execute("Select * from Supplier where InvoiceNo=?",(self.var_invoiceNo.get(),))
                row=cr.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Invoice No Already Exist!!!")
                else:
                    cr.execute("Insert into Supplier(InvoiceNo,Name,Contact,Description) Values (?,?,?,?)",(
                               self.var_invoiceNo.get(),
                               self.var_supplierName.get(),
                               self.var_contact.get(),
                               self.txt_desc.get("1.0",END)
                               ) )
                    
                    conn.commit()
                    messagebox.showinfo("Success","Supplier Added successfully")
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")
    #================= clear the fields 
    def clear(self):
            self.var_invoiceNo.set(""),
            self.var_supplierName.set(""),
            self.var_contact.set(""),
            self.txt_desc.delete("1.0",END)
            self.var_search_type.set("Select By")
            self.var_txt_search.set("")
            self.show()
    #============================= show Function  ================================================================
    def show(self):
        try:
            #Retrive all records 
            cr.execute("Select * from  Supplier")
            #retreive all rows
            rows=cr.fetchall()
            
            #delete all record from TreeView table
            self.SupplierTable.delete(*self.SupplierTable.get_children())

            for row in rows:
                #insert every row in Treeview table
                self.SupplierTable.insert("",END,values=row)
                

        except Exception as ex:
            messagebox.showerror("Error",f" Error due to {str(ex)}")

    #========================== get_data ==============================
    def get_data(self,event):
        # get the currently focus row in SupplierTable row those data is set on fields
        f=self.SupplierTable.focus()

        #get all information about focus item
        content=(self.SupplierTable.item(f))

        #get the values of the extract row of content
        row=content["values"]

        #set the invoiceNo value to the first element of the row
        self.var_invoiceNo.set(row[0]),
        self.var_supplierName.set(row[1]),
        self.var_contact.set(row[2]),
        self.txt_desc.delete("1.0",END)
        self.txt_desc.insert(END,row[3])

    def update(self):
        try:
            if self.var_invoiceNo.get()=="":
                messagebox.showerror("Error","InvoiceNo must be required")
            else:
                cr.execute("Select * from  Supplier where invoiceNo=?",(self.var_invoiceNo.get(),))
                row=cr.fetchone()

                if row==None:
                    messagebox.showerror("Error","Invalid InvoiceNo")
                else:
                    cr.execute("Update supplier set Name=?,Contact=?,Description=? where InvoiceNo=?",(

                        self.var_supplierName.get(),
                        self.var_contact.get(),
                        self.txt_desc.get("1.0",END),
                        self.var_invoiceNo.get()))
                    conn.commit()
                    messagebox.showinfo("Success","Supplier Update successfully")
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")


    #=========================== Delete function =============================
    def delete(self):
        try:
            if self.var_invoiceNo.get()=="":
                messagebox.showerror("Error","Supplier must be required Invoice No")
            else:
                cr.execute("Select * from Supplier where InvoiceNo=?",(self.var_invoiceNo.get(),))
                row=cr.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No")
                else:
                    op=messagebox.askyesno("Confirm","Do You Really want to delete Record")
                    if op==True:
                        cr.execute("Delete from Supplier where InvoiceNo=?",(self.var_invoiceNo.get(),))
                    
                    conn.commit()
                    messagebox.showinfo("Success","Supplier Delete successfully")
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

    #=========================== search function ===========================
            
    def search(self):
        try:
            if self.var_search_type.get()=="Select By":
                messagebox.showerror("Error","Please Select Option For Searching ")
            elif self.var_txt_search.get()=="":
                messagebox.showerror("Error","Search Input must be required")
            else:
                cr.execute("Select * From supplier where "+ self.var_search_type.get() + " Like '%" + self.var_txt_search.get()+ "%'")
                rows=cr.fetchall()

                if len(rows)!=0:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    for row in rows:
                        self.SupplierTable.insert("",END,values=row)

                else:
                    messagebox.showerror("Error","Not Found Record")
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}")

if __name__=="__main__":
    root=Tk()
    #Create obj for my class IMS
    obj=SupplierClass(root)
    root.mainloop()