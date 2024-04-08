import tkinter as tk
from tkinter import ttk
import mysql.connector
import tkinter.messagebox as tm


mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="123")

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE restaurant")
except:
    pass


mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="123",
     database="restaurant")

mycursor = mydb.cursor()

dishquery = "INSERT INTO dishes (DISHNAME, DISH_NO, DISH_PRICE) VALUES (%s,%s,%s)"

dishvalues = [
      ('French Fries', 1, 50),
      ('Veggie Burger', 2, 75),
      ('Aloo Tikki Burger', 3,75),
      ('Chicken King Burger', 4, 110),
      ('Onion Pizza', 5, 130),
      ('Corn Pizza', 6, 130),
      ('Loaded Pizza', 7, 175),
      ('Mexican Pizza', 8, 160),
      ('Red Sauce Pasta', 9, 100),
      ('White Sauce Pasta', 10, 100),
      ('Margherita Pizza', 11, 160),
      ('Choco Muffin', 12, 90),
      ('BreadSticks', 13, 80),
]    

offerquery = "INSERT INTO offers (OFFERNAME, DISCOUNT, OFFERDESC) VALUES (%s,%s,%s)"

offervalues = [
      (1, 20, 'HDFC Bank Offer'),
      (2, 25, 'Yes Bank Offer'),
      (3, 25, 'Axis Bank Offer'),
      (4, 50, 'PayTM Offer'),
      (5, 20, 'Restaurant Offer'),
]
employeequery = "INSERT INTO employees (FIRST_NAME, LAST_NAME, EMPLOYEE_ID, GENDER, DOB, SALARY) VALUES (%s,%s,%s,%s,%s,%s)"

employeevalues = [
      ('Jay', 'Sharma', 1, 'M', '22101996', '15000'),
      ('Hitesh', 'Jain', 2, 'M', '10071996', '17000'),
      ('Rupali', 'Gupta', 3, 'F', '17031997', '13000'),
      ('Yuvraj', 'Singh', 4, 'M', '28121998', '15750'),
      ('Shreya', 'Yadav', 5, 'F', '02091997', '18000'),
]
try:
    mycursor.execute("DROP TABLE orders")
except:
    pass
try:
    mycursor.execute("CREATE TABLE orders (FIRST_NAME VARCHAR(40),LAST_NAME VARCHAR(40), ORDER_NO INT UNIQUE, GENDER TEXT, PHONE_NO LONGTEXT, DISHNO INT, COST INT)")
except:
    pass
try:
    mycursor.execute("CREATE TABLE employees (FIRST_NAME VARCHAR(40),LAST_NAME VARCHAR(40), EMPLOYEE_ID INT UNIQUE, GENDER TEXT, DOB LONGTEXT, SALARY LONGTEXT)")
except:
    pass
try:
    mycursor.execute("CREATE TABLE dishes (DISHNAME VARCHAR(40),DISH_NO INT UNIQUE, DISH_PRICE LONGTEXT)")
except:
    pass
try:
    mycursor.execute("CREATE TABLE offers (OFFERNAME INT UNIQUE, DISCOUNT LONGTEXT, OFFERDESC VARCHAR(250))")
except:
    pass
try:
    mycursor.executemany(dishquery,dishvalues)
except:
    pass
try:
    mycursor.executemany(offerquery,offervalues)
except:
    pass
try:
    mycursor.executemany(employeequery,employeevalues)
except:
    pass


mydb.commit()
mydb.close()

def Greeting(msg):
    greet = tk.Tk()
    greet.wm_title("Python Restaurant")
    label = tk.Label(greet, text=msg, font='impact 15')
    label.pack(fill="x", pady=10)
    Button = tk.Button(greet, text="Enter",bg='brown', fg='white',  command = greet.destroy)
    Button.pack(side='bottom')
    greet.mainloop()

class BackEnd(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Python Restaurant")
        tk.Tk.wm_geometry(self, "800x600")
        tk.Tk.wm_resizable(self,0,0)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, WelcomePage, StartPage, OrderPage, CurOrderPage, OfferPage, DishPage, EmployeePage, SalesPage):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.pack_propagate(0)
        label_username = ttk.Label(self, text="Username", font='20')
        label_password = ttk.Label(self, text="Password", font='20')

        entry_username = ttk.Entry(self)
        entry_password = ttk.Entry(self, show="*")

        label_username.grid(row=0
                            )
        label_password.grid(row=1)
        entry_username.grid(row=0, column=1)
        entry_password.grid(row=1, column=1)

        checkbox = tk.Checkbutton(self, text="Keep me logged in")
        checkbox.grid(columnspan=2)
        def _login_btn_clicked():
            username = entry_username.get()
            password = entry_password.get()
            if username == "Manager" and password == "1234":
                controller.show_frame(WelcomePage)
            else:
                tm.showerror("Login error", "Incorrect username or password")
        
        LoginButton = ttk.Button(self, text="Login", command=_login_btn_clicked)
        LoginButton.grid(columnspan=2)

