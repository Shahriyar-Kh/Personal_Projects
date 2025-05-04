from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
#step 6 import employee class

class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by Shary")
        
        #========= cart list ==============
        self.cart_list=[]
        # Step 1 ===== Title =================================================================================================
        self.title_icon=PhotoImage(file=r"E:\Python_Prac\Ch17_GUI_Tkinter\Inventory_Managment_sys\images\title_icon.png")
        #create Label 1 for Title 
        title=Label(self.root,text="Inventory Management System ",image=self.title_icon,compound=LEFT,font=("Times New Roman",40,"bold"),fg="White",bg="#010c48",padx=20,anchor=W)
        title.place(x=0,y=0,relwidth=1,height=70)
        
        #================ Logout Button ======================
        log_btn=Button(self.root,text="Logout",font=("Times new roman",20,"bold"),bg="Yellow",cursor="hand2").place(x=1150,y=10,width=150,height=50)

        #====== Clock label ==========================
        self.lbl_clock=Label(self.root,text="Welcome Inventory Management System\t\t Date:DD-MM-YYYY\t\t Time:HH-MM-SS",font=("Times New Roman",15),fg="White",bg="#4d636d")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        #=====================================================================================================================

        #====================== product Frame =================================================================
        self.var_txt_search=StringVar()
        product_frame1=Frame(self.root,relief=RIDGE,bd=3,bg="White")
        product_frame1.place(x=6,y=110,width=410,height=550)

        ptitle=Label(product_frame1,text="All Products",font=("gody old style",20,"bold"),bg="#262626",fg="White").pack(side=TOP,fill=X)
        
        product_frame2=Frame(product_frame1,relief=RIDGE,bd=3,bg="White")
        product_frame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(product_frame2,text="Search Product | By Name",font=("Time new roman",15,"bold"),bg="White",fg="green").place(x=2,y=5)

        lbl_name=Label(product_frame2,text="Product Name",font="lucida 13 bold ",bg="White").place(x=2,y=45)

        txt_search=Entry(product_frame2,textvariable=self.var_txt_search,font=("Time new roman",15),bg="lightyellow")
        txt_search.place(x=128,y=47,width=150,height=22 )

        btn_search=Button(product_frame2,text="Search",command=self.search,font="Locida 13 bold",bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(product_frame2,text="Show All",command=self.show,font="Locida 13 bold",bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)

        #============= Product frame 3 Treeview  ======================================
        Product_frame3=Frame(product_frame1,bd=3,relief=RIDGE)
        Product_frame3.place(x=2,y=140,width=398,height=375)

        scrollx=Scrollbar(Product_frame3,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly=Scrollbar(Product_frame3,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.ProductTable=ttk.Treeview(Product_frame3,columns=("pid","Name","price","qty","status"),yscrollcommand=scrolly,xscrollcommand=scrollx)
        # config the scrollbar on emptable set view
        scrollx.config(command=self.ProductTable .xview)
        scrolly.config(command=self.ProductTable .yview)

   
        self.ProductTable .heading('pid',text='PID')
        self.ProductTable .heading('Name',text='Name')
        self.ProductTable .heading('price',text='Price')
        self.ProductTable .heading('qty',text='QTY')
        self.ProductTable .heading('status',text='Status')
        self.ProductTable .pack(fill=BOTH,expand=1)
        self.ProductTable .bind("<ButtonRelease-1>",self.get_data)

        lbl_note=Label(product_frame1,text="Note:'Enter 0 Quantity to remove product from Cart'",font=("gody old style",12),anchor=W,bg="White",fg="red").pack(side=BOTTOM,fill=X)

        #================== Column width ===========================
        #using for column start from begining
        self.ProductTable ["show"]="headings"
        self.ProductTable .column("pid",width=40)
        self.ProductTable .column("Name",width=100)
        self.ProductTable .column("price",width=100)
        self.ProductTable .column("qty",width=50)
        self.ProductTable .column("status",width=90)

    #==================== Customer Frame ==================
        self.var_cust_name=StringVar()
        self.var_cust_contact=StringVar()

        Customer_Frame=Frame(self.root,relief=RIDGE,bd=3,bg="White")
        Customer_Frame.place(x=420,y=110,width=530,height=70)
        ctitle=Label(Customer_Frame,text="Customer Details",font=("gody old style",15),bg="lightgrey").pack(side=TOP,fill=X)

        lbl_name=Label(Customer_Frame,text="Name",font="lucida 13 bold ",bg="White").place(x=5,y=35)
        txt_name=Entry(Customer_Frame,textvariable=self.var_cust_name,font=("Time new roman",15),bg="lightyellow")
        txt_name.place(x=80,y=35,width=180)
       
        lbl_contact=Label(Customer_Frame,text="Contact NO",font="lucida 13 bold ",bg="White").place(x=270,y=35)
        txt_contact=Entry(Customer_Frame,textvariable=self.var_cust_contact,font=("Time new roman",15),bg="lightyellow")
        txt_contact.place(x=380,y=35,width=140)

        #======================= Calculator and Cart Frames ===========================
        Cal_Cart_Frame=Frame(self.root,relief=RIDGE,bd=3,bg="White")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)

        #================= Calculator Frame ======================
        self.var_txt_input=StringVar()

        Cal_Frame=Frame(Cal_Cart_Frame,relief=RIDGE,bd=9,bg="White")
        Cal_Frame.place(x=5,y=10,width=268,height=340)

        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_txt_input,font="Arial 15 bold",state="readonly",width=21,bd=10,relief=GROOVE,justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        
        #=========== calculator Buttons ================
        btn_7=Button(Cal_Frame,text="7",font="Arail 15 bold",command=lambda:self.get_input(7),bd=5,width=4,pady=11,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text="8",font="Arail 15 bold",command=lambda:self.get_input(8),bd=5,width=4,pady=11,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text="9",font="Arail 15 bold",command=lambda:self.get_input(9),bd=5,width=4,pady=11,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text="+",font="Arail 15 bold",command=lambda:self.get_input("+"),bd=5,width=4,pady=11,cursor="hand2").grid(row=1,column=3)
        
        btn_4=Button(Cal_Frame,text="4",font="Arail 15 bold",command=lambda:self.get_input(4),bd=5,width=4,pady=11,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text="5",font="Arail 15 bold",command=lambda:self.get_input(5),bd=5,width=4,pady=11,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text="6",font="Arail 15 bold",command=lambda:self.get_input(6),bd=5,width=4,pady=11,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text="-",font="Arail 15 bold",command=lambda:self.get_input("-"),bd=5,width=4,pady=11,cursor="hand2").grid(row=2,column=3)
        
        btn_1=Button(Cal_Frame,text="1",font="Arail 15 bold",command=lambda:self.get_input(1),bd=5,width=4,pady=11,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text="2",font="Arail 15 bold",command=lambda:self.get_input(2),bd=5,width=4,pady=11,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text="3",font="Arail 15 bold",command=lambda:self.get_input(3),bd=5,width=4,pady=11,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text="*",font="Arail 15 bold",command=lambda:self.get_input("*"),bd=5,width=4,pady=11,cursor="hand2").grid(row=3,column=3)
       
        btn_0=Button(Cal_Frame,text="0",font="Arail 15 bold",command=lambda:self.get_input(0),bd=5,width=4,pady=12,cursor="hand2").grid(row=4,column=0)
        btn_C=Button(Cal_Frame,text="C",font="Arail 15 bold",command=self.clear_cal,bd=5,width=4,pady=12,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text="=",font="Arail 15 bold",command=self.perform_cal,bd=5,width=4,pady=12,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text="/",font="Arail 15 bold",command=lambda:self.get_input("/"),bd=5,width=4,pady=12,cursor="hand2").grid(row=4,column=3)

        #============== Cart Frame ==========================
        Cart_Frame=Frame(Cal_Cart_Frame,relief=RIDGE,bd=3,bg="White")
        Cart_Frame.place(x=280,y=8,width=245,height=342)

        self.carttitle=Label(Cart_Frame,text="Cart\tTotal Products:[0]",font=("gody old style",15),bg="lightgrey")
        self.carttitle.pack(side=TOP,fill=X)

        scrollx=Scrollbar(Cart_Frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly=Scrollbar(Cart_Frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.CartTable =ttk.Treeview(Cart_Frame,columns=("pid","Name","price","qty","status"),yscrollcommand=scrolly,xscrollcommand=scrollx)
        # config the scrollbar on emptable set view
        scrollx.config(command=self.CartTable .xview)
        scrolly.config(command=self.CartTable .yview)

   
        self.CartTable .heading('pid',text='PID')
        self.CartTable .heading('Name',text='Name')
        self.CartTable .heading('price',text='Price')
        self.CartTable .heading('qty',text='QTY')
        self.CartTable .heading('status',text='Status')
        self.CartTable .pack(fill=BOTH,expand=1)
        # self.CartTable .bind("<ButtonRelease-1>",self.get_data)

                #using for column start from begining
        self.CartTable ["show"]="headings"
        self.CartTable .column("pid",width=40)
        self.CartTable .column("Name",width=100)
        self.CartTable .column("price",width=90)
        self.CartTable .column("qty",width=40)
        self.CartTable .column("status",width=90)
 
    # ================= Add cart buttons =============================
        self.var_pid=StringVar()
        self.var_p_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
   
        Cart_buttons_f=Frame(self.root,relief=RIDGE,bd=3,bg="White")
        Cart_buttons_f.place(x=420,y=550,width=530,height=110)

        p_name=Label(Cart_buttons_f,text="Product Name",font=("Time new roman",15),bg="white").place(x=5,y=5)
        p_name_entry=Entry(Cart_buttons_f,textvariable=self.var_pid ,font=("Time new roman",15),bg="lightyellow",state="readonly").place(x=5,y=35,width=190,height=22)

        p_price=Label(Cart_buttons_f,text="Price per Qty",font=("Time new roman",15),bg="white").place(x=230,y=5)
        p_price_entry=Entry(Cart_buttons_f,textvariable=self.var_price ,font=("Time new roman",15),bg="lightyellow",state="readonly").place(x=230,y=35,width=150,height=22)

        p_price=Label(Cart_buttons_f,text="Quantity",font=("Time new roman",15),bg="white").place(x=390,y=5)
        p_price_entry=Entry(Cart_buttons_f,textvariable=self.var_qty ,font=("Time new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.p_stock=Label(Cart_buttons_f,text="In stock[9999]",font=("Time new roman",15),bg="white")
        self.p_stock.place(x=5,y=70)

        btn_clear_cart=Button(Cart_buttons_f,text="Clear",font=("Time new roman",15),bg="lightgrey",cursor="hand2").place(x=180,y=70,width=150,height=30)

        btn_add_cart=Button(Cart_buttons_f,text="Add/Update Cart",command=self.add_update_cart,font=("Time new roman",15),bg="Orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
        
    #======================== Column3 Billing Area Frame =============================
        bill_area_frame=Frame(self.root,relief=RIDGE,bd=3,bg="White")
        bill_area_frame.place(x=953,y=110,width=410,height=410)

        btitle=Label(bill_area_frame,text="Customer Bill Area",font=("gody old style",20,"bold"),bg="#F44336",fg="White").pack(side=TOP,fill=X)

        scrolly=Scrollbar(bill_area_frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area=Text(bill_area_frame,yscrollcommand=scrolly.set)
        scrolly.config(command=self.txt_bill_area.yview)
        self.txt_bill_area.pack(fill=BOTH,expand=1)

    #===================== Billing Buttons =========================
        bill_menue_frame=Frame(self.root,relief=RIDGE,bd=3,bg="White")
        bill_menue_frame.place(x=953,y=520,width=410,height=140)

        self.lbl_amnt=Label(bill_menue_frame,text="Bill Amount\n[0]",font=("gody old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=120,height=70)

        self.lbl_discount=Label(bill_menue_frame,text="Discount\n[5%]",font=("gody old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_netpay=Label(bill_menue_frame,text="Net Pay\n[0]",font=("gody old style",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_netpay.place(x=246,y=5,width=160,height=70)
        
        btn_print=Button(bill_menue_frame,text="Print",font=("Lucida 13 bold"),bg="lightgreen",cursor="hand2",fg="white")
        btn_print.place(x=2,y=80,width=120,height=50)

        btn_clear_all=Button(bill_menue_frame,text="Clear All",font=("Lucida 13 bold"),bg="grey",cursor="hand2",fg="white")
        btn_clear_all.place(x=124,y=80,width=120,height=50)

        btn_generate=Button(bill_menue_frame,text="Generate/Save Bill",font=("Lucida 13 bold"),bg="#009688",cursor="hand2",fg="white")
        btn_generate.place(x=246,y=80,width=160,height=50)

        #====== Footer ==========================
        Label(self.root,text="IMS-Inventory Management System | Develop by Shary\n For any Technical issue Contact 03110924560",font=("Times New Roman",12),fg="White",bg="#4d636d").pack(side=BOTTOM,fill=X)
        

        self.show()




#========================= All functions ======================================================
    #========= Calculator functions ======================
    def get_input(self,num):
        xnum=self.var_txt_input.get()+str(num)
        self.var_txt_input.set(xnum)
    def clear_cal(self):
        self.var_txt_input.set('')

    def perform_cal(self):
        result=self.var_txt_input.get()
        self.var_txt_input.set(eval(result))# eval is function which is used for perform arithmetic operations

    #================= function for product Frame ====================
        #================= Show function (data in treeview ) ========================
    def show(self):
        conn=sqlite3.connect(database=r"IMS.db")
        cr=conn.cursor()
        try:
            cr.execute("select pid,Name,price,qty,status from Product")
            rows=cr.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    #================ search btn ============================
    def search(self):
        conn=sqlite3.connect(database=r"IMS.db")
        cr=conn.cursor()
        try:
            if self.var_txt_search.get()=="":
                messagebox.showerror("Error","Search input should be required ",parent=self.root)
            else:
                cr.execute("select pid,Name,price,qty,status from Product where  Name LIKE '%" +self.var_txt_search.get()+"%'")
                rows=cr.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert("",END,values=row)
                else:
                    messagebox.showerror("Error","Not Records Found in Database!!!!!")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
    
     #================== get data function for when we clicke on the row it gose in entries =========
    def get_data(self,event):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content["values"]
        self.var_pid.set(row[0])
        self.var_p_name.set(row[1])
        self.var_price.set(row[2])
        self.p_stock.config(text=f"In Stock [{str(row[3])}]")

    #================ Add/update Cart =================
    def add_update_cart(self):
        if self.var_pid.get()=="":
            messagebox.showerror("Error","Please Select Product from the List")
        elif self.var_qty.get()=="":
            messagebox.showerror("Error","Quantity is Required")
        else:
            price_cal=(int(self.var_qty.get())*float(self.var_price.get()))
            price_cal=float(price_cal)
            
            cart_data=[self.var_pid.get(),self.var_p_name.get(),price_cal,self.var_qty.get()]

            #============= update cart ================
            present="no"
            index=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index+=1
            if present=='yes':
                op=messagebox.askyesno("Confirm","Product already present \n Do you want to Update|Remove From the Cart List",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index)
                    else:
                        self.cart_list[index][2]=price_cal #price
                        self.cart_list[index][3]=self.var_qty.get()#qty
            else:
                self.cart_list.append(cart_data)
            self.show_cart()# this show add data in the cart
            self.bill_update()


    #================== Bill Updates =======================
    def bill_update(self):
        bill_amnt=0
        net_pay=0
        for row in self.cart_list:
            bill_amnt=bill_amnt+float(row[2])
        net_pay=bill_amnt-((bill_amnt*5)/100)

        self.lbl_amnt.config(text=f"Bill Amount\n{str(bill_amnt)}")
        self.lbl_netpay.config(text=f"Ney Pay\n{str(net_pay)}")
        self.carttitle.config(text=f"Cart\tTotal Products[{str(len(self.cart_list))}")
    #========= show function for CartTable =================        
    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")




if __name__=="__main__":
    #create obj of Tk() to inherit all the classes of Tk
    root=Tk()
    #Create obj for my class IMS
    obj=BillClass(root)
    root.mainloop()