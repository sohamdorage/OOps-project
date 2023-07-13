from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class Cust_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")



        #===============variables===============
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_cust_mother=StringVar()
        self.var_cust_gender=StringVar()
        self.var_cust_post=StringVar()
        self.var_cust_mobile=StringVar()
        self.var_cust_email=StringVar()
        self.var_cust_nationality=StringVar()
        self.var_cust_address=StringVar()
        self.var_cust_id_proof=StringVar()
        self.var_cust_id_number=StringVar()


        #===============title================
        lbl_title= Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE) 
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # ===============logo================
        img2 = Image.open("D:/STUDY MATERIAL/SEM4/RPPOOP/Hotel_Management_System/images/logo.png")
        img2 = img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image = self.photoimg2, bd = 0,relief = RIDGE ) # bd--> border,relief = border style
        lblimg2.place(x=5,y=2,width=100,height=40)

        #===============labelFrame===========
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #===============labels and entrys========
        #custRef
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref = ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly") #-->ttk for stylish entry       
        entry_ref.grid(row=0,column=1)

        #cust_name
        lblcname=Label(labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblcname.grid(row=1,column=0,sticky=W)

        txtcname = ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_name,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)
        
        #mother name
        lblmname=Label(labelframeleft,text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)

        txtmname = ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_mother,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)
        
        #gender combobox
        lbl_gender=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_cust_gender,width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)  #-->to make male as default choice
        combo_gender.grid(row=3,column=1)

        #postcode
        lblPostCode=Label(labelframeleft,text="PostCode:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)

        txtPostCode = ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_post,font=("arial",13,"bold"))
        txtPostCode.grid(row=4,column=1)

        #mobilenumber
        lblMobile=Label(labelframeleft,text="Mobile:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)

        txtMobile = ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_mobile,font=("arial",13,"bold"))
        txtMobile.grid(row=5,column=1)

        #email
        lblEmail=Label(labelframeleft,text="email:",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)

        txtEmail = ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_email,font=("arial",13,"bold"))
        txtEmail.grid(row=6,column=1)

        #nationalityy
        lblNationality=Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_cust_nationality,width=27,state="readonly")
        combo_Nationality["value"]=("Indian","American","British")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        


        #idproof type combobox
        lblIdProof=Label(labelframeleft,text="Id Proofr:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,textvariable=self.var_cust_id_proof,state="readonly")
        combo_id["value"]=("AadharCard","DrivingLiscence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        
        #id number
        lblIdNumber=Label(labelframeleft,text="Id Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_id_number,font=("arial",13,"bold"))
        txtIdNumber.grid(row=9,column=1)

        #address
        lblAddress=Label(labelframeleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)

        txtAddress= ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_address,font=
                              ("arial",13,"bold"))
        txtAddress.grid(row=10,column=1)


        # ==========buttons==========
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=425,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)


        #===========tableframe search system ===============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),padx=2,pady=6,bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()

        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch = ttk.Entry(Table_Frame,width=24,textvariable=self.txt_search,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2)

        btnSearch=Button(Table_Frame,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowAll=Button(Table_Frame,text="Show All ",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #========Show data Table===============
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL) #--->for making scroll bar
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)  #-->these all are dummy names

        scroll_x.pack(side=BOTTOM,fill=X)  #X-->axis
        scroll_y.pack(side=RIGHT,fill=Y)  #Y-->axis

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)


        self.Cust_Details_Table.heading("ref",text="Ref no")  #ref-->dummy name,  Ref no-->name to show to user
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother's Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="Post")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id proof")
        self.Cust_Details_Table.heading("idnumber",text="Id number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)






if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()