class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.pack_propagate(0)
        label = ttk.Label(self, text="Welcome Administator", font='impact')
        label.place(x=285, y=40)
        button = ttk.Button(self, text="Proceed",
                            command=lambda: controller.show_frame(StartPage))
        button.place(x=325, y=60)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.pack_propagate(0)
        label = tk.Label(self, text="Python Restaurant", font='impact 15')
        label.pack(pady=10,padx=10)
        F1=tk.Frame(self)
        F1.pack(side='left')
        F2=tk.Frame(self)
        F2.pack(side='right')
        
        button = ttk.Button(F1, text="Make Order",
                            command=lambda: controller.show_frame(OrderPage))
        button.pack(side = 'top')

        button2 = ttk.Button(F1, text="Current Orders",
                            command=lambda: controller.show_frame(CurOrderPage))
        button2.pack(side = 'top')

        button3 = ttk.Button(F1, text="Offers and Discounts",
                            command=lambda: controller.show_frame(OfferPage))
        button3.pack(side = 'top')
        
        button4 = ttk.Button(F2, text="Add/Delete Dishes",
                            command=lambda: controller.show_frame(DishPage))
        button4.pack(side = 'top')

        button5 = ttk.Button(F2, text="Employee Directory",
                            command=lambda: controller.show_frame(EmployeePage))
        button5.pack(side = 'top')

        button6 = ttk.Button(F2, text="Sales Today",
                            command=lambda: controller.show_frame(SalesPage))
        button6.pack(side = 'top')

        BigText1= tk.Label(self, text="Python",fg='#581845', font='impact 80')
        BigText1.pack()
        BigText2= tk.Label(self, text="Restaurant",fg='#581845', font='impact 80')
        BigText2.pack()
        MadeBy = ttk.Label(self, text = 'Made By Abhyudaya Soni', font='Helvetica 10')
        MadeBy.pack(side='bottom')
                

       

class OrderPage(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.propagate(0)
        label = tk.Label(self, text="Order Window", font='impact 15')
        label.grid(row=0, column = 9)
        ents1=tk.StringVar()
        ents2=tk.StringVar()
        ents3=tk.IntVar()
        ents4=tk.StringVar()
        ents5=tk.IntVar()
        ents6=tk.IntVar()
        lab1 = tk.Label(self, width=22, text="First Name : ", anchor='w')
        ent1 = ttk.Entry(self, textvariable=ents1)
        lab1.grid(row = 3, column = 3)
        ent1.grid(row = 4, column = 6)
        lab2 = tk.Label(self, width=22, text="Last Name : ", anchor='w')
        ent2 = ttk.Entry(self, textvariable=ents2)
        lab2.grid(row = 5, column = 3)
        ent2.grid(row = 6, column = 6)
        lab3 = tk.Label(self, width=22, text="Order no. : ", anchor='w')
        ent3 = ttk.Entry(self, textvariable=ents3)
        lab3.grid(row = 7, column = 3)
        ent3.grid(row = 8, column = 6)
        lab4 = tk.Label(self, width=22, text="Gender : ", anchor='w')
        ent4 = ttk.Entry(self, textvariable=ents4)
        lab4.grid(row = 9, column = 3)
        ent4.grid(row = 10, column = 6)
        lab5 = tk.Label(self, width=22, text="Phone No : ", anchor='w')
        ent5 = ttk.Entry(self, textvariable=ents5)
        lab5.grid(row = 11, column = 3)
        ent5.grid(row = 12, column = 6)
        lab6 = tk.Label(self, width=22, text="Dish no. selected : ", anchor='w')
        ent6 = ttk.Entry(self, textvariable=ents6)
        lab6.grid(row = 13, column = 3)
        ent6.grid(row = 14, column = 6)
        
        def save():
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123",
            database="restaurant")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT DISH_PRICE FROM dishes WHERE DISH_NO = {}".format(ents6.get()))
            dishcost = mycursor.fetchall()
            query = "INSERT INTO orders (FIRST_NAME, LAST_NAME, ORDER_NO, GENDER, PHONE_NO, DISHNO, COST) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (str(ents1.get()), str(ents2.get()), ents3.get(), str(ents4.get()), ents5.get(), ents6.get(), dishcost[0][0])
            mycursor.execute(query,values)           
            mydb.commit()
            mydb.close()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123",
            database="restaurant")
        mycursor = mydb.cursor()        
        
        mycursor.execute("SELECT DISHNAME FROM dishes")
        dish = mycursor.fetchall()
        mycursor.execute("SELECT DISH_NO FROM dishes")
        dishno = mycursor.fetchall()
        mycursor.execute("SELECT DISH_PRICE FROM dishes")
        cost = mycursor.fetchall()

        
        lb = tk.Listbox(self, height = 15, width = 40)
        
        for i in range(0, len(dish)):
            lb.insert(i+1, "{}  |  {}  |  Price:{}".format(dish[i][0],dishno[i][0],cost[i][0]))    

        lb.pack(side='bottom')        
        button = ttk.Button(self, text = "Save Order",
                            command=lambda: save())
        button.pack(side='bottom')
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side='bottom')

        button2 = ttk.Button(self, text="View Current Orders",
                            command=lambda: controller.show_frame(CurOrderPage))
        button2.pack(side='bottom')


class CurOrderPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Current Orders", font='impact 15')
        label.pack(pady=10,padx=10)
        def refresh():
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="123",
                database="restaurant"
                )

                mycursor = mydb.cursor()

                mycursor.execute("SELECT FIRST_NAME FROM orders")

                fname = mycursor.fetchall()
                mycursor.execute("SELECT LAST_NAME FROM orders")

                lname = mycursor.fetchall()
                mycursor.execute("SELECT ORDER_NO FROM orders")

                orderno = mycursor.fetchall()
                mycursor.execute("SELECT GENDER FROM orders")

                gender = mycursor.fetchall()
                mycursor.execute("SELECT PHONE_NO FROM orders")

                phoneno = mycursor.fetchall()
                mycursor.execute("SELECT DISHNO FROM orders")

                dishes = mycursor.fetchall()
                mycursor.execute("SELECT COST FROM orders")

                cost = mycursor.fetchall()
                lb = tk.Listbox(self, height=10 ,width=150)
                        
                for i in range(0, len(fname)):
                    lb.insert(i+1, "First Name:{}  Last Name:{} Order No:{} Gender:{} Phone no:{} Dish No:{} Cost:{}".format(fname[i][0],lname[i][0],orderno[i][0],gender[i][0],phoneno[i][0],dishes[i][0],cost[i][0]))    
                lb.place(y=50)
        DelLabel=ttk.Label(self, text="Delete Orders", font='impact 15')
        DelLabel.place(x=100, y=300)
        ents=tk.IntVar()
        lab = tk.Label(self, width=22, text="Order No: ", anchor='w')
        ent = ttk.Entry(self, textvariable=ents)
        lab.place(x=100, y=350)
        ent.place(x=200, y=350)
        def delete():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="123",
                database="restaurant"
                )

            mycursor = mydb.cursor()

            mycursor.execute("DELETE FROM orders WHERE ORDER_NO = {}".format(ents.get()))

            mydb.commit()
            mydb.close()
                
        button1 = ttk.Button(self, text="Back to Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=100, y=400)

        button2 = ttk.Button(self, text="Make Order",
                            command=lambda: controller.show_frame(OrderPage))
        button2.place(x=100, y=440)

        button3 = ttk.Button(self, text="Refresh",
                            command=lambda: refresh())
        button3.place(x=100, y=480)
        button4 = ttk.Button(self, text="Delete",
                             command=lambda: delete())
        button4.place(x=350, y=350)
        

class OfferPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.pack_propagate(0)
        label = ttk.Label(self, text="Offers and Discounts", font='impact 15')
        label.pack(pady=10,padx=10)
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="123",
          database="restaurant"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT OFFERNAME FROM offers")
        offer = mycursor.fetchall()
        mycursor.execute("SELECT DISCOUNT FROM offers")
        disc = mycursor.fetchall()
        mycursor.execute("SELECT OFFERDESC FROM offers")
        desc = mycursor.fetchall()

        lb = tk.Listbox(self, height=7, width=40)
        
        for i in range(0, len(offer)):
          lb.insert(i+1, "{} | {}% | {}".format(offer[i][0],disc[i][0],desc[i][0]))    

        lb.pack(side='top')

        button1 = ttk.Button(self, text="Back to Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class DishPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.pack_propagate(0)
        label = ttk.Label(self, text="Add A New Dish", font='impact 15')
        label.pack(pady=10,padx=10)
        ents1=tk.StringVar()
        ents2=tk.IntVar()
        ents3=tk.StringVar()
        lab1 = tk.Label(self, width=22, text="Dish Name : ", anchor='w')
        ent1 = ttk.Entry(self, textvariable=ents1)
        lab1.grid(row = 3, column = 3)
        ent1.grid(row = 4, column = 6)
        lab2 = tk.Label(self, width=22, text="Dish Number : ", anchor='w')
        ent2 = ttk.Entry(self, textvariable=ents2)
        lab2.grid(row = 5, column = 3)
        ent2.grid(row = 6, column = 6)
        lab3 = tk.Label(self, width=22, text="Price : ", anchor='w')
        ent3 = ttk.Entry(self, textvariable=ents3)
        lab3.grid(row = 7, column = 3)
        ent3.grid(row = 8, column = 6)

        def save():
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123",
            database="restaurant")
            mycursor = mydb.cursor()
            query = "INSERT INTO dishes (DISHNAME, DISH_NO, DISH_PRICE) VALUES (%s, %s, %s)"
            values = (str(ents1.get()), ents2.get(), str(ents3.get()))
            mycursor.execute(query,values)           
            mydb.commit()
            mydb.close()
        DelLabel=ttk.Label(self, text="Delete Dishes", font='impact 15')
        DelLabel.place(x=100, y=200)
        ents=tk.IntVar()
        lab = tk.Label(self, width=22, text="Dish No: ", anchor='w')
        ent = ttk.Entry(self, textvariable=ents)
        lab.place(x=100, y=250)
        ent.place(x=200, y=250)
        def delete():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="123",
                database="restaurant"
                )

            mycursor = mydb.cursor()

            mycursor.execute("DELETE FROM dishes WHERE DISH_NO = {}".format(ents.get()))

            mydb.commit()
            mydb.close()    


        button= ttk.Button(self, text='Save Data',
                            command= lambda: save())
        button.pack()
        button1 = ttk.Button(self, text="Back to Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Delete",
                             command=lambda: delete())
        button2.place(x=100, y= 280)
        def refresh():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="123",
                database="restaurant")
            mycursor = mydb.cursor()        
            
            mycursor.execute("SELECT DISHNAME FROM dishes")
            dish = mycursor.fetchall()
            mycursor.execute("SELECT DISH_NO FROM dishes")
            dishno = mycursor.fetchall()
            mycursor.execute("SELECT DISH_PRICE FROM dishes")
            cost = mycursor.fetchall()

            
            lb = tk.Listbox(self, height = 15, width = 40)
            
            for i in range(0, len(dish)):
                lb.insert(i+1, "{}  |  {}  |  Price:{}".format(dish[i][0],dishno[i][0],cost[i][0]))    
            lb.place(x=270, y=340)
        button3 = ttk.Button(self, text="Refresh",
                            command=lambda: refresh())
        button3.pack()
        
class EmployeePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.pack_propagate(0)
        label = ttk.Label(self, text="Employee Directory", font='impact 15')
        label.pack(pady=10,padx=10)
        ents1=tk.StringVar()
        ents2=tk.StringVar()
        ents3=tk.IntVar()
        ents4=tk.StringVar()
        ents5=tk.StringVar()
        ents6=tk.StringVar()
        lab1 = tk.Label(self, width=22, text="First Name : ", anchor='w')
        ent1 = ttk.Entry(self, textvariable=ents1)
        lab1.grid(row = 3, column = 3)
        ent1.grid(row = 4, column = 6)
        lab2 = tk.Label(self, width=22, text="Last Name : ", anchor='w')
        ent2 = ttk.Entry(self, textvariable=ents2)
        lab2.grid(row = 5, column = 3)
        ent2.grid(row = 6, column = 6)
        lab3 = tk.Label(self, width=22, text="Employee ID : ", anchor='w')
        ent3 = ttk.Entry(self, textvariable=ents3)
        lab3.grid(row = 7, column = 3)
        ent3.grid(row = 8, column = 6)
        lab4 = tk.Label(self, width=22, text="Gender : ", anchor='w')
        ent4 = ttk.Entry(self, textvariable=ents4)
        lab4.grid(row = 9, column = 3)
        ent4.grid(row = 10, column = 6)
        lab5 = tk.Label(self, width=22, text="Date Of Birth(DDMMYYYY) : ", anchor='w')
        ent5 = ttk.Entry(self, textvariable=ents5)
        lab5.grid(row = 11, column = 3)
        ent5.grid(row = 12, column = 6)
        lab6 = tk.Label(self, width=22, text="Salary : ", anchor='w')
        ent6 = ttk.Entry(self, textvariable=ents6)
        lab6.grid(row = 13, column = 3)
        ent6.grid(row = 14, column = 6)
        
        def save():
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123",
            database="restaurant")
            mycursor = mydb.cursor()
            query = "INSERT INTO employees (FIRST_NAME, LAST_NAME, EMPLOYEE_ID, GENDER, DOB, SALARY) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (str(ents1.get()), str(ents2.get()), ents3.get(), str(ents4.get()), str(ents5.get()), str(ents6.get()))
            mycursor.execute(query,values)           
            mydb.commit()
            mydb.close()
        DelLabel=ttk.Label(self, text="Delete Employees", font='impact 15')
        DelLabel.place(x=100, y=280)
        ents=tk.IntVar()
        lab = tk.Label(self, width=22, text="Employee ID: ", anchor='w')
        ent = ttk.Entry(self, textvariable=ents)
        lab.place(x=100, y=330)
        ent.place(x=200, y=330)
        def delete():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="123",
                database="restaurant"
                )

            mycursor = mydb.cursor()

            mycursor.execute("DELETE FROM employees WHERE EMPLOYEE_ID = {}".format(ents.get()))

            mydb.commit()
            mydb.close()      
       
        button = ttk.Button(self, text = "Save Record",
                            command=lambda: save())
        button.pack()
        button1 = ttk.Button(self, text="Back to Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Delete",
                             command=lambda: delete())
        button2.place(x=350, y= 330)
        def refresh():
            mydb = mysql.connector.connect(
              host="localhost",
              user="root",
              passwd="123",
              database="restaurant"
            )

            mycursor = mydb.cursor()

            mycursor.execute("SELECT FIRST_NAME FROM employees")
            fname = mycursor.fetchall()
            mycursor.execute("SELECT LAST_NAME FROM employees")
            lname = mycursor.fetchall()
            mycursor.execute("SELECT EMPLOYEE_ID FROM employees")
            empid = mycursor.fetchall()
            mycursor.execute("SELECT GENDER FROM employees")
            gender = mycursor.fetchall()
            mycursor.execute("SELECT DOB FROM employees")
            dob = mycursor.fetchall()
            mycursor.execute("SELECT SALARY FROM employees")
            salary = mycursor.fetchall()

            lb = tk.Listbox(self, height=15, width=100)
            
            for i in range(0, len(fname)):
              lb.insert(i+1, "First Name:{} | Last Name:{} | Employee ID:{} | Gender:{} | Date of Birth:{} | Salary:{}".format(fname[i][0],lname[i][0],empid[i][0],gender[i][0],dob[i][0],salary[i][0]))    

            lb.place(x=110 , y=380)
        button3 = ttk.Button(self, text="Refresh",
                            command=lambda: refresh())
        button3.pack()    

class SalesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.pack_propagate(0)
        label = ttk.Label(self, text="Sales Today", font='impact 15')
        label.pack(pady=10,padx=10)
        def refresh():
            mydb = mysql.connector.connect(
              host="localhost",
              user="root",
              passwd="123",
              database="restaurant"
            )

            mycursor = mydb.cursor()

            mycursor.execute("SELECT COST FROM orders")
            cost = mycursor.fetchall()
            
            lb = tk.Listbox(self, width=25)
            
            for i in range(0, len(cost)):
              lb.insert(i+1, "Sale On Orders:{}".format(cost[i][0]))    

            lb.place(x=325, y=50)
        
        button1 = ttk.Button(self, text="Back to Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side='bottom')
        button2 = ttk.Button(self, text="Refresh",
                            command=lambda: refresh())
        button2.pack(side='bottom')

start = Greeting("Welcome to the Python Restaurant!!!")
app = BackEnd()
app.mainloop()
