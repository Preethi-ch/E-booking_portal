from tkinter import Tk, Frame, Label, Entry, Button, messagebox,ttk,Scrollbar,VERTICAL, HORIZONTAL
from PIL import Image, ImageTk
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lalitha@1310",
    database="library_database"
)
mycursor = mydb.cursor()



fonts = ('Courier New', 13, 'bold')
fonts1 = ('Courier New', 17, 'bold')

root = Tk()


class welcome_page:
    def __init__(self, root):
        self.root = root
        self.root.title("HOME")
        self.page = Frame(self.root, width=600, height=400)
        self.page.place(x=0, y=0)

        self.image = Image.open('../assets/cover.png')
        self.image = self.image.resize((600, 400))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page, image=self.image)
        self.image_label.place(x=0, y=0)

        self.main_label_btn = Button(self.page, text='Let\'s Dive', font=fonts1, command=self.home_login,
                                     bg="aquamarine3", fg="white")
        self.main_label_btn.place(x=100, y=290)

    def home_login(self):
        self.page.destroy()
        home_obj = Login_page(root)


class Login_page:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN PAGE")
        self.right = Frame(self.root, width=600, height=400, bg='darkseagreen1')
        self.right.place(x=0, y=0)

        self.admin_logo = Image.open('../assets/ai.png')
        self.admin_logo = self.admin_logo.resize((100, 100))
        self.admin_logo = ImageTk.PhotoImage(self.admin_logo)
        self.admin_logo_lbl = Label(self.right, image=self.admin_logo)
        self.admin_logo_lbl.place(x=100, y=30)

        self.admin__login = Label(self.right, text="Admin login")
        self.admin__login.place(x=100, y=125)
        self.admin_name = Label(self.right, text='USER ID', bg='steel blue', fg='white', font=fonts, width=9)
        self.admin_name.place(x=50, y=170)
        self.admin_name_entry = Entry(self.right, width=10, font=fonts)
        self.admin_name_entry.place(x=150, y=170)
        self.admin_pass = Label(self.right, text='PASSWORD', bg='steel blue', fg='white', font=fonts, width=9)
        self.admin_pass.place(x=50, y=200)
        self.admin_pass_entry = Entry(self.right, width=10, font=fonts)
        self.admin_pass_entry.place(x=150, y=200)

        self.admin_login_btn = Button(self.right, text='LOGIN', font=fonts, command=self.admin_login)
        self.admin_login_btn.place(x=100, y=250)

        self.left = Frame(self.root, width=600, height=400, bg='darkseagreen1')
        self.left.place(x=250, y=0)

        self.student_logo = Image.open('../assets/si.png')
        self.student_logo = self.student_logo.resize((100, 100))
        self.student_logo = ImageTk.PhotoImage(self.student_logo)
        self.student_logo_lbl = Label(self.left, image=self.student_logo)
        self.student_logo_lbl.place(x=100, y=30)

        self.student__login = Label(self.left, text="Student login")
        self.student__login.place(x=100, y=125)

        self.student_name = Label(self.left, text='USER ID', bg='steel blue', fg='white', font=fonts, width=9)
        self.student_name.place(x=50, y=170)
        self.student_name_entry = Entry(self.left, width=10, font=fonts)
        self.student_name_entry.place(x=150, y=170)

        self.student_pass = Label(self.left, text='PASSWORD', bg='steel blue', fg='white', font=fonts, width=9)
        self.student_pass.place(x=50, y=200)
        self.student_pass_entry = Entry(self.left, width=10, font=fonts)
        self.student_pass_entry.place(x=150, y=200)

        self.student_login_btn = Button(self.left, text='LOGIN', font=fonts, command=self.student_login)
        self.student_login_btn.place(x=100, y=250)

    def admin_login(self):
        self.b_name = self.admin_name_entry.get()
        self.b_pass = self.admin_pass_entry.get()

        # Query to check if admin credentials exist in the database
        mycursor.execute("SELECT * FROM admin WHERE userid= %s AND password = %s", (self.b_name, self.b_pass))
        admin_data = mycursor.fetchone()

        if admin_data:
            self.right.destroy()
            self.left.destroy()
            admin_obj = Admin_page(root, self.b_name)
        else:
            messagebox.showerror('INVALID', 'Invalid UserID or Password')

    def student_login(self):
        self.b_name = self.student_name_entry.get()
        self.b_pass = self.student_pass_entry.get()

        mycursor.execute("SELECT * FROM Student WHERE userid= %s AND password = %s", (self.b_name, self.b_pass))
        student_data = mycursor.fetchone()

        if student_data:
            self.right.destroy()
            self.left.destroy()
            student_obj = Student_page(root)
        else:
            messagebox.showerror('INVALID', 'Invalid UserID or Password')


