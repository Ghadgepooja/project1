from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry('1050x500+230+200')


         #========================variables====================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_availablerooms=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        




        
        #===========title=========

        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #========LOGO=======

        img2=Image.open(r"C:\\images\\logo.jpeg")
        img2=img2.resize((100,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

         #===========LABEL========

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room_details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=400,height=390)


          #=============================labels and entry===================

          #customer contact
        lbl_cust_contact=Label(labelframeleft,text="Customer contact:",font=("arial",12,"bold"),padx=1,pady=3)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("times new roman",13,"bold"),width=17)
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetch data btn

        btnfetch=Button(labelframeleft,text="Fetch Data",command=self.fetch_contact,width=9,font=("arial",10,"bold"),bg="black",fg="gold")
        btnfetch.place(x=310,y=3)


         #check in 
        check_in_date=Label(labelframeleft,text="Check_In Date:",font=("arial",12,"bold"),padx=1,pady=3)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheckindate=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("times new roman",13,"bold"),width=25)
        txtcheckindate.grid(row=1,column=1)

        #check out
        check_out_date=Label(labelframeleft,text="Check_Out Date:",font=("arial",12,"bold"),padx=1,pady=3)
        check_out_date.grid(row=2,column=0,sticky=W)

        txtcheckoutdate=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("times new roman",13,"bold"),width=25)
        txtcheckoutdate.grid(row=2,column=1)

        #room type

        Label_roomtype=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=1,pady=3)
        Label_roomtype.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        

        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("times new roman",12,"bold"),width=26,state="readonly")
        combo_roomtype["value"]=ide
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)

        #available rooms
        label_roomavailable=Label(labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=1,pady=3)
        label_roomavailable.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        AvailableRoom=ttk.Combobox(labelframeleft,textvariable=self.var_availablerooms,font=("times new roman",11,"bold"),width=20,state="readonly")
        AvailableRoom["value"]=rows
        AvailableRoom.current(0)
        AvailableRoom.grid(row=4,column=1)


        # txtroomavailable=ttk.Entry(labelframeleft,textvariable=self.var_availablerooms,font=("times new roman",13,"bold"),width=25)
        # txtroomavailable.grid(row=4,column=1)
         
        #meal
        lbl_meal=Label(labelframeleft,text="Meal",font=("arial",12,"bold"),padx=1,pady=3)
        lbl_meal.grid(row=5,column=0,sticky=W)

        txt_meal=ttk.Entry(labelframeleft,textvariable=self.var_meal,font=("times new roman",13,"bold"),width=25)
        txt_meal.grid(row=5,column=1)
        

        #no of days
        lbl_noofdays=Label(labelframeleft,text="No Of Days",font=("arial",12,"bold"),padx=1,pady=3)
        lbl_noofdays.grid(row=6,column=0,sticky=W)

        txtnoofdays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,font=("times new roman",13,"bold"),width=25)
        txtnoofdays.grid(row=6,column=1)
        
        
        #paid tax

        lbl_noofdays=Label(labelframeleft,text="Paid Tax",font=("arial",12,"bold"),padx=1,pady=3)
        lbl_noofdays.grid(row=7,column=0,sticky=W)

        txtnoofdays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font=("times new roman",13,"bold"),width=25)
        txtnoofdays.grid(row=7,column=1)
        

        #subtotal
    
        lbl_subtotal=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_subtotal.grid(row=8,column=0,sticky=W)

        txtsubtotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font=("times new roman",13,"bold"),width=25)
        txtsubtotal.grid(row=8,column=1)
      
        # Total cost
        lbl_totalcost=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=1,pady=3)
        lbl_totalcost.grid(row=9,column=0,sticky=W)

        txttotalcost=ttk.Entry(labelframeleft,textvariable=self.var_total,font=("times new roman",13,"bold"),width=25)
        txttotalcost.grid(row=9,column=1)

        # btn bill

        btnbill=Button(labelframeleft,text="BILL",command=self.total,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        btnbill.grid(row=10,column=0,padx=1,sticky=W)


        #===============================btns=========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=340,width=410,height=35)

        add_btn=Button(btn_frame,text="ADD", command=self.add_room,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        add_btn.grid(row=0,column=0,padx=1)

        update_btn=Button(btn_frame,text="UPDATE",command=self.update,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        update_btn.grid(row=0,column=1,padx=1)

        del_btn=Button(btn_frame,text="DELETE",command=self.mDelete,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        del_btn.grid(row=0,column=2,padx=1)

        res_btn=Button(btn_frame,text="RESET", command=self.reset,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        res_btn.grid(row=0,column=3,padx=1)

        #right side image

        img4=Image.open(r"C:\\images\\Room.jpeg")
        img4=img4.resize((640,170),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=700,y=55,width=360,height=170)

        
          #==========================table frame=====================================
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"))
        table_frame.place(x=435,y=220,width=650,height=260)

        lblsearch=Label(table_frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
        lblsearch.grid(row=0,column=0,sticky=W,padx=2)

        self.var_search=StringVar() 
        combo_search=ttk.Combobox(table_frame,textvariable=self.var_search,font=("times new roman",12,"bold"),width=15,state="readonly")
        combo_search["value"]=("Contact","roomtype")
        combo_search.current(0)
        combo_search.grid(row=0,column=1)
        
        self.txt_search=StringVar() 
        txt_serach=ttk.Entry(table_frame,textvariable=self.txt_search,font=("times new roman",13,"bold"),width=15)
        txt_serach.grid(row=0,column=2,padx=2)

        

        


        serby_btn=Button(table_frame,text="Search",command=self.search,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        serby_btn.grid(row=0,column=3,padx=1)

        show_btn=Button(table_frame,text="Show",command=self.fetch_room,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        show_btn.grid(row=0,column=4,padx=1)

         #===========================show data tabe===========================================
        
        details_table1=Frame(table_frame,bd=2,relief=RIDGE)
        details_table1.place(x=0,y=33,width=680,height=170)

        scroll_x=ttk.Scrollbar(details_table1,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table1,orient=VERTICAL)

        self.room_details_table=ttk.Treeview(details_table1,column=("contact","check in","check out","roomtype","roomnumber","meal","noofdays","paidtax","subtotal","totalcost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_details_table.xview)
        scroll_y.config(command=self.room_details_table.yview)

        self.room_details_table.heading("contact",text="Contact")
        self.room_details_table.heading("check in",text="Check-in")
        self.room_details_table.heading("check out",text="check-out")
        self.room_details_table.heading("roomtype",text="RoomType")
        self.room_details_table.heading("roomnumber",text="RoomNo")
        self.room_details_table.heading("meal",text="Meal")
        self.room_details_table.heading("noofdays",text="NoOfDays")
        self.room_details_table["show"]="headings"
        self.room_details_table.pack(fill=BOTH,expand=1) 

        
        self.room_details_table.column("contact",width=100)
        self.room_details_table.column("check in",width=100)
        self.room_details_table.column("check out",width=100)
        self.room_details_table.column("roomtype",width=100)
        self.room_details_table.column("roomnumber",width=100)
        self.room_details_table.column("meal",width=100)
        self.room_details_table.column("noofdays",width=100)
        self.room_details_table.pack(fill=BOTH,expand=1)

        self.room_details_table.bind("<ButtonRelease-1>",self.get_cursor)
       

        self.fetch_room()
       

       #==============================fetch function for fetching the data==================
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
    
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=431,y=52,width=260,height=160)

                lblName=Label(showDataframe,text="Name: ",font=("arial",11,"bold"))
                lblName.place(x=0,y=0) 

                lbl1=Label(showDataframe,text=row,font=("arial",11,"bold"))
                lbl1.place(x=70,y=0)


             #=======================for gender==================================
                conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
                my_cursor=conn.cursor()
                query=("select gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender: ",font=("arial",11,"bold"))
                lblGender.place(x=0,y=30)

                lbl1=Label(showDataframe,text=row,font=("arial",11,"bold"))
                lbl1.place(x=70,y=30)
              #=======================for email==================================
                conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
                my_cursor=conn.cursor()
                query=("select email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="Email: ",font=("arial",11,"bold"))
                lblemail.place(x=0,y=60)

                lbl2=Label(showDataframe,text=row,font=("arial",11,"bold"))
                lbl2.place(x=70,y=60)

                #=======================for nationality==================================
                conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
                my_cursor=conn.cursor()
                query=("select nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblnationality=Label(showDataframe,text="Nationality: ",font=("arial",11,"bold"))
                lblnationality.place(x=0,y=90)

                lbl3=Label(showDataframe,text=row,font=("arial",11,"bold"))
                lbl3.place(x=76,y=90)

                #=======================for address==================================
                conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
                my_cursor=conn.cursor()
                query=("select address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbladdress=Label(showDataframe,text="Address: ",font=("arial",11,"bold"))
                lbladdress.place(x=0,y=120)

                lbl4=Label(showDataframe,text=row,font=("arial",11,"bold"))
                lbl4.place(x=70,y=120)

                 
    
                 #========================================for search==============================
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.var_search.get())+" LIKE '%"+str(self.txt_search.get())+"%' ")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    



    
    
    
    
    def total(self):
        inDate=self.var_checkin.get()
        OutDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        OutDate=datetime.strptime(OutDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(OutDate-inDate).days)

        
        
        if(self.var_meal.get()=="lunch" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.01))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+(q5)*0.01))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="duplex"):
            q1=float(400)
            q2=float(800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)






 #================================add room details func========================
    def add_room(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                              self.var_contact.get(),
                                                              self.var_checkin.get(),
                                                              self.var_checkout.get(),
                                                              self.var_roomtype.get(),
                                                              self.var_availablerooms.get(),
                                                              self.var_meal.get(),
                                                              self.var_noofdays.get()
                                                            
                                                            ))
               conn.commit()
               self.fetch_room()
               conn.close()
               messagebox.showinfo("success","Room Booked!",parent=self.root)
            except Exception as es:
               messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)
 
   #==========================fetching room details===========================================
    def fetch_room(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #===============================get focus===================================================
    def get_cursor(self,event=""):
        cursor_row=self.room_details_table.focus()
        content=self.room_details_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_availablerooms.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

   
  #==============================for updating==========================================
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s",(
                                                                                               
                                                                                                self.var_checkin.get(),
                                                                                                self.var_checkout.get(),
                                                                                                self.var_roomtype.get(),
                                                                                                self.var_availablerooms.get(),
                                                                                                self.var_meal.get(),
                                                                                                self.var_noofdays.get(),
                                                                                                self.var_contact.get(),
                                                                                                ))
            conn.commit()
            self.fetch_room()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

   
   #========================================for deleting====================================
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete details this room detail",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_room()
        conn.close()

    #====================================reset all=======================================
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_availablerooms.set(""),
    
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")


    
     
   
      

       
        


        





if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()       