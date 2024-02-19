from tkinter import Tk,Frame,Label,Entry,Button,messagebox
from PIL import Image,ImageTk

fonts = ('Courier New', 13, 'bold')
fonts1 = ('Courier New', 17, 'bold')
admin = 'a'
password = '1'
student = 's'
password1 = 'st'
book= 'p'

root = Tk()

class Home:
    def __init__(self,root):
        self.root=root
        self.root.title("HOME")
        self.page = Frame(self.root,width=600,height=400)
        self.page.place(x=0,y=0)

        self.image = Image.open('../assets/png1.png')
        self.image = self.image.resize((600,400))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page,image=self.image)
        self.image_label.place(x=0,y=0)

        self.main_label = Label(self.page , text = 'WELCOME', font = fonts1)
        self.main_label.place(x=235,y=50)
        self.main_label2 = Label(self.page , text = "Lock in your reservations early with SVECW E-Portal" , font = fonts)
        self.main_label2.place(x=50,y=110)
        self.main_label_btn = Button(self.page,text='ENTER',font=fonts1,command=self.home_login)
        self.main_label_btn.place(x=240,y=200)


    def home_login(self):    
        self.page.destroy()
        home_obj = Main(root)



class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN PAGE")
        self.right =Frame(self.root,width = 600, height = 400,bg='darkseagreen1')
        self.right.place(x = 0, y = 0 )

        
        self.admin_logo = Image.open('../assets/ai.png')
        self.admin_logo = self.admin_logo.resize((100, 100))

        self.admin_logo = ImageTk.PhotoImage(self.admin_logo)

        self.admin_logo_lbl = Label(self.right, image = self.admin_logo)
        self.admin_logo_lbl.place(x = 100, y= 30)



       
        self.admin__login = Label(self.right,text="Admin login")
        self.admin__login.place(x=100,y=125) 
        self.admin_name = Label(self.right, text = 'USER ID', bg = 'steel blue', fg ='white', font = fonts,width = 9)
        self.admin_name.place(x = 50, y = 170)
        self.admin_name_entry = Entry(self.right, width = 10, font = fonts)
        self.admin_name_entry.place(x = 150, y = 170)
        self.admin_pass = Label(self.right, text = 'PASSWORD', bg = 'steel blue', fg ='white', font = fonts, width = 9)
        self.admin_pass.place(x = 50, y = 200)
        self.admin_pass_entry = Entry(self.right, width = 10, font = fonts)
        self.admin_pass_entry.place(x = 150, y = 200)

        self.admin_login_btn = Button(self.right, text = 'LOGIN', font = fonts, command = self.admin_login)
        self.admin_login_btn.place(x = 100, y = 250)


        self.left =Frame(self.root, width = 600, height = 400,bg='darkseagreen1')
        self.left.place(x = 250, y = 0 )
        
        
      
        self.student_logo = Image.open('../assets/si.png')
        self.student_logo = self.student_logo.resize((100, 100))

        self.student_logo = ImageTk.PhotoImage(self.student_logo)

        self.student_logo_lbl = Label(self.left, image = self.student_logo)
        self.student_logo_lbl.place(x = 100, y= 30)



        self.student__login = Label(self.left,text="Student login")
        self.student__login.place(x=100,y=125) 


        self.student_name = Label(self.left, text = 'USER ID', bg = 'steel blue', fg ='white', font = fonts,width=9)
        self.student_name.place(x = 50, y = 170)
        self.student_name_entry = Entry(self.left, width = 10, font = fonts)
        self.student_name_entry.place(x = 150, y = 170)

        self.student_pass = Label(self.left, text = 'PASSWORD', bg = 'steel blue', fg ='white', font = fonts, width = 9)
        self.student_pass.place(x = 50, y = 200)
        self.student_pass_entry = Entry(self.left, width = 10, font = fonts)
        self.student_pass_entry.place(x = 150, y = 200)

        self.student_login_btn = Button(self.left, text = 'LOGIN', font = fonts,command = self.student_login)
        self.student_login_btn.place(x = 100, y = 250)
    

    def admin_login(self):
        global admin, password
        self.a_name = self.admin_name_entry.get()
        self.a_pass = self.admin_pass_entry.get()
        if self.a_name == admin:
            if self.a_pass == password:
                self.right.destroy()
                self.left.destroy()
                admin_obj = Admin(root)
            else:
                messagebox.showerror('INVALID','INCORRECT PASSWORD')
        else:
                messagebox.showerror('INVALID','USER ID INVALID')



    def student_login(self):
        global student, password1
        self.b_name = self.student_name_entry.get()
        self.b_pass = self.student_pass_entry.get()
        if self.b_name == student:
            if self.b_pass == password1:
                self.right.destroy()
                self.left.destroy()
                student_obj = Student(root)
            else:
                messagebox.showerror('INVALID','INCORRECT PASSWORD')
        else:
                messagebox.showerror('INVALID','USER ID INVALID')
      

