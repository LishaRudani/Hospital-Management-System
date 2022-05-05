from cProfile import label
from cgitb import text
from logging import root
from multiprocessing.sharedctypes import Value
from optparse import Values
from textwrap import fill
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from tkinter.font import BOLD
from tokenize import String
from turtle import heading
import mysql.connector



class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
     
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Nameoftablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()    
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.furtherInformation=StringVar()
        self.storageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font="times new roman",)
        lbltitle.pack(side=TOP,fill=X)
        
        # ============================Dataframe=============================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                 font=("arial",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)
        
        DataframeRight=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                 font=("arial",12,"bold"),text="Prescription")
        DataframeLeft.place(x=990,y=5,width=460,height=350)
        
        # ==========================button frame=======================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        #=======================Details Frame=========================
        Detailsframe=Frame(self.root ,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        
        #======================DataframeLeft=========================
        
        lblNameTablet=Label(DataframeLeft,text="Name of Tablet",font=("times new roman",12,"bold"),
        padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        
        comNametablet=ttk.Combobox(DataframeLeft,txtvariable=self.Nameoftablets,state="readonly",font=("times new roman",12,"bold"),
                                                                                    width=33)
        comNametablet["values"]=("nice","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)
        
        lblref=Label(DataframeLeft,txtvariable=self.ref,font=("arial",12,"bold"),text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)
        
        
        lblDose=Label(DataframeLeft,txtvariable=self.Dose,font=("arial",12,"bold"),text="Dose:",padx=2,pady=2)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)
        
        lblNoOftablets=Label(DataframeLeft,txtvariable=self.Nameoftablets,font=("arial",12,"bold"),text="No.of tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        lblLot=Label(DataframeLeft,txtvariable=self.Lot,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtLot.grid(row=4,column=1)
        
        
        lblIssueDate=Label(DataframeLeft,txtvariable=self.Issuedate,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtIssueDate.grid(row=5,column=1)
        
        lblExpDate=Label(DataframeLeft,txtvariable=self.ExpDate,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)
        
        lblDailyDose=Label(DataframeLeft,txtvariable=self.DailyDose,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)
        
        lblSideEffects=Label(DataframeLeft,txtvariable=self.sideeffectsfont=("arial",12,"bold"),text="Side Effects:",padx=2,pady=6)
        lblSideEffects.grid(row=8,column=0,sticky=W)
        txtSideEffects=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtSideEffects.grid(row=8,column=1)
        
        lblNoOftablets=Label(DataframeLeft,txtvariable=self.Nameoftablets,font=("arial",12,"bold"),text="No.of tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        lblFurtherInformation=Label(DataframeLeft,txtvariable=self.furtherInformation,font=("arial",12,"bold"),text="Further Information",padx=2,pady=6)
        lblFurtherInformation.grid(row=3,column=0,sticky=W)
        txtFurtherInformation=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtFurtherInformation.grid(row=3,column=1)
        
        lblBloodPressure=Label(DataframeLeft,txtvariable=self.BloodPressure,font=("arial",12,"bold"),text="Blood Pressure",padx=2,pady=6)
        lblBloodPressure.grid(row=3,column=0,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtBloodPressure.grid(row=3,column=1)
        
        lblStorageAdvice=Label(DataframeLeft,txtvariable=self.storageAdvice,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorageAdvice.grid(row=3,column=0,sticky=W)
        txtStorageAdvice=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtStorageAdvice.grid(row=3,column=1)
        
        lblMedication=Label(DataframeLeft,txtvariable=self.Medication,font=("arial",12,"bold"),text="Medication",padx=2,pady=6)
        lblMedication.grid(row=3,column=0,sticky=W)
        txtMedication=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtMedication.grid(row=3,column=1)
        
        lblPatientId=Label(DataframeLeft,txtvariable=self.PatientId,font=("arial",12,"bold"),text="Patient Id",padx=2,pady=6)
        lblPatientId.grid(row=3,column=0,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtPatientId.grid(row=3,column=1)
        
        lblNHSNumber=Label(DataframeLeft,txtvariable=self.nhsNumber,font=("arial",12,"bold"),text="NHS Number",padx=2,pady=6)
        lblNHSNumber.grid(row=3,column=0,sticky=W)
        txtNHSNumber=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtNHSNumber.grid(row=3,column=1)
        
        lblPatientName=Label(DataframeLeft,txtvariable=self.PatientName,font=("arial",12,"bold"),text="Patient Name",padx=2,pady=6)
        lblPatientName.grid(row=3,column=0,sticky=W)
        txtPatientName=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtPatientName.grid(row=3,column=1)
        
        lblDateOfBirth=Label(DataframeLeft,txtvariable=self.DateOfBirth,font=("arial",12,"bold"),text="Date Of Birth",padx=2,pady=6)
        lblDateOfBirth.grid(row=3,column=0,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtDateOfBirth.grid(row=3,column=1)
        
        lblPatientAddress=Label(DataframeLeft,txtvariable=self.PatientAddress,font=("arial",12,"bold"),text="Patient Address",padx=2,pady=6)
        lblPatientAddress.grid(row=3,column=0,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtPatientAddress.grid(row=3,column=1)
        
        # =============================DataFrameRight=========================
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
        
        # ===============================Button=================================
        btnprescription=Button(Buttonframe,command=self.iprescription,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        btnprescription.grid(row=0,column=0)
        
        btnprescriptionData=Button(Buttonframe,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        btnprescriptionData.grid(row=0,column=1)
        
        btnupdate=Button(Buttonframe,command=self.update_data,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        btnupdate.grid(row=0,column=2)
        
        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)
        
        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        btnClear.grid(row=0,column=4)
        
        btnClear=Button(Buttonframe,command=self.iExit,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        btnClear.grid(row=0,column=5)
        
        # ===========================Table================================================
        # ============================Scrollbar===========================================
        
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftables","ref","Dose","nooftables","lot","issuesdate",
                                                               "Issue Date","Exp Date","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        
        scroll_x.pack= (side=BUTTOM,fill=X)
        scroll_y.pack= (side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftable",text="Name Of Table")
        self.hospital_table.heading("ref",text="Referance No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No. Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("exp date",text="Exp Date")
        self.hospital_table.heading("daily dose",text="Daily Date")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        
        self.hospital_table["show"]="headings"
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)  
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
        # ==========================Functinality Declaration=========================
        
        def iPrescriptionDate(self):
            if self.Nmaeoftablets.get()=="" or self.ref.get()="":
                 messagebox.showerror("error","All field are required")  
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                   self.Nameoftablets.get(),
                                                                                                    self.ref.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.Nameoftablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.Issuedate.get(),    
                                                                                                    self.ExpDate.get(),
                                                                                                    self.DailyDose.get(),
                                                                                                    self.sideEffect.get(),
                                                                                                    self.furtherInformation.get(),
                                                                                                    self.storageAdvice.get(),
                                                                                                    self.DrivingUsingMachine.get(),
                                                                                                    self.HowToUseMedication.get(),
                                                                                                    self.PatientId.get(),
                                                                                                    self.nhsNumber.get(),
                                                                                                    self.PatientName.get(),
                                                                                                    self.DateOfBirth.get(),
                                                                                                    self.PatientAddress.get()
                                                                                                    ))    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Record has been inserted")
                
        def update(self):
             conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
             my_cursor=conn.cursor()
             my_cursor.execute("update hospital set Nameoftablets=%s,ref=%s,Dose=%s,Nameoftablets=%s,Lot=%s,Issuedate=%s,ExpDate=%s,DailyDose=%s,sideEffect=%s,furtherInformation=%s,storageAdvice=%s)",( 
                                                                                                    
                                                                                                    self.ref.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.Nameoftablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.Issuedate.get(),    
                                                                                                    self.ExpDate.get(),
                                                                                                    self.DailyDose.get(),
                                                                                            
                                                                                                    self.storageAdvice.get(),
                                                                                           
                                                                                                    self.nhsNumber.get(),
                                                                                                    self.PatientName.get(),
                                                                                                    self.DateOfBirth.get(),
                                                                                                    self.PatientAddress.get())
                                                                                                     )) 
                    
                
        def fetch_date(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from hospital")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                    self.hospital_table.insert("",END,Values=i)
                conn.commit()
            conn.close()  
            
        def get_cursor(self,event=""):
            cursor_row=self.hospital_table.focus()
            content=self.hospital_table.item(cursor_row)
            row=content["values"]
            self.Nameoftablets=set(row[0])
            self.ref=set(row[1])
            self.Dose=set(row[2])
            self.Nameoftablets=set(row[3])
            self.Lot=set(row[4])
            self.Issuedate=set(row[5])    
            self.ExpDate=set(row[6])
            self.DailyDose=set(row[7])
            self.storageAdvice=set(row[8])
            self.nhsNumber=set(row[9])
            self.PatientName=set(row[10])
            self.DateOfBirth=set(row[11])
            self.PatientAddress=set(row[12])
            
        def iprescription(self):
             self.txtPrescription.insert(END,"name Of Tablets:\t\t\t"+self.NameOftablets.get() +"\n")         
             self.txtPrescription.insert(END,"Referance No.:\t\t\t"+self.Referance No.get() +"\n")                                                                                           
             self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get() +"\n")                                                                                       
             self.txtPrescription.insert(END,"Number Of Tablets:\t\t\t"+self.NumberOftablets.get() +"\n")                                                                                      
             self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get() +"\n")                                                                                       
             self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issue Date.get() +"\n") 
             self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.Exp Date.get() +"\n") 
             self.txtPrescription.insert(END,"daily Dose:\t\t\t"+self.Daily Dose.get() +"\n") 
             self.txtPrescription.insert(END,"side Effect:\t\t\t"+self.side Effect.get() +"\n") 
             self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.furtherInformation.get() +"\n") 
             self.txtPrescription.insert(END,"StorageAdvice:\t\t\t"+self.storageAdvice.get() +"\n") 
             self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t"+self.DrivingUsingMachine.get() +"\n") 
             self.txtPrescription.insert(END,"PatientId:\t\t\t"+self.PatientId.get() +"\n") 
             self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get() +"\n") 
             self.txtPrescription.insert(END,"PatientName:\t\t\t"+self.PatientName.get() +"\n") 
             self.txtPrescription.insert(END,"DateOfBirth:\t\t\t"+self.DateOfBirth.get() +"\n")
             self.txtPrescription.insert(END,"PatientAddress:\t\t\t"+self.PatientAddress.get() +"\n")  
        
        def idelete(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
            my_cursor=conn.cursor()
            query="delete from hospital where Referance_No=%s"
            value=(self.ref.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Delete","Patient has been deleted successfully")
            
        def clear(self):
            self.Nameoftablets.set("")
            self.ref.set("")
            self.Dose.set("")
            self.NumberofTablets.set("")
            self.Lot.set("")
            self.Issuedate.set("")
            self.ExpDate.set("")
            self.DailyDose.set("")
            self.sideEfect.set("")
            self.FurtherInformation.set("")
            self.StorageAdvice.set("")
            self.DrivingUsingMachine.set("")
            self.HowToUseMedication.set("")
            self.PatientId.set("")
            self.nhsNumber.set("")
            self.PatientNmae.set("")
            self.DateOfBirth.set("")
            self.PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
        
        def iExit(self):
            iExit=messagebox.askyesno("Hospital management system","Confirm you want to exit")
            if iExit>0:
                root.destroy()
                return
              
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__=="__main__":        
    root=Tk() 
    ob=Hospital(root)
    root.mainloop() 

       