class Admin_page:
    def __init__(self, root, admin_id):
        self.root = root
        self.root.title("ADMIN DASHBOARD")
        self.right = Frame(self.root, width=600, height=400)
        self.right.place(x=0, y=0)
        self.image = Image.open('../assets/admin_space_home.png')
        self.image = self.image.resize((600, 400))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.right, image=self.image)
        self.image_label.place(x=0, y=0)

        self.profile_image = Image.open('../assets/profile1.png')
        self.profile_image = self.profile_image.resize((50, 50))
        self.profile_photo = ImageTk.PhotoImage(self.profile_image)
        self.profile_button = Button(self.right, image=self.profile_photo, bg='gray', bd=0,
                                     command=lambda: self.profile(admin_id))
        self.profile_button.place(x=548, y=2)


        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.right, image=self.back_image, bg='gray', bd=0)
        self.back_button.image=self.back_image
        self.back_button.place(x=10, y=340)
        self.back_button.bind('<Button-1>',self.go_back)
                              


        self.add_book_btn = Button(self.right, text='STUDENT DETAILS', font=fonts, bg='firebrick', fg='white',
                                   width=20, command=self.student1)
        self.add_book_btn.place(x=80, y=140)
        self.add_book_btn = Button(self.right, text='ADD BOOK DETAILS', font=fonts, bg='firebrick', fg='white',
                                   width=20, command=self.add_book)
        self.add_book_btn.place(x=80, y=190)
        self.add_book_btn = Button(self.right, text='DELETE BOOK', font=fonts, bg='firebrick', fg='white', width=20,
                                   command=self.delete)
        self.add_book_btn.place(x=80, y=240)
        self.add_book_btn = Button(self.right, text='ISSUE/RETURN BOOK', font=fonts, bg='firebrick', fg='white',
                                   width=20, command=self.issue_return)
        self.add_book_btn.place(x=80, y=290)
        self.add_book_btn = Button(self.right, text='PRE-BOOKING REQUEST', font=fonts, bg='firebrick', fg='white',
                                   width=20, command=self.pre_request)
        self.add_book_btn.place(x=80, y=340)

    
    def go_back(self,event):    
        self.right.destroy()
        Admin_obj=Login_page(root)


    def profile(self, admin_id):
        self.right.destroy()
        Admin_obj = profile_page(root, admin_id)

    def student1(self):
        self.right.destroy()
        Admin_obj = Std_page(root)

    def add_book(self):
        self.right.destroy()
        Admin_obj = Add_page(root)

    def delete(self):
        self.right.destroy()
        Admin_obj = Delete_page(root)

    def issue_return(self):
        self.right.destroy()
        Admin_obj = Issue_page(root)

    def pre_request(self):
        self.right.destroy()
        Admin_obj = Request_page(root)


