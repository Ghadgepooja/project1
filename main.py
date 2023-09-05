from tkinter import*
from PIL import Image,ImageTk
from customer import cust_win
from room import Roombooking
from details import DetailsRoom

class hotel:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry('1360x645+0+0')

        #=====================img1===============================
        img1=Image.open("image\\taj.jpeg")
        img1=img1.resize((1349,80),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=6,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1349,height=140)

        #====logo========

        img2=Image.open(r"C:\\images\\logo.jpeg")
        img2=img2.resize((230,80),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=6,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=110)

         #==================title==============================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=110,width=1360,height=50)

        #mainframe
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=160,width=1360,height=570)

        #======================menu=========================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=224,height=50)

        #=============================btn frame===========================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=224,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER", command=self.cust_details,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.grid(row=0,column=0,pady=1)

        cust_btn=Button(btn_frame,text="ROOMS",command=self.roombooking,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.grid(row=1,column=0,pady=1)

        cust_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.grid(row=2,column=0,pady=1)

        cust_btn=Button(btn_frame,text="REPORT",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.grid(row=3,column=0,pady=1)

        cust_btn=Button(btn_frame,text="LOGOUT",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.grid(row=4,column=0,pady=1)

        
          #==========================right side menu=====================
        img3=Image.open(r"C:\\images\\slide3.jpeg")
        img3=img3.resize((1120,570),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1120,height=490)

        
        #======================================down image=================
        img4=Image.open(r"C:\\images\\room2.jpeg")
        img4=img4.resize((224,147),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=225,width=224,height=135)

        img5=Image.open(r"C:\\images\\khana.jpeg")
        img5=img5.resize((224,147),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=365,width=224,height=120)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)



    
    
if __name__ == "__main__":
    root=Tk()
    obj=hotel(root)
    root.mainloop()