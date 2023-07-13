from tkinter import *
from PIL import Image,ImageTk
from pr2 import Cust_Win


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        
        # ===============1st image==============
        img1 = Image.open("D:/STUDY MATERIAL/SEM4/RPPOOP/Hotel_Management_System/images/hotel.jpg")
        img1 = img1.resize((1550,140),Image.ANTIALIAS) #-->Image.ANTIALIAS parameter specifies that the image should be resized with an anti-aliasing algorithm to preserve quality.
        self.photoimg1 = ImageTk.PhotoImage(img1)  #-->creates a Tkinter-compatible image object 

        lblimg = Label(self.root, image = self.photoimg1, bd = 4,relief = RIDGE ) # bd--> border,relief = border style
        lblimg.place(x=0,y=0,width=1550,height=140)

        # ===============logo================
        img2 = Image.open("D:/STUDY MATERIAL/SEM4/RPPOOP/Hotel_Management_System/images/logo.png")
        img2 = img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image = self.photoimg2, bd = 4,relief = RIDGE ) # bd--> border,relief = border style
        lblimg2.place(x=0,y=0,width=230,height=140)


        #===============title================
        lbl_title= Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE) 
        lbl_title.place(x=0,y=140,width=1550,height=50)

         #==============main frame===========
        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        
        #==============menu=================
        lbl_menu = Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE) 
        lbl_menu.place(x=0,y=0,width=230,height=35)

        #=============btn frame============
        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)
        # cust_btn.place(x=0,y=225,width=228,height=25)--> does not work

        room_btn=Button(btn_frame,text="ROOM",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="DETAILS",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        #=============right side image================
        img3 = Image.open("D:/STUDY MATERIAL/SEM4/RPPOOP/Hotel_Management_System/images/slide3.jpg")
        img3 = img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image = self.photoimg3, bd = 4,relief = RIDGE ) # bd--> border,relief = border style
        lblimg3.place(x=225,y=0,width=1310,height=590)

        #===========down image=======================
        img4 = Image.open("D:/STUDY MATERIAL/SEM4/RPPOOP/Hotel_Management_System/images/downImg1.jpg")
        img4 = img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(main_frame, image = self.photoimg4, bd = 4,relief = RIDGE ) # bd--> border,relief = border style
        lblimg4.place(x=0,y=225,width=230,height=210)

        img5 = Image.open("D:/STUDY MATERIAL/SEM4/RPPOOP/Hotel_Management_System/images/downImg2.jpg")
        img5 = img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg5 = Label(main_frame, image = self.photoimg5, bd = 4,relief = RIDGE ) # bd--> border,relief = border style
        lblimg5.place(x=0,y=420,width=230,height=190)


        def cust_details(self):
            self.new_window = Toplevel(self.root)
            self.app = Cust_Win(self.new_window)






    

if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

