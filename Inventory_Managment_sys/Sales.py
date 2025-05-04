from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
class SalesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Shary")
        self.root.config(bg="White")
        self.root.focus_force()
        #=============== variables ==========================
        self.var_txt_search=StringVar()

        self.bill_list=[]
        #================== Main Label ===================================
        Label(self.root,text="Customer Bill Reports",font="Lucida 20 bold ",bg="DarkBlue",fg="White").pack(side=TOP,fill=X,padx=10,pady=20)

        #====================================== Search btn label txt ===================================
        Label(self.root,text="Invoice No:",font="Lucida 14 bold",bg="white").place(x=50,y=100)
        txt_search=Entry(self.root,textvariable=self.var_txt_search,font="Lucida 14 bold",bg="lightyellow")
        txt_search.place(x=160,y=100,width=180,height=28)
        btn_search=Button(self.root,text="Search",command=self.search,font="Lucida 13 bold",bg="#2196f3",cursor="hand2",fg="white")
        btn_search.place(x=360,y=100,width=120,height=28)
        
        btn_clear=Button(self.root,text="Clear",command=self.clear,font="Lucida 13 bold",bg="lightgrey",cursor="hand2",fg="Black")
        btn_clear.place(x=490,y=100,width=120,height=28)


    #======================== Frame1  ==============================
        sal_frame=Frame (self.root,relief=RIDGE,bd=3)
        sal_frame.place(x=50,y=140,width=200,height=330)

    #==================== scrollbar =================
        scrolly=Scrollbar(sal_frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
    #================= List View ====================
        self.sale_list=Listbox(sal_frame,font="Lucida 14 bold",bg="White",yscrollcommand=scrolly)
        scrolly.config(command=self.sale_list.yview)
        self.sale_list.pack(fill=BOTH,expand=1)
        self.sale_list.bind("<ButtonRelease-1>",self.get_data)
        
    #======================== Frame2 Bill Area  ==============================
        
        bill_frame=Frame (self.root,relief=RIDGE,bd=3)
        bill_frame.place(x=289,y=140,width=410,height=330)
    #================ title bill area ==========================
        Label(bill_frame,text="Customer Bill Area",font="Lucida 20 bold ",bg="Orange").pack(side=TOP,fill=X)
    #==================== scrollbar =================
        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        scrolly2.pack(side=RIGHT,fill=Y)
    #================= List View ====================
        self.bill_area=Text(bill_frame,font="Lucida 14 bold",bg="lightYellow",yscrollcommand=scrolly2)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        


        #============== menue logo ======================    
        self.bill_photo = Image.open(r"images/bill3.jpeg")
        self.bill_photo = self.bill_photo.resize((450, 300),Image.BICUBIC)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)
        #============ label for menue logo ===================
        M_lbl=Label(self.root,image=self.bill_photo,bd=0)
        M_lbl.place(x=700,y=110)

        self.show()
#=========================== Functions ====================================
    def show(self):
        del self.bill_list[:]
        self.sale_list.delete(0,END)
        # print(os.listdir('bill')
        for i in os.listdir('bill'):
            # print( i.split(".")[0])#show the extension
            if i.split(".")[-1]=="txt":
                self.sale_list.insert(END,i)
                self.bill_list.append(i.split('.')[0]) 

    def get_data(self,event):
        index_=self.sale_list.curselection()
        file_name=self.sale_list.get(index_)
        self.bill_area.delete('1.0',END)
        fp=open(f"bill/{file_name}",'r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    #================== search function ======================
        
    def search(self):
        if self.var_txt_search.get()=="":
            messagebox.showerror("Error","Invoice NO. should be required",parent=self.root)
        else:
            if self.var_txt_search.get() in self.bill_list:
                fp=open(f"bill/{self.var_txt_search.get()}.txt",'r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice no")

    def clear(self):
        self.show()
        self.bill_area.delete("1.0",END)

            


if __name__=="__main__":
    root=Tk()
    #Create obj for my class IMS
    obj=SalesClass(root)
    root.mainloop()