class Admin:
    def __init__(self, root):
        self.root = root
        self.root.title("ADMIN DASHBOARD")
        self.right = Frame(self.root, width = 600, height = 400)
        self.right.place(x = 0, y = 0)

        self.student__login = Label(self.right,text="WELCOME TO SVECW E - BOOKING PORTAL",fg='black',font=fonts)
        self.student__login.place(x=100,y=30)
        self.add_book_btn = Button(self.right,text = 'STUDENT DETAILS', font = fonts,bg='black',fg='white',width=20,command=self.student1)
        self.add_book_btn.place(x = 160, y = 100)
        self.add_book_btn = Button(self.right,text = 'ADD BOOK DETAILS', font = fonts,bg='black',fg='white',width=20,command=self.add_book )
        self.add_book_btn.place(x = 160, y = 135)
        self.add_book_btn = Button(self.right,text = 'DELETE BOOK', font = fonts,bg='black',fg='white',width=20,command=self.delete)
        self.add_book_btn.place(x = 160, y = 170)
        self.add_book_btn = Button(self.right,text = 'ISSUE/RETURN BOOK', font = fonts,bg='black',fg='white' ,width=20,command=self.issue_return)
        self.add_book_btn.place(x = 160, y = 205)
        self.add_book_btn = Button(self.right,text = 'PRE-BOOKING REQUEST', font = fonts,bg='black',fg='white',width=20,command=self.pre_request)
        self.add_book_btn.place(x = 160, y = 240)
        

        

    def student1(self):    
        self.right.destroy()
        Admin_obj = Std(root)

    def add_book(self):    
        self.right.destroy()
        Admin_obj = Add(root)

    def delete(self):    
        self.right.destroy()
        Admin_obj = Delete(root)

    def issue_return(self):    
        self.right.destroy()
        Admin_obj = Issue(root)

    def pre_request(self):    
        self.right.destroy()
        Admin_obj = Request(root)

class Add:
     def __init__(self, root):
        self.root = root
        self.root.title("Book Details")
        self.page = Frame(self.root, width = 600, height = 400,bg='darksalmon')
        self.page.place(x = 0, y = 0)

        self.book__details = Label(self.page,text="BOOK DETAILS",fg='red',font=fonts1)
        self.book__details.place(x=200,y=40)

        self.book_id = Label(self.page, text = 'BOOK ID:',fg ='black', font = fonts,width=11)
        self.book_id.place(x = 100, y = 140)
        self.book_id_entry = Entry(self.page,width=20, font = fonts)
        self.book_id_entry.place(x = 250, y = 140)
        self.book_title= Label(self.page, text = 'Book Name:',fg ='black', font = fonts,width=11)
        self.book_title.place(x = 100, y = 190)
        self.book_title_entry = Entry(self.page,width=20, font = fonts)
        self.book_title_entry.place(x = 250, y = 190)
        self.book_author= Label(self.page, text = 'AUTHOR:',fg ='black', font = fonts,width=11)
        self.book_author.place(x = 100, y = 240)
        self.book_author_entry = Entry(self.page,width=20, font = fonts)
        self.book_author_entry.place(x = 250, y = 240)
        self.book_status= Label(self.page, text = 'STATUS:',fg ='black', font = fonts,width=11)
        self.book_status.place(x = 100, y = 290)
        self.book_status_entry = Entry(self.page,width=20, font = fonts)
        self.book_status_entry.place(x = 250, y = 290)