class profile_page(Login_page):
    def __init__(self, root, admin_id):
        self.root = root
        self.root.title("Profile page")
        self.page = Frame(self.root, width=600, height=400)
        self.page.place(x=0, y=0)

        self.image = Image.open('../assets/profilebg.png')
        self.image = self.image.resize((600,400))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page,image=self.image)
        self.image_label.image=self.image
        self.image_label.place(x=0,y=0)


        mycursor.execute("SELECT * FROM admin WHERE userid= %s", (admin_id,))
        admin_data = mycursor.fetchone()

        if admin_data:
            admin_user_label = Label(self.page, text=f"Userid: {admin_data[0]}", font=fonts)
            admin_user_label.place(x=230, y=210)

            admin_name_label = Label(self.page, text=f"Name: {admin_data[2]}", font=fonts)
            admin_name_label.place(x=230, y=240)

            admin_email_label = Label(self.page, text=f"Email: {admin_data[3]}", font=fonts)
            admin_email_label.place(x=230, y=270)

            admin_phone_label = Label(self.page, text=f"Phone number: {admin_data[4]}", font=fonts)
            admin_phone_label.place(x=230, y=300)



class Add_page:
     def __init__(self, root):
        self.root = root
        self.root.title("Book Details")
        self.page = Frame(self.root, width = 600, height = 400,bg='darksalmon')
        self.page.place(x = 0, y = 0)

        self.book__details = Label(self.page,text="BOOK DETAILS",fg='red',font=fonts1)
        self.book__details.place(x=200,y=40)

        self.book_id = Label(self.page, text = 'BOOK ID:',fg ='black', font = fonts,width=11)
        self.book_id.place(x = 100, y = 100)
        self.book_id_entry = Entry(self.page,width=20, font = fonts)
        self.book_id_entry.place(x = 250, y = 100)

        self.book_title= Label(self.page, text = 'Book Name:',fg ='black', font = fonts,width=11)
        self.book_title.place(x = 100, y = 140)
        self.book_title_entry = Entry(self.page,width=20, font = fonts)
        self.book_title_entry.place(x = 250, y = 140)

        self.book_author= Label(self.page, text = 'AUTHOR:',fg ='black', font = fonts,width=11)
        self.book_author.place(x = 100, y = 180)
        self.book_author_entry = Entry(self.page,width=20, font = fonts)
        self.book_author_entry.place(x = 250, y = 180)

        self.book_edition= Label(self.page, text = 'Edition:',fg ='black', font = fonts,width=11)
        self.book_edition.place(x = 100, y = 220)
        self.book_edition_entry = Entry(self.page,width=20, font = fonts)
        self.book_edition_entry.place(x = 250, y = 220)

        self.book_status= Label(self.page, text = 'STATUS:',fg ='black', font = fonts,width=11)
        self.book_status.place(x = 100, y = 260)
        self.book_status_entry = Entry(self.page,width=20, font = fonts)
        self.book_status_entry.place(x = 250, y = 260)

        self.save_button = Button(self.page, text="Save", command=self.save_to_database)
        self.save_button.place(x=250, y=300)

     def save_to_database(self):
        book_id = self.book_id_entry.get()
        book_title = self.book_title_entry.get()
        book_author = self.book_author_entry.get()
        book_edition = self.book_edition_entry.get()
        book_status = self.book_status_entry.get()


        query = "INSERT INTO books (bid, book_title,author,edition,status) VALUES (%s, %s, %s, %s,%s)"
        values = (book_id, book_title, book_author,book_edition, book_status)
        mycursor.execute(query, values)

        mydb.commit()
        mydb.close()

        self.book_id_entry.delete(0, 'end')
        self.book_title_entry.delete(0, 'end')
        self.book_author_entry.delete(0, 'end')
        self.book_edition_entry.delete(0, 'end')
        self.book_status_entry.delete(0, 'end')

        



