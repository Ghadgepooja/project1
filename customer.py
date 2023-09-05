from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import random
import mysql.connector
from tkinter import messagebox


class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry('1050x500+230+200')
        
        #========================variables====================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother_name=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mob=StringVar()
        self.var_mail=StringVar()
        self.var_nation=StringVar()
        self.var_proof=StringVar()
        self.var_id=StringVar()
        self.var_addr=StringVar()

        

        #===========title=========

        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #========LOGO=======

        img2=Image.open(r"C:\\images\\logo.jpeg")
        img2=img2.resize((100,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #===========LABEL========

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="customer_details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=400,height=440)

        

          #=============================labels and entry===================
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=1,pady=3)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("times new roman",13,"bold"),width=25,state="readonly")
        enty_ref.grid(row=0,column=1)

        cust_name=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=1,pady=3)
        cust_name.grid(row=1,column=0,sticky=W)

        cust_ref=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("times new roman",13,"bold"),width=25)
        cust_ref.grid(row=1,column=1)

        mother_name=Label(labelframeleft,text="Mother Name",font=("arial",12,"bold"),padx=1,pady=3)
        mother_name.grid(row=2,column=0,sticky=W)

        mother_ref=ttk.Entry(labelframeleft,textvariable=self.var_mother_name,font=("times new roman",13,"bold"),width=25)
        mother_ref.grid(row=2,column=1)
    
         #gender

        gender=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=1,pady=3)
        gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=26,state="readonly")
        combo_gender["value"]=("male","female","other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        

        
        post=Label(labelframeleft,text="post",font=("arial",12,"bold"),padx=1,pady=3)
        post.grid(row=4,column=0,sticky=W)

        post_ref=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("times new roman",13,"bold"),width=25)
        post_ref.grid(row=4,column=1)

        mob=Label(labelframeleft,text="Mobile",font=("arial",12,"bold"),padx=1,pady=3)
        mob.grid(row=5,column=0,sticky=W)

        mob_ref=ttk.Entry(labelframeleft,textvariable=self.var_mob,font=("times new roman",13,"bold"),width=25)
        mob_ref.grid(row=5,column=1)

        mail=Label(labelframeleft,text="Email",font=("arial",12,"bold"),padx=1,pady=3)
        mail.grid(row=6,column=0,sticky=W)

        mail_ref=ttk.Entry(labelframeleft,textvariable=self.var_mail,font=("times new roman",13,"bold"),width=25)
        mail_ref.grid(row=6,column=1)
        
        #nationality

        nation=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=1,pady=3)
        nation.grid(row=7,column=0,sticky=W)

        combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nation,font=("times new roman",12,"bold"),width=26,state="readonly")
        combo_nationality["value"]=("Indian","American","Russian")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)

        #proof
        

        proof=Label(labelframeleft,text="Id Proof Type",font=("arial",12,"bold"),padx=1,pady=3)
        proof.grid(row=8,column=0,sticky=W)

        combo_idproof=ttk.Combobox(labelframeleft,textvariable=self.var_proof,font=("times new roman",12,"bold"),width=26,state="readonly")
        combo_idproof["value"]=("Adhar card","Driving Liscence","Passport")
        combo_idproof.current(0)
        combo_idproof.grid(row=8,column=1)
        
        id=Label(labelframeleft,text="Id Number:",font=("arial",12,"bold"),padx=2,pady=6)
        id.grid(row=9,column=0,sticky=W)

        id_ref=ttk.Entry(labelframeleft,textvariable=self.var_id,font=("times new roman",13,"bold"),width=25)
        id_ref.grid(row=9,column=1)

        addr=Label(labelframeleft,text="Address:",font=("arial",12,"bold"),padx=1,pady=3)
        addr.grid(row=10,column=0,sticky=W)

        addr_ref=ttk.Entry(labelframeleft,textvariable=self.var_addr,font=("times new roman",13,"bold"),width=25)
        addr_ref.grid(row=10,column=1)

        #===============================btns=========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=340,width=410,height=35)

        add_btn=Button(btn_frame,text="ADD", command=self.add_data,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        add_btn.grid(row=0,column=0,padx=1)

        update_btn=Button(btn_frame,text="UPDATE",command=self.update,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        update_btn.grid(row=0,column=1,padx=1)

        del_btn=Button(btn_frame,text="DELETE",command=self.mDelete,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        del_btn.grid(row=0,column=2,padx=1)

        res_btn=Button(btn_frame,text="RESET",command=self.reset,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        res_btn.grid(row=0,column=3,padx=1)

        #==========================table frame=====================================
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"))
        table_frame.place(x=435,y=50,width=860,height=465)

        lblsearch=Label(table_frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
        lblsearch.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()

        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("times new roman",12,"bold"),width=15,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1)

        self.txt_search=StringVar()

        txt_serach=ttk.Entry(table_frame,textvariable=self.txt_search,font=("times new roman",13,"bold"),width=15)
        txt_serach.grid(row=0,column=2,padx=2)

        

        


        serby_btn=Button(table_frame,text="Search",command=self.search,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        serby_btn.grid(row=0,column=3,padx=1)

        show_btn=Button(table_frame,text="Show",command=self.fetch_data,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        show_btn.grid(row=0,column=4,padx=1)

        #=======show data tabe=======
        
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=600,height=320)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref",text="Refer No")
        self.cust_details_table.heading("name",text="Name")
        self.cust_details_table.heading("mother",text="Mother Name")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("post",text="post")
        self.cust_details_table.heading("mobile",text="Mobile")
        self.cust_details_table.heading("email",text="Email")
        self.cust_details_table.heading("nationality",text="Nationality")
        self.cust_details_table.heading("idproof",text="Id Proof")
        self.cust_details_table.heading("idnumber",text="Id Number") 
        self.cust_details_table.heading("address",text="Address")

        self.cust_details_table["show"]="headings"
        self.cust_details_table.pack(fill=BOTH,expand=1) 

        
        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name",width=100)
        self.cust_details_table.column("mother",width=100)
        self.cust_details_table.column("gender",width=100)
        self.cust_details_table.column("post",width=100)
        self.cust_details_table.column("mobile",width=100)
        self.cust_details_table.column("email",width=100)
        self.cust_details_table.column("nationality",width=100)
        self.cust_details_table.column("idproof",width=100)
        self.cust_details_table.column("idnumber",width=100) 
        self.cust_details_table.column("address",width=100)

        self.cust_details_table.pack(fill=BOTH,expand=1)

        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
        
        

    def add_data(self):
        if self.var_mob.get()=="" or self.var_mother_name.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                              self.var_ref.get(),
                                                              self.var_cust_name.get(),
                                                              self.var_mother_name.get(),
                                                              self.var_gender.get(),
                                                              self.var_post.get(),
                                                              self.var_mob.get(),
                                                              self.var_mail.get(),
                                                              self.var_nation.get(),
                                                              self.var_proof.get(),
                                                              self.var_id.get(),
                                                              self.var_addr.get()
                                                            ))
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
               messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)


     #==========================fetching room details===========================================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #===============================get focus===================================================
    def get_cursor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mob.set(row[5]),
        self.var_mail.set(row[6]),
        self.var_nation.set(row[7]),
        self.var_proof.set(row[8])
        self.var_id.set(row[9])
        self.var_addr.set(row[10])
        




   
  #==============================for updating==========================================
    def update(self):
        if self.var_mob.get()=="":
            messagebox.showerror("Error","please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,Post=%s,Mobile=%s,Email=%s ,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s where Ref=%s",(
                                                                                               
                                                                                                self.var_cust_name.get(),
                                                                                                self.var_mother_name.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_post.get(),
                                                                                                self.var_mob.get(),
                                                                                                self.var_mail.get(),
                                                                                                self.var_nation.get(),
                                                                                                self.var_proof.get(),
                                                                                                self.var_id.get(),
                                                                                                self.var_addr.get(),
                                                                                                self.var_ref.get()
                                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)

   
#    #========================================for deleting====================================
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #====================================reset all=======================================
    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother_name.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mob.set(""),
        self.var_mail.set(""),
        #self.var_nation.set(""),
        #self.var_proof.set(""),
        self.var_id.set(""),
        self.var_addr.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

     
     
    def search(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
            my_cursor=conn.cursor()

            my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%' ")

            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.cust_details_table.delete(*self.cust_details_table.get_children())
                for i in rows:
                    self.cust_details_table.insert("",END,values=i)
                conn.commit()
            conn.close()        
   
      

       
     
        

if __name__ == "__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()