class Std:
     def __init__(self, root):
        self.root = root
        self.root.title("STUDENT DETAILS")
        self.page = Frame(self.root, width = 600, height = 400)
        self.page.place(x = 0, y = 0)

class Delete:
     def __init__(self, root):
        self.root = root
        self.root.title("DELETE BOOK")
        self.page = Frame(self.root, width = 600, height = 400)
        self.page.place(x = 0, y = 0)

class Issue:
     def __init__(self, root):
        self.root = root
        self.root.title("ISSUE OR RETURN BOOK")
        self.page = Frame(self.root, width = 600, height = 400)
        self.page.place(x = 0, y = 0)

class Request:
     def __init__(self, root):
        self.root = root
        self.root.title("PRE-BOOKING REQUEST")
        self.page = Frame(self.root, width = 600, height = 400)
        self.page.place(x = 0, y = 0)


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title('STUDENT DASHBOARD')
        self.left = Frame(self.root, width = 600, height = 400)
        self.left.place(x = 0, y = 0)


        self.image = Image.open('../assets/b2.png')
        self.image = self.image.resize((600,400))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.left,image=self.image)
        self.image_label.place(x=0,y=0)



        self.student__login = Label(self.left,text="HELLO ENTHUSIASTS!",fg='red',font=fonts1)
        self.student__login.place(x=200,y=40)

        self.book_name = Label(self.left, text = 'Enter a Book Name:',fg ='black', font = fonts)
        self.book_name.place(x = 100, y = 140)
        self.book_name_entry = Entry(self.left,width=20, font = fonts)
        self.book_name_entry.place(x = 300, y = 140)
        

        self.book_submit_btn = Button(self.left,text = 'SUBMIT', font = fonts,command=self.book_submit )
        self.book_submit_btn.place(x = 250, y = 220)

    def book_submit(self):
        global book 
        self.c_name = self.book_name_entry.get()
        if self.c_name == book:
            self.left.destroy()
            book_obj = Book(root)
        else:
            messagebox.showerror('INVALID','Invalid Book Name')
        

class Book:
    def __init__(self,root):
        self.root = root
        self.root.title('BOOK')
        self.left = Frame(self.root, width = 600, height = 400,bg='beige')
        self.left.place(x = 0, y = 0)
        self.book_name = Label(self.left, text = 'Title',font=fonts,fg='black')
        self.book_name.place(x = 50, y = 140)
        self.book_name = Label(self.left, text = 'Book Status :',font=fonts,fg='black')
        self.book_name.place(x = 50, y = 200)
      
        self.book_name = Label(self.left, text = 'Available',font=fonts,fg='black')
        self.book_name.place(x = 200, y = 200)
        self.book_now_btn = Button(self.left,text = 'Book Now', font = fonts,bg='red',fg='white',command=self.book_now )
        self.book_now_btn.place(x = 350, y = 200) 
        self.book_name = Label(self.left, text = 'Unavailable',font=fonts,fg='black')
        self.book_name.place(x = 200, y = 300)
        self.book_now_btn = Button(self.left,text = 'Make a Request', font = fonts,bg='red',fg='white',command=self.request_now)
        self.book_now_btn.place(x = 350, y = 300) 
           
        
    
    
    
    def book_now(self):
        messagebox.askyesno('BOOK NOW','Confirm Booking')
    

    def request_now(self):
        messagebox.askyesno('MAKE REQUEST','Confirm Request')
   


root.geometry('600x400+550+200')
home = Home(root)
root.mainloop()