class Std_page:
    def __init__(self, root):
        self.root = root
        self.root.title("STUDENT DETAILS")
        self.page = Frame(self.root, width=600, height=400)
        self.page.place(x=0, y=0)


        self.tree = ttk.Treeview(self.page, columns=('ID', 'Name', 'Email', 'Branch Name', 'Phone Number'), show='headings', height=15)
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Email', text='Email') 
        self.tree.heading('Branch Name', text='Branch') 
        self.tree.heading('Phone Number', text='Phone no')
        
        self.tree.column('ID', width=90, anchor='center')  
        self.tree.column('Name', width=150, anchor='center') 
        self.tree.column('Email', width=200, anchor='center')  
        self.tree.column('Branch Name', width=50, anchor='center')  
        self.tree.column('Phone Number', width=100, anchor='center')  
        self.tree.pack(pady=40)

        
        v_scrollbar = Scrollbar(self.page, orient=VERTICAL, command=self.tree.yview)
        v_scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=v_scrollbar.set)

     
        h_scrollbar = Scrollbar(self.page, orient=HORIZONTAL, command=self.tree.xview)
        h_scrollbar.pack(side="bottom", fill="x")
        self.tree.configure(xscrollcommand=h_scrollbar.set)

        
        mycursor.execute("SELECT * FROM student")
        student_data = mycursor.fetchall()

        
        for data in student_data:
            self.tree.insert('', 'end', values=data)



class Delete_page:
    def __init__(self, root):
        self.root = root
        self.root.title("DELETE BOOK")
        self.page = Frame(self.root, width=600, height=400,bg='darksalmon')
        self.page.place(x=0, y=0)



class Issue_page:
    def __init__(self, root):
        self.root = root
        self.root.title("ISSUE OR RETURN BOOK")
        self.page = Frame(self.root, width=600, height=400)
        self.page.place(x=0, y=0)


class Request_page:
    def __init__(self, root):
        self.root = root
        self.root.title("PRE-BOOKING REQUEST")
        self.page = Frame(self.root, width=600, height=400)
        self.page.place(x=0, y=0)


class Student_page:
    def __init__(self, root):
        self.root = root
        self.root.title('STUDENT DASHBOARD')
        self.left = Frame(self.root, width=600, height=400)
        self.left.place(x=0, y=0)


        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.left, image=self.back_image, bg='gray', bd=0)
        self.back_button.image=self.back_image
        self.back_button.place(x=10, y=340)
        self.back_button.bind('<Button-1>',self.go_back)
                              

        self.student__login = Label(self.left, text="HELLO ENTHUSIASTS!", fg='red', font=fonts1)
        self.student__login.place(x=150, y=40)

        self.history_btn = Button(self.left, text='Book Store', font=fonts, command=self.book_store_next, width=15)
        self.history_btn.place(x=200, y=150)

        self.book_store_btn = Button(self.left, text='Request Status', font=fonts, command=self.request_status_next,
                                      width=15)
        self.book_store_btn.place(x=200, y=200)

        self.book_store_btn = Button(self.left, text='Wishlist', font=fonts, command=self.wishlist_next, width=15)
        self.book_store_btn.place(x=200, y=250)

       
    def wishlist_next(self):
        self.left.destroy()
        wishlist_obj = Wishlist_page(root)

    def request_status_next(self):
        self.left.destroy()
        request_status_obj = Request_status_page(root)

    def book_store_next(self):
        self.left.destroy()
        store_obj = book_store_page(root)

    def go_back(self,event):    
        self.left.destroy()
        std_obj=Login_page(root)


class Wishlist_page:
    def __init__(self, root):
        self.root = root
        self.root.title("WISHLIST")
        self.page = Frame(self.root, width=600, height=400)
        self.page.place(x=0, y=0)


class Request_status_page:
    def __init__(self, root):
        self.root = root
        self.root.title("REQUEST STATUS")
        self.page = Frame(self.root, width=600, height=400)
        self.page.place(x=0, y=0)


class book_store_page:
    def __init__(self, root):
        self.root = root
        self.root.title("BOOK STORE")
        self.left = Frame(self.root, width=600, height=400)
        self.left.place(x=0, y=0)


root.geometry('600x400+550+200')
home = welcome_page(root)
root.mainloop()