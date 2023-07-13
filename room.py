from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime
from details import DetailsRoom
    


class Roombooking:
    def __init__(self,root):

          
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")


        # ================variables=========
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_room=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        

        #===============title================
        lbl_title= Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE) 
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # ===============logo================
        img2 = Image.open("D:/STUDY MATERIAL/SEM4/RPPOOP/Hotel_Management_System/images/logo.png")
        img2 = img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image = self.photoimg2, bd = 0,relief = RIDGE ) # bd--> border,relief = border style
        lblimg2.place(x=5,y=2,width=100,height=40)

        #===============labelFrame===========
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Room booking Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #===============labels and entrys========
        #customer contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)  
        entry_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))        
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetch data button-
        btn_fetch_data=Button(labelframeleft,text="Fetch Data",command=self.fetch_contact,font=("arial",8,"bold"),width=10,bg="black",fg="gold")
        btn_fetch_data.place(x=340,y=4)

        #customer checkin date
        lbl_cust_check_in=Label(labelframeleft,text="Check in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_check_in.grid(row=1,column=0,sticky=W)  

        entry_check_in = ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))      
        entry_check_in.grid(row=1,column=1)

        #customer checkout date
        lbl_cust_check_out=Label(labelframeleft,text="Check Out Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_check_out.grid(row=2,column=0,sticky=W)  
        entry_check_out = ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold")) 
        entry_check_out.grid(row=2,column=1)
        
        #Roomtype
        lbl_cust_roomtype=Label(labelframeleft,text="Roomtype:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_roomtype.grid(row=3,column=0,sticky=W)  

        

        # conn=mysql.connector.connect(host="localhost",username="root",password="Passward@123",database="management")
        # my_cursor=conn.cursor()
        # my_cursor.execute("select RoomType from details")
        # ide=my_cursor.fetchall()

        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_roomtype["values"]=("Single","Double","Deluxe","Luxury")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)
        

        #Available Rooms
        lbl_cust_room=Label(labelframeleft,text="Room no.:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_room.grid(row=4,column=0,sticky=W)  
        # entry_room= ttk.Entry(labelframeleft,textvariable=self.var_room,width=29,font=("arial",13,"bold"))     
        # entry_room.grid(row=4,column=1)
        combo_roomNo=ttk.Combobox(labelframeleft,textvariable=self.var_room,font=("arial",12,"bold"),width=27,state="readonly")
        combo_roomNo.grid(row=4,column=1)
        # combo_roomNo["values"]=(" abc","def")
        
        # conn=mysql.connector.connect(host="localhost",username="root",password="Passward@123",database="management")
        # my_cursor=conn.cursor()
        # my_cursor.execute("select RoomNo from details WHERE RoomType =%s",(self.var_roomtype.get(),))
        # rows=my_cursor.fetchall()
                
            


        # # conn=mysql.connector.connect(host="localhost",username="root",password="Passward@123",database="management")
        # # my_cursor=conn.cursor()
        # # my_cursor.execute("select RoomNO from details")
        # # rows=my_cursor.fetchall()

        def update_room_numbers(*args):
            selected_room_type = self.var_roomtype.get()
            
            # Establish database connection and create cursor
            conn = mysql.connector.connect(host="localhost", username="root", password="Passward@123", database="management")
            my_cursor = conn.cursor()

            # Execute query to fetch room numbers based on the selected room type
            query = "SELECT RoomNo FROM details WHERE RoomType = %s"
            my_cursor.execute(query, (selected_room_type,))
            rows = my_cursor.fetchall()

            # Update the combobox values with the fetched room numbers
            combo_roomNo["values"] = [row[0] for row in rows]
            combo_roomNo.current(0)

        
        # combo_roomNo.current(0)
            

        self.var_roomtype.trace("w", update_room_numbers)

        # Initially populate the room numbers based on the default room type
        update_room_numbers(self)

        
        #Meals
        lbl_cust_meals=Label(labelframeleft,text="Meals:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_meals.grid(row=5,column=0,sticky=W) 

        # entry_meals = ttk.Entry(labelframeleft,width=29,textvariable=self.var_meal,font=("arial",13,"bold"))       
        # entry_meals.grid(row=5,column=1)

        combo_meaals=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",12,"bold"),width=27,state="readonly")
        combo_meaals["values"]=("BreakFast","Lunch","Dinner")
        combo_meaals.current(0)
        combo_meaals.grid(row=5,column=1)

        #No. of Days
        lbl_cust_no_of_days=Label(labelframeleft,text="No. of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_no_of_days.grid(row=6,column=0,sticky=W)

        entry_no_of_days = ttk.Entry(labelframeleft,width=29,textvariable=self.var_noofdays,font=("arial",13,"bold"))        
        entry_no_of_days.grid(row=6,column=1)

        #Paid Tax
        lbl_cust_paidtax=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_paidtax.grid(row=7,column=0,sticky=W)  

        entry_paidtax = ttk.Entry(labelframeleft,width=29,textvariable=self.var_paidtax,font=("arial",13,"bold"),state="readonly")       
        entry_paidtax.grid(row=7,column=1)

        #Sub Total
        lbl_cust_subtotal=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_subtotal.grid(row=8,column=0,sticky=W)  
        entry_subtotal= ttk.Entry(labelframeleft,width=29,textvariable=self.var_actualtotal,font=("arial",13,"bold"),state="readonly")    
        entry_subtotal.grid(row=8,column=1)

        #Total Cost
        lbl_cust_totalcost=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_totalcost.grid(row=9,column=0,sticky=W)  
        entry_totalcost = ttk.Entry(labelframeleft,width=29,textvariable=self.var_total,font=("arial",13,"bold"),state="readonly")  
        entry_totalcost.grid(row=9,column=1)

        #=======Bill button==========
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        # ==========buttons==========
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=425,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)


        #===========Right Side Image=====================

        img3 = Image.open("D:/STUDY MATERIAL/SEM4/RPPOOP/Hotel_Management_System/images/bed.jpg")
        img3 = img3.resize((530,270),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(self.root, image = self.photoimg3, bd = 0,relief = RIDGE ) # bd--> border,relief = border style
        lblimg3.place(x=760,y=55,width=530,height=270)



        #===========tableframe search system ===============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details ",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        # lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),padx=2,pady=6,bg="red",fg="white")
        # lblSearchBy.grid(row=0,column=0,sticky=W)

        # self.search_var=StringVar() #--> store mobile or ref option whichever selected

        # combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly")
        # combo_Search["value"]=("Contact","Room")
        # combo_Search.current(0)
        # combo_Search.grid(row=0,column=1,padx=2)

        # self.txt_search=StringVar() #-->  store input in entry table i.e mobile or ref to be searched
        # txtSearch = ttk.Entry(Table_Frame,width=24,textvariable=self.txt_search,font=("arial",13,"bold"))
        # txtSearch.grid(row=0,column=2)

        
        # btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        # btnSearch.grid(row=0,column=3,padx=1)
        
        # btnShowAll=Button(Table_Frame,text="Show All ",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        # btnShowAll.grid(row=0,column=4,padx=1)

        #========Show data Table===============
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=0,width=860,height=230)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL) #--->for making scroll bar
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)


        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","room","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)  #-->these all are dummy names

        scroll_x.pack(side=BOTTOM,fill=X)  #X-->axis
        scroll_y.pack(side=RIGHT,fill=Y)  #Y-->axis

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")  #ref-->dummy name,  Ref no-->name to show to user
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room type")
        self.room_table.heading("room",text="Room no.")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="No. of Days")
        
        
        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("room",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #=============update room numbers acoording to roomtype=================
    

    #==============add data================
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="Passward@123",database="management")
                my_cursor=conn.cursor()
                # Check if the room is already booked
                room_number = self.var_room.get()
                my_cursor.execute("SELECT room FROM room WHERE room = %s", (room_number,))
                result = my_cursor.fetchone()


                

                if result:
                    messagebox.showerror("Error", "The Room is already booked.", parent=self.root)

                else:
                    my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),
                                                                                                self.var_checkin.get(),
                                                                                                self.var_checkout.get(),
                                                                                                self.var_roomtype.get(),
                                                                                                self.var_room.get(),
                                                                                                self.var_meal.get(),
                                                                                                self.var_noofdays.get(),
                                                                                                ))
                
                    conn.commit()
                    self.fetch_data()
                    conn.close()

                    messagebox.showinfo("Success","Room has been booked",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)


    #============fetch roombooking data=================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Passward@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #===========get cursor=======================   
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"] 

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_room.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])        

    #=============update=================
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact number",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Passward@123",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("UPDATE room set checkin=%s,checkout=%s,roomtype=%s,room=%s,meal=%s,noOfdays=%s WHERE Contact=%s",(
                                            self.var_checkin.get(),self.var_checkout.get(),
                                            self.var_roomtype.get(),self.var_room.get(),
                                            self.var_meal.get(),self.var_noofdays.get(), self.var_contact.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("update","Room details has been updated successfully",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    #==============delete===============
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Passward@123",database="management")
            my_cursor=conn.cursor()

            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        
        else:
            if not delete:
                return
            
        conn.commit()
        self.fetch_data()
        conn.close()    

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_room.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")   
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")







      
    #=============All Customer Data Fetch=========================
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter contact number",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Passward@123",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number is not found",parent=self.root)

            else:
                #===================Name========================
                conn.commit()
                conn.close()
            
                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=300,height=180)

                lbl_name=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
                lbl_name.place(x=0,y=0)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                #==============Gender==================
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Passward@123",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbl_gender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
                lbl_gender.place(x=0,y=30)

                lbl2=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                #==============email=====================
                conn=mysql.connector.connect(host="localhost",username="root",password="Passward@123",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbl_name=Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
                lbl_name.place(x=0,y=60)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=60)

                #==============Nationality=====================
                conn=mysql.connector.connect(host="localhost",username="root",password="Passward@123",database="management")
                my_cursor=conn.cursor()
                query=("select nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbl_name=Label(showDataFrame,text="Nationality:",font=("arial",12,"bold"))
                lbl_name.place(x=0,y=90)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=90)

                #==============Address=====================
                conn=mysql.connector.connect(host="localhost",username="root",password="Passward@123",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbl_name=Label(showDataFrame,text="Address:",font=("arial",12,"bold"))
                lbl_name.place(x=0,y=120)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=120)

    # #==================search system=========================
    # def search(self):
    #     conn=mysql.connector.connect(host="localhost",username="root",password="Passward@123",database="management")
    #     my_cursor=conn.cursor()

    #     my_cursor.execute("SELECT * FROM customer WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        


    #     rows=my_cursor.fetchall()

    #     if len(rows)!=0:
    #         self.room_table.delete(*self.room_table.get_children())
    #         for i in rows:
    #             self.room_table.insert("",END,values=i)
    #         conn.commit()
    #     conn.close()


    #=============total billing==============

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y") 
        outDate=datetime.strptime(outDate,"%d/%m/%Y") 
        # self.var_noofdays.set(abs(outDate-inDate).days)
        noofdays=float(abs(outDate-inDate).days)
        

        # if(self.var_meal.get()=="BreakFast"and self.var_roomtype.get()=="Luxary"):
        #     q1=float(300)
        #     q2=float(500)
        #     q3=float(self.var_noofdays.get())
        #     q4=float(q1+q2)
        #     q5=float(q3*q4)
        #     Tax="Rs."+str("%.2f"%((q5)*0.1))
        #     ST="Rs."+str("%.2f"%((q5)))
        #     TT="Rs."+str("%2f"%(q5+((q5)*0.1)))
        #     self.var_paidtax.set(Tax)
        #     self.var_actualtotal.set(ST)
        #     self.var_total.set(TT)

        # elif(self.var_meal.get()=="Lunch"and self.var_roomtype.get()=="Single"):
        #     q1=float(300)
        #     q2=float(500)
        #     q3=float(self.var_noofdays.get())
        #     q4=float(q1+q2)
        #     q5=float(q3*q4)
        #     Tax="Rs."+str("%.2f"%((q5)*0.1))
        #     ST="Rs."+str("%.2f"%((q5)))
        #     TT="Rs."+str("%2f"%(q5+((q5)*0.1)))
        #     self.var_paidtax.set(Tax)
        #     self.var_actualtotal.set(ST)
        #     self.var_total.set(TT)
            
        # elif(self.var_meal.get()=="BreakFast"and self.var_roomtype.get()=="Deluxe"):
        #     q1=float(300)
        #     q2=float(500)
        #     q3=float(self.var_noofdays.get())
        #     q4=float(q1+q2)
        #     q5=float(q3*q4)
        #     Tax="Rs."+str("%.2f"%((q5)*0.1))
        #     ST="Rs."+str("%.2f"%((q5)))
        #     TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        #     self.var_paidtax.set(Tax)
        #     self.var_actualtotal.set(ST)
        #     self.var_total.set(TT)


        if self.var_meal.get()=="BreakFast":
            meal_cost=float(100)
        elif self.var_meal.get()=="Lunch":
            meal_cost=float(200)
        elif self.var_meal.get()=="Dinner":
            meal_cost=float(200)

        if self.var_roomtype.get()=="Single":
            room_cost=float(1000)

        elif self.var_roomtype.get()=="Double":
            room_cost=float(2000)

        elif self.var_roomtype.get()=="Deluxe":
            room_cost=float(3000)

        elif self.var_roomtype.get()=="Luxury":
            room_cost=float(4000)

        print(type(noofdays))
        print(type(meal_cost))
        print(type(room_cost))


        # ST="Rs. "+str("%.2f"%((meal_cost+room_cost)*noofdays))
        ST = "Rs. " + str("%.2f" % ((meal_cost + room_cost) * noofdays ))
        Tax = "Rs. " + str("%.2f" % ((meal_cost + room_cost) * noofdays * 0.1))
        TT = "Rs. " + str("%.2f" % ((meal_cost + room_cost) * noofdays * 1.1))
        # TT="Rs. "+str("%.2f"%((meal_cost+room_cost)*noofdays)*1.1)


        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)
        self.var_noofdays.set(str(noofdays))
        




if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
