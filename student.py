from tkinter import *
from tkinter import ttk
import pymysql


class Student:
    def __init__(self, root):
        self.root = root  # init cons
        self.root.title("Student DBMS")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Managment System", bd=10,relief=GROOVE, font=("times new roman",40,"bold"), bg="RoyalBlue4", fg="black")
        title.pack(side=TOP,fill=X)

        #=========All variables================
        self.Roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.Address=StringVar()


        #======Main frame=======
        Manage_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="RoyalBlue4")
        Manage_Frame.place(x=20, y=100, width=450, height=590) 

        m_title=Label(Manage_Frame, text="Manage Students", font=("times new roman",30,"bold"), bg="RoyalBlue4", fg="black")
        m_title.grid(row=0, columnspan=2, pady=20) #grid precise > place

        lbl_roll=Label(Manage_Frame, text="Roll No.", font=("times new roman",20,"bold"), bg="RoyalBlue4", fg="black")
        lbl_roll.grid(row=1, column=0, pady=10, padx=10, sticky="w") #w=west
        txt_Roll=Entry(Manage_Frame, textvariable=self.Roll_no_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name=Label(Manage_Frame, text="Name", font=("times new roman",20,"bold"), bg="RoyalBlue4", fg="black")
        lbl_name.grid(row=2, column=0, pady=10, padx=10, sticky="w") 
        txt_name=Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email=Label(Manage_Frame, text="Email", font=("times new roman",20,"bold"), bg="RoyalBlue4", fg="black")
        lbl_Email.grid(row=3, column=0, pady=10, padx=10, sticky="w") 
        txt_Email=Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender=Label(Manage_Frame, text="Gender", font=("times new roman",20,"bold"), bg="RoyalBlue4", fg="black")
        lbl_Gender.grid(row=4, column=0, pady=10, padx=10, sticky="w") 
        combo_Gender=ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman",15,"bold"),state='readonly')
        combo_Gender['values']=("Male", "Female", "Other")
        combo_Gender.grid(row=4, column=1, padx=20, pady=10)    #comboBox = dropdown

        lbl_Contact=Label(Manage_Frame, text="Contact", font=("times new roman",20,"bold"), bg="RoyalBlue4", fg="black")
        lbl_Contact.grid(row=5, column=0, pady=10, padx=10, sticky="w") 
        txt_Contact=Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_Dob=Label(Manage_Frame, text="DOB(d/m/y)", font=("times new roman",20,"bold"), bg="RoyalBlue4", fg="black")
        lbl_Dob.grid(row=6, column=0, pady=10, padx=10, sticky="w") 
        txt_Dob=Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address=Label(Manage_Frame, text="Address", font=("times new roman",20,"bold"), bg="RoyalBlue4", fg="black")
        lbl_Address.grid(row=7, column=0, pady=10, padx=10, sticky="w")
        self.txt_Address=Text(Manage_Frame, width=15, height=2, font=("times new roman",20,"bold"))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        #============Button Frame in Manage Frame========
        btn_Frame=Frame(Manage_Frame, bd=4, relief=RIDGE, bg="RoyalBlue4")
        btn_Frame.place(x=15, y=522, width=380)

        Addbtn=Button(btn_Frame, text="Add", width=6, command=self.add_students).grid(row=0, column=0, padx=10, pady=10)
        upadtebtn=Button(btn_Frame, text="Update", width=6, command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn=Button(btn_Frame, text="Delete", width=6, command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn=Button(btn_Frame, text="Clear", width=6, command=self.clear).grid(row=0, column=3, padx=10, pady=10)


        #======Detail frame=======
        Detail_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="RoyalBlue4")
        Detail_Frame.place(x=500, y=100, width=810, height=590) 

        lbl_search = Label(Detail_Frame, text="Search By", font=("times new roman",20,"bold"), bg="RoyalBlue4", fg="black")
        lbl_search.grid(row=0, column=0, padx=10, pady=20, sticky="w")
        combo_search=ttk.Combobox(Detail_Frame,width=10, font=("times new roman",15,"bold"),state='readonly')
        combo_search['values']=("Roll No.", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_Search=Entry(Detail_Frame, width=15, font=("times new roman",14,"bold"),bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn=Button(Detail_Frame,  text="Search",   font=("times new roman",14,"bold"), width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
        showallbtn=Button(Detail_Frame, text="Show All", font=("times new roman",14,"bold"), width=10, pady=5).grid(row=0, column=4, padx=10, pady=10)


        #============Table Frame===============
        Table_Frame=Frame(Detail_Frame, bd=4, relief=RIDGE, bg="RoyalBlue4")
        Table_Frame.place(x=10, y=70, width=770, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame, columns=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,  fill=Y)               # config after packing
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll", text="Roll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("Address", text="Address")

        self.Student_table['show']='headings' # to clear default show of index column
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("Address", width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor) # event handling
        self.fetch_data()


    def add_students(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="stm")
        command_handler=con.cursor()
        
        command_handler.execute("INSERT INTO students VALUES(%s, %s, %s, %s, %s, %s, %s)",(self.Roll_no_var.get(),
                                                                                        self.name_var.get(),
                                                                                        self.email_var.get(),
                                                                                        self.gender_var.get(),
                                                                                        self.contact_var.get(),
                                                                                        self.dob_var.get(),#txtadrs para line 1 to endline fetch data
                                                                                        self.txt_Address.get('1.0', END)
                                                                                        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def fetch_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="stm")
        command_handler=con.cursor()
        command_handler.execute("SELECT * FROM students ")
        rows=command_handler.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children()) # deletes all data in table
            for row in rows:
                self.Student_table.insert('',END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0", END) # clear data from ine1 to endline

    def get_cursor(self, ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0", END) # clear data from ine1 to endline
        self.txt_Address.insert(END, row[6])
       

    def update_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="stm")
        command_handler=con.cursor()
        command_handler.execute("UPDATE students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                                            self.name_var.get(),
                                                                                                            self.email_var.get(),
                                                                                                            self.gender_var.get(),
                                                                                                            self.contact_var.get(),
                                                                                                            self.dob_var.get(),
                                                                                                            self.txt_Address.get('1.0', END),
                                                                                                            self.Roll_no_var.get(),
                                                                                                                    ))
        
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    
    def delete_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="stm")
        command_handler=con.cursor()
        command_handler.execute("DELETE from students where roll_no=%s", self.Roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

root =Tk()
ob = Student(root)
root.mainloop()