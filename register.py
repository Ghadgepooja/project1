from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

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
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\ADMIN\Desktop\Hotel ma agement system\image\regi.jpeg")

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

        lblimg=Button(frame,image=self.photoimg4,borderwidth=0,cursor="hand2")
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
               

    

       




    


if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()