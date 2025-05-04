#step 9 ============================== Creating db ======================================
import sqlite3

def db():
    #create or access db
    conn=sqlite3.connect(database=r"IMS.db")
    #create curser obj
    cr=conn.cursor()

    #Create table
    cr.execute("""CREATE TABLE IF NOT EXISTS Employee(
               eid INTEGER PRIMARY KEY AUTOINCREMENT,
               name Text,
               email Text,
               gender Text,
               contact Text,
               dob Text,
               doj Text,
               pass Text,
               utype Text,
               address Text,
               salary Text)
               """)
    cr.execute(""" Create Table If Not Exists Supplier(
               InvoiceNo INTEGER PRIMARY KEY AUTOINCREMENT,
               Name Text,
               Contact Text,
               Description Text
               )
                """)
    cr.execute(" Create Table if not Exists Category (CID Integer Primary key AUTOINCREMENT,Name Text)")

    cr.execute(""" Create Table If Not Exists Product(
               pid INTEGER PRIMARY KEY AUTOINCREMENT,
               Category Text,
               Supplier Text,
               Name Text,
               Price INTEGER,
               QTY INTEGER,
               Status Text
               )
                """)
   
    conn.commit()

db()