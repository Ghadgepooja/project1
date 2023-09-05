from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
#from hotel import HotelManagementSystem
import mysql.connector
from customer import cust_win
from room import Roombooking
from details import DetailsRoom


def main():
    win=Tk()
    app=Login(win)
    win.mainloop()

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry('1360x768+0+0')

        #==============var====================
        self.var_email=StringVar()
        self.var_pass=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ADMIN\Desktop\Hotel ma agement system\image\sun.jpeg")

        lblimg=Label(self.root,image=self.bg)
        lblimg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=120,width=340,height=410)

        img2=Image.open(r"C:\Users\ADMIN\Desktop\Hotel ma agement system\image\userlogo.jpg")
        img2=img2.resize((100,100),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=6,relief=RIDGE)
        lblimg.place(x=620,y=80,width=100,height=100)

        lbl_cust_phone=Label(frame,text="Get started",font=("times new roman",24,"bold"),fg="white",bg="black")
        lbl_cust_phone.place(x=90,y=70)

        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=145)

        self.enty_user=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.enty_user.place(x=40,y=180,width=270)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=215)
        
        self.enty_pass=ttk.Entry(frame,show='*',font=("times new roman",15,"bold"))
        self. enty_pass.place(x=40,y=250,width=270)

        def show_pass():
            if self.enty_pass.cget('show')=='*':
                self.enty_pass.config(show='')
            else:
                self.enty_pass.config(show='*')    

        check_button=Checkbutton(root,text="show password",command=show_pass)
        check_button.place(x=540,y=410)

         #=================================login btn=========================================
        login=Button(frame,text="Login",command=self.hotel_window,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,bg="red",fg="white",activebackground="red",foreground="white")
        login.place(x=180,y=350,width=100,height=30)

        #=================================register btn=========================================
        register=Button(frame,text="Register New user",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white")
        register.place(x=12,y=350,width=140)

        #=================================forgot btn=========================================
        forgot=Button(frame,text="forgot password",font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white")
        forgot.place(x=12,y=370,width=140)

    def register_window(self):
         self.new_window=Toplevel(self.root)
         self.app=Register(self.new_window)

    def hotel_window(self):
         self.new_window=Toplevel(self.root)
         self.app=hotel(self.new_window)

    # def login_window(self):
    #      self.new_window=Toplevel(self.root)
    #      self.app=Login(self.new_window)


    def login1(self):
         if self.enty_user.get()=="" or self.enty_pass.get()=="":
            messagebox.showerror("Error","All fields are required")
         elif self.enty_user.get()=="neetarane345" and self.enty_pass.get()=="neetarane@123":
            messagebox.showinfo("Success! you are login successfully to the hotel management system.....")
         else :
             conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
             my_cursor=conn.cursor()
             my_cursor.execute("select * from register where email=%s  and password=%s",(
                                                                     self.var_email.get(),
                                                                     self.var_pass.get(),

             ))

             row=my_cursor.fetchone()
             if row!=None:
                 messagebox.showerror("Error","user already exist ,please try another email")
             else:
                open_main=messagebox.askyesno("yesno","access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=hotel(self.new_window)
                else:
                    if not open_main:
                        return    
             conn.commit()
             conn.close()

            
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry('1360x768+0+0')


         #========================variables====================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
       

       #============================bg image==========================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ADMIN\Desktop\Hotel ma agement system\image\sun.jpeg")

        lblimg=Label(self.root,image=self.bg)
        lblimg.place(x=0,y=0,relwidth=1,relheight=1)

        #===================================left image===============================
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\ADMIN\Desktop\Hotel ma agement system\image\loginimg.jpeg")

        lblimg=Label(self.root,image=self.bg1)
        lblimg.place(x=42,y=90,width=450,height=520)

        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=90,width=700,height=520)

        lblimg=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        lblimg.place(x=20,y=20)

        #=======================================label and entry==============================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=370,y=130,width=250)

        #========================================2nd row======================================
        contact_no=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact_no.place(x=50,y=170)

        contact_no_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contact_no_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        email_entry=_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=370,y=200,width=250)

        #========================================3rd row===================================
        security_q=Label(frame,text="Select security Q.",font=("times new roman",15,"bold"),bg="white")
        security_q.place(x=50,y=240)

        combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        combo_security_q["value"]=["Select","your birth date","your birth place"]
        combo_security_q.current(0)
        combo_security_q.place(x=50,y=270,width=250)

        security_a=Label(frame,text="Select ans.",font=("times new roman",15,"bold"),bg="white")
        security_a.place(x=370,y=240)

        security_a_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        security_a_entry.place(x=370,y=270,width=250)

        #========================================4th row===================================
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password.place(x=50,y=310)
        
        password_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        password_entry.place(x=50,y=340,width=250)

        con_pass=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        con_pass.place(x=370,y=310)

        con_pass_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        con_pass_entry.place(x=370,y=340,width=250)

        #=======================================check btn===================================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #===========================================buttons===================================
        img3=Image.open(r"C:\Users\ADMIN\Desktop\Hotel ma agement system\image\registerimg.jpeg")
        img3=img3.resize((200,50),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Button(frame,command=self.register_data,image=self.photoimg3,borderwidth=0,cursor="hand2")
        lblimg.place(x=10,y=420,width=200)

         #===========================================buttons===================================
        img4=Image.open(r"C:\Users\ADMIN\Desktop\Hotel ma agement system\image\loginimg.jpeg")
        img4=img4.resize((200,50),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Button(frame,command=self.return_login,image=self.photoimg4,borderwidth=0,cursor="hand2")
        lblimg.place(x=330,y=420,width=200)
    

    #====function declaration=====

    def register_data(self):
        
         if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
         elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error" ,"password and confirm password must be same")
         elif self.var_check.get()==0:
            messagebox.showerror("Error" ,"please agree our terms and conditions")
         else:
             conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
             my_cursor=conn.cursor()
             query=("select * from register where email=%s")
             value=(self.var_email.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             if row!=None:
                 messagebox.showerror("Error","user already exist ,please try another email")
             else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                              self.var_fname.get(),
                                                              self.var_lname.get(),
                                                              self.var_contact.get(),
                                                              self.var_email.get(),
                                                              self.var_securityQ.get(),
                                                              self.var_securityA.get(),
                                                              self.var_pass.get(),
                                                              
                                                            ))
             conn.commit()
               
             conn.close()
             messagebox.showinfo("success","Register Successfully")
    
    def return_login(self):
        self.root.destroy()
      

class hotel:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
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

        cust_btn=Button(btn_frame,text="LOGOUT",command=self.redirect,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.grid(row=3,column=0,pady=1)

        # cust_btn=Button(btn_frame,text="LOGOUT",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        # cust_btn.grid(row=4,column=0,pady=1)

        
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

    def redirect(self):
        self.root.destroy()

    

if __name__ == "__main__":
   main()