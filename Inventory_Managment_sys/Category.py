from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class CategoryClass:
    global cr,conn
    conn=sqlite3.connect(database=r"IMS.db")
    cr=conn.cursor()

    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Shary")
        self.root.config(bg="White")
        self.root.focus_force()


        self.var_cat_name=StringVar()
        #==================================== Category Title ================================
        Label(self.root,text="Manage Product Category",font="Lucida 20 bold",fg="White",bg="Green",relief=SUNKEN,bd=3).place(x=10,y=20,width=1080,height=50)
        #=============================== Label & Entry ====================
        Label(self.root,text="Enter Category Name",font="Lucida 14 bold",bg="White").place(x=50,y=100)
        txt_cat_name=Entry(self.root,textvariable=self.var_cat_name,font="Arial 14 bold",bg="lightYellow")
        txt_cat_name.place(x=50,y=150,width=300)

        #============================== buttons =========================
        Button(self.root,text="Add",command=self.add,font="Lucida 14 bold",bg="green",fg="White").place(x=360,y=148,width=150,height=30)
        Button(self.root,text="Delete",command=self.delete,font="Lucida 14 bold",bg="red",fg="White").place(x=520,y=148,width=150,height=30)

        #============================= TreeView =============================
        #creating frame
        cat_frame=Frame(self.root,relief=SUNKEN,bd=3)
        cat_frame.place(x=730,y=90,width=350,height=100)

        xscroll=Scrollbar(cat_frame,orient=HORIZONTAL)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll=Scrollbar(cat_frame,orient=VERTICAL)
        yscroll.pack(side=RIGHT,fill=Y)

        self.CategoryTable=ttk.Treeview(cat_frame,columns=("CID","Name"),xscrollcommand=xscroll,yscrollcommand=yscroll)

        xscroll.config(command=self.CategoryTable.xview)
        yscroll.config(command=self.CategoryTable.yview)

        self.CategoryTable.heading("CID",text="CID")
        self.CategoryTable.heading("Name",text="Name")
        self.CategoryTable.pack(fill=BOTH,expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>",self.get_data)

        self.CategoryTable["show"]="headings"
        self.CategoryTable.column("CID",width=100)
        self.CategoryTable.column("Name",width=100)


        #=========================== background images ====================
        # f1=Frame(self.root,relief=SUNKEN,bd=3)
        # f1.place(x=50,y=200,width=500,height=280)
        # f2=Frame(self.root,relief=SUNKEN,bd=3)
        # f2.place(x=580,y=200,width=500,height=280)

        #======================== images =========================
        self.img1=Image.open("images/cat1.png")
        self.img1=self.img1.resize((500,250),Image.BICUBIC)
        self.img1=ImageTk.PhotoImage(self.img1)

        self.lbl=Label(self.root,image=self.img1,relief=RAISED,bd=3)
        self.lbl.place(x=50,y=220)
        
        self.img2=Image.open("images/product4.jpeg")
        self.img2=self.img2.resize((500,250),Image.BICUBIC)
        self.img2=ImageTk.PhotoImage(self.img2)

        self.lbl=Label(self.root,image=self.img2,relief=RAISED,bd=3)
        self.lbl.place(x=580,y=220)
        self.show()

    def add(self):
        try:
            if self.var_cat_name.get()=="":
                messagebox.showerror("Error","Category Name must be required")
            else:
                cr.execute("Select * from Category where Name=?",(self.var_cat_name.get(),))
                row=cr.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already Exist.Try different")
                else:
                    cr.execute("Insert into Category (Name) Values (?)",(self.var_cat_name.get(),))
                    
                    conn.commit()
                    messagebox.showinfo("Success","Category Added Successfully")
                    self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

        
    def show(self):
        try:
            cr.execute("select * from Category")
            rows=cr.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def clear(self):
        self.var_cat_name.set("")
        self.show()

    def get_data(self,event):
        f=self.CategoryTable.focus()
        content=self.CategoryTable.item(f)
        row=content["values"]
        self.var_cat_name.set(row[1])

    def delete(self):
        try:
            if self.var_cat_name.get()=="":
                messagebox.showerror("Error","Category Name must be required")
            else:
                cr.execute("Select * from Category where Name=?",(self.var_cat_name.get(),))
                row=cr.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Category name")
                else:
                    op=messagebox.askyesno("Confirm","Do You Really Want to delete")
                    if op==True:
                        cr.execute("Delete From Category where Name=?",(self.var_cat_name.get(),))
                    
                        conn.commit()
                        messagebox.showinfo("Success","Delete Category Successfully")
                    self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")


if __name__=="__main__":
    root=Tk()
    #Create obj for my class IMS
    obj=CategoryClass(root)
    root.mainloop()