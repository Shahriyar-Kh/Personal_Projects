import sqlite3
from tkinter import*
from PIL import Image,ImageTk
#step 6 import employee class
from Employee import EmployeeClass
from Supplier import SupplierClass
from Category import CategoryClass
from Product import ProductClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by Shary")

        # Step 1 ===== Title =================================================================================================
        self.title_icon=PhotoImage(file=r"D:\python WORK\Python_Prac\Ch17_GUI\Tkinter\Inventory_Managment_sys\images\title_icon.png")
        #create Label 1 for Title 
        title=Label(self.root,text="Inventory Management System ",image=self.title_icon,compound=LEFT,font=("Times New Roman",40,"bold"),fg="White",bg="#010c48",padx=20,anchor=W)
        title.place(x=0,y=0,relwidth=1,height=70)
        
        #================ Logout Button ======================
        log_btn=Button(self.root,text="Logout",font=("Times new roman",20,"bold"),bg="Yellow",cursor="hand2").place(x=1150,y=10,width=150,height=50)

        #====== Clock label ==========================
        self.lbl_clock=Label(self.root,text="Welcome Inventory Management System\t\t Date:DD-MM-YYYY\t\t Time:HH-MM-SS",font=("Times New Roman",15),fg="White",bg="#4d636d")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        #=====================================================================================================================

        #Step 2 ======= Left Menue ============================================================================================
        
        #============== menue Frame=====================
        left_M=Frame(self.root,bg="White",relief=SUNKEN,bd=2)
        left_M.place(x=0,y=100,width=200,height=580)

        #============== menue logo ======================    
        self.menu_logo = Image.open(r"D:\python WORK\Python_Prac\Ch17_GUI\Tkinter\Inventory_Managment_sys\images\menuelogo1.PNG")
        self.menu_logo = self.menu_logo.resize((200, 200),Image.BICUBIC)
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)
        #============ label for menue logo ===================
        M_lbl=Label(left_M,image=self.menu_logo)
        M_lbl.pack(side=TOP,fill=X)
        #===== label for menue =============
        lbl=Label(left_M,text="Menue",font=("Times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        
        #============= Buttons ===========================
        self.btn_icon=PhotoImage(file=r"D:\python WORK\Python_Prac\Ch17_GUI\Tkinter\Inventory_Managment_sys\images\side1.png")

        btn_emp=Button(left_M,text="Employee",image=self.btn_icon,compound=LEFT,command=self.employee,font=("Times new roman",20,"bold"),bg="White",bd=3,cursor="hand2",anchor=W)
        btn_emp.pack(side=TOP,fill=X)

        btn_Sup=Button(left_M,text="Supplier",command=self.Supplier,image=self.btn_icon,compound=LEFT,font=("Times new roman",20,"bold"),bg="White",bd=3,cursor="hand2",anchor=W)
        btn_Sup.pack(side=TOP,fill=X)

        btn_cat=Button(left_M,text="Category",command=self.category,image=self.btn_icon,compound=LEFT,font=("Times new roman",20,"bold"),bg="White",bd=3,cursor="hand2",anchor=W)
        btn_cat.pack(side=TOP,fill=X)

        btn_Prod=Button(left_M,text="Products",command=self.product,image=self.btn_icon,compound=LEFT,font=("Times new roman",20,"bold"),bg="White",bd=3,cursor="hand2",anchor=W)
        btn_Prod.pack(side=TOP,fill=X)
        
        btn_sales=Button(left_M,text="Sales",command=self.sales,image=self.btn_icon,compound=LEFT,font=("Times new roman",20,"bold"),bg="White",bd=3,cursor="hand2",anchor=W)
        btn_sales.pack(side=TOP,fill=X)
        
        btn_exit=Button(left_M,text="Exit",image=self.btn_icon,compound=LEFT,font=("Times new roman",20,"bold"),bg="White",bd=3,cursor="hand2",anchor=W)
        btn_exit.pack(side=TOP,fill=X)
        #================== end menue ==============================================================================================================

        #Step3=============== Content ============================================================================================================== 
        self.lbl_emp=Label(self.root,text="Total Employee\n[0]",font=("gody old style",20,"bold"),fg="White",bg="#33bbf9",relief=SUNKEN,bd=5)
        self.lbl_emp.place(x=300,y=120,width=300,height=150)

        self.lbl_emp=Label(self.root,text="Total Supplier\n[0]",font=("gody old style",20,"bold"),fg="White",bg="#ff5722",relief=SUNKEN,bd=5)
        self.lbl_emp.place(x=650,y=120,width=300,height=150)
        
        self.lbl_emp=Label(self.root,text="Total Category\n[0]",font=("gody old style",20,"bold"),fg="White",bg="#009688",relief=SUNKEN,bd=5)
        self.lbl_emp.place(x=1000,y=120,width=300,height=150)
        
        self.lbl_emp=Label(self.root,text="Total Product\n[0]",font=("gody old style",20,"bold"),fg="White",bg="#607d8b",relief=SUNKEN,bd=5)
        self.lbl_emp.place(x=300,y=300,width=300,height=150)
        
        self.lbl_emp=Label(self.root,text="Total Sales\n[0]",font=("gody old style",20,"bold"),fg="White",bg="#ffc107",relief=SUNKEN,bd=5)
        self.lbl_emp.place(x=650,y=300,width=300,height=150)
        #step 4  ====== Footer ==========================
        Label(self.root,text="IMS-Inventory Management System | Develop by Shary\t For any Technical issue Contact 03110924560",font=("Times New Roman",12),fg="White",bg="#4d636d").pack(side=BOTTOM,fill=X)
        

    # step 6 =========== Create employee function for btn_empl ==================================================
    def employee(self):
        self.employee_root=Toplevel(self.root)
        #create new obj and pass the new window to employee class
        self.new_obj=EmployeeClass(self.employee_root)

    def Supplier(self):
        self.supplier_window=Toplevel(self.root)
        self.new_obj2=SupplierClass(self.supplier_window)

    def category(self):
        self.category_wind=Toplevel(self.root)
        self.cat_obj=CategoryClass(self.category_wind)

    def product(self):
        self.product_wind=Toplevel(self.root)
        self.prod_obj=ProductClass(self.product_wind)

    def sales(self):
        self.sales_wind=Toplevel(self.root)
        self.sales_obj=SalesClass(self.sales_wind)




if __name__=="__main__":
    #create obj of Tk() to inherit all the classes of Tk
    root=Tk()

    #Create obj for my class IMS
    obj=IMS(root)

    root.mainloop()