from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry('1050x500+230+200')


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

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=410,height=300)

        #=============================labels and entry===================

        #floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        self.var_floor=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("times new roman",13,"bold"),width=25)
        enty_floor.grid(row=0,column=1)
        
        #room no
        room_no=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        room_no.grid(row=1,column=0,sticky=W)
         
        self.var_roomNo=StringVar()
        enty_no=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,font=("times new roman",13,"bold"),width=25)
        enty_no.grid(row=1,column=1)

        #roomtype

        room_type=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        room_type.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        enty_room_type=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,font=("times new roman",13,"bold"),width=25)
        enty_room_type.grid(row=2,column=1)


         #===============================btns=========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=180,width=410,height=39)

        add_btn=Button(btn_frame,text="ADD",command=self.add_details,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        add_btn.grid(row=0,column=0,padx=1)

        update_btn=Button(btn_frame,text="UPDATE",command=self.update,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        update_btn.grid(row=0,column=1,padx=1)

        del_btn=Button(btn_frame,text="DELETE",command=self.mDelete,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        del_btn.grid(row=0,column=2,padx=1)

        res_btn=Button(btn_frame,text="RESET",command=self.reset,width=10,font=("arial",11,"bold"),bg="black",fg="gold")
        res_btn.grid(row=0,column=3,padx=1)

         #==========================table frame=====================================
        detail_table=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"))
        detail_table.place(x=459,y=50,width=500,height=300)

        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
        
        self.detailroom_table=ttk.Treeview(detail_table,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.detailroom_table.xview)
        scroll_y.config(command=self.detailroom_table.yview)

        self.detailroom_table.heading("floor",text="Floor")
        self.detailroom_table.heading("roomno",text="Room No")
        self.detailroom_table.heading("roomtype",text="RoomType")
        

        self.detailroom_table["show"]="headings"
        self.detailroom_table.pack(fill=BOTH,expand=1) 
 
        self.detailroom_table.column("floor",width=100)
        self.detailroom_table.column("roomno",width=100)
        self.detailroom_table.column("roomtype",width=100)
        

        self.detailroom_table.pack(fill=BOTH,expand=1)

        self.detailroom_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
        

        #==================================adding room data========================
    def add_details(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                              self.var_floor.get(),
                                                              self.var_roomNo.get(),
                                                              self.var_RoomType.get()
                                                            ))
               conn.commit()
               #self.fetch_data()
               conn.close()
               messagebox.showinfo("Success!","New Room has been added",parent=self.root)
            except Exception as es:
               messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)

    
        #===============================display data on show frame===========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.detailroom_table.delete(*self.detailroom_table.get_children())
            for i in rows:
                self.detailroom_table.insert("",END,values=i)
            conn.commit()
        conn.close()


        #======================================get focus==================================
    def get_cursor(self,event=""):
        cursor_row=self.detailroom_table.focus()
        content=self.detailroom_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_RoomType.set(row[2])




        #=========================update data ===========================
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                                                                           
                                                self.var_floor.get(),
                                                
                                                self.var_RoomType.get(),
                                                self.var_roomNo.get(),
                                                 ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

          
          #======================================delete==========================================
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete details this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Ghadge@169",database="management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
         

         #================================resetting data=================================
    def reset(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")


    

       










if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()              