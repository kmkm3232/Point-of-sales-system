from tkinter import *
import tkinter as tk
import pymysql
from datetime import *
db = pymysql.connect(host= "127.0.0.1",
                     user="root",
                      passwd="",
                      db="allproject")
cursor = db.cursor()
class gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Odering System")
        self.root.geometry('1300x600') # size of GUI
        self.root.resizable(0,0) 
        self.fm= Frame(self.root).pack()
        self.instruction = Label(self.root, text='Please Login / Register To start ordering food!\n', font=(20))
        self.instruction.place(x=1,y=11)
        self.uid=Label(self.root, text='User ID: ', font=(20))
        self.uid.place(x=1,y=61)
        self.pwd =Label(self.root, text='Password: ', font=(20))
        self.pwd.place(x=1,y=121)
        self.menubar = Menu(self.root)
        editmenu = Menu(self.root, tearoff=0)
        User = Menu(self.root, tearoff=0)
        User.add_command(label="User Data",command=self.usdata)
        User.add_command(label="User Order",command=self.usord)
        editmenu.add_command(label="About this Program",command=self.info)
        editmenu.add_command(label="Contact Us",command=self.contact)
        editmenu.add_command(label="How to Use",command=self.how)
        self.menubar.add_cascade(label="User",menu=User)
        self.menubar.add_cascade(label="Help", menu=editmenu)
        self.menubar.add_command(label="Quit",command=self.root.destroy)
        self.root.config(menu=self.menubar)
        self.menubar.entryconfig("User", state="disabled")
        self.idEL = Entry(self.root)
        self.pwordEL = Entry(self.root, show='*')
        self.idEL.place(x=1,y=91)
        self.pwordEL.place(x=1,y=151)
    
        self.loginB = Button(self.root, text='Login', command=self.CheckLogin,font=(20))
        self.loginB.place(x=1,y=181)
        
        self.loginC = Button(self.root, text='Register', command=self.Register,font=(20))
        self.loginC.place(x=71,y=181)
        self.root.mainloop()
    def getID(self):
        return self.idEL.get()

    def getPW(self):
        return self.pwordEL.get()

    def Register(self):
        if cursor.execute("SELECT * FROM `user` WHERE `userID`='"
                           + self.getID() + "'" ):
            self.win = Toplevel()
            self.win.title("")
            self.l = Label(self.win, text="This userID has been taken by others.\n Please Try another one!",font=(15))
            self.l.grid(row=0, column=0)
            self.iun = Button(self.win,text = "Okay!",command =self.win.destroy)
            self.iun.grid(row=1, column=0)
        elif len(self.idEL.get()) ==0:
            self.win = Toplevel()
            self.win.title("")
            self.l = Label(self.win, text="Your did not enter ID!",font=(15))
            self.l.grid(row=0, column=0)
            self.iun = Button(self.win,text = "Okay!",command =self.win.destroy)
            self.iun.grid(row=1, column=0)
        elif len(self.pwordEL.get()) ==0:
            self.win = Toplevel()
            self.win.title("")
            self.l = Label(self.win, text="Your did not enter password!",font=(15))
            self.l.grid(row=0, column=0)
            self.iun = Button(self.win,text = "Okay!",command =self.win.destroy)
            self.iun.grid(row=1, column=0)
        else:
            cursor.execute("INSERT INTO user( \
                    userID, Password) \
                    VALUES ('%s','%s' )" % \
                    (self.getID(), self.getPW()))

            db.commit()

            self.win = Toplevel()
            self.win.title("")
            self.l = Label(self.win, text="Congratduration ! You are now Registered to be our members. \n Now login to start ordering!",font=(15))
            self.l.grid(row=0, column=0)
            self.iun = Button(self.win,text = "Okay!",command =self.win.destroy)
            self.iun.grid(row=1, column=0)
    def CheckLogin(self):
        if cursor.execute("SELECT * FROM `user` WHERE `userID`='"
                           + self.getID() + "'AND `Password`='"
                            + self.getPW() +"'" ):
            self.win = Toplevel()
            self.win.title("")
            self.l = Label(self.win, text="Logged in",font=(15))
            self.l.grid(row=0, column=0)
            self.iun = Button(self.win,text = "Okay!",command =self.win.destroy)
            self.iun.grid(row=1, column=0)
            self.menu()
        else:
            self.win = Toplevel()
            self.win.wm_title("Window")
            self.l = Label(self.win, text="Wrong ID or Password", font=(20))
            self.l.grid(row=0, column=0)
            
    def menu(self):
        self.menubar.entryconfig("User", state="normal")
        self.submit = tk.Button(self.fm,text='Submit',width= 30, height=3,command=self.confirmwindow,font=(20)) # error message box area
        self.submit.pack(side=LEFT, anchor=SW)
        self.instruction.place_forget()
        self.loginB.place_forget()
        self.loginC.place_forget()
        self.idEL.place_forget()
        self.pwordEL.place_forget()
        self.uid.place_forget()
        self.pwd.place_forget()
        self.welcomemess= Label(self.root,text="Welcome !", font=(20))
        self.welcomemess.place(x=610,y=41)
        self.who = Label(self.root,text=self.idEL.get(), font=(20))
        self.welcomemess.place(x=660,y=41)
        self.totaltag=Label(self.root,text="TotalPrice:",font=(20))
        self.totaltag.place(x=610,y=1)
        self.calbutton=Button(self.root,text='Calulate TotalPrice',command=self.Total).place(x=810,y=1)
        sql = "SELECT * FROM `PRODUCT`"
        cursor.execute(sql)
        results = cursor.fetchall()
        m = 1
        n = 1
        self.entries = []
        self.Resetb = []
        self.p1     = []
        self.m1     = []
        self.p10    = []
        self.m10    = []
        for row in results:
            fname = row[2]
            price = row[3]
            self.ProductN = Label(self.root, text=fname)
            self.ProductN.place(x=1, y= m)
            self.Price = Label(self.root, text='$' + str(price))
            self.Price.place(x= 130,y= m)
            self.Quantity = Label(self.root, text='Quantity :')
            self.Quantity.place(x= 230,y= m)
            m += 30
        for i in range(0,13):
            self.en = Label(self.root,text=0)
            self.en.place(x=290,y=n)
            self.entries.append(self.en)
            self.ResetButton = Button(self.root, text='Reset',command = lambda i=i: self.reset(i))
            self.ResetButton.place(x=380,y=n)
            self.Resetb.append(self.ResetButton)
            self.plus1 = Button(self.root, text='+1',command = lambda i=i: self.plus(i))
            self.plus1.place(x=430,y=n)
            self.p1.append(self.plus1)
            self.minus1 = Button(self.root, text='-1',command = lambda i=i: self.Minus(i))
            self.minus1.place(x=460,y=n)
            self.m1.append(self.minus1)
            self.plus10 = Button(self.root, text='+10',command = lambda i=i: self.plus10f(i))
            self.plus10.place(x=490,y=n)
            self.p10.append(self.plus10)
            self.minus10 = Button(self.root, text='-10',command = lambda i=i: self.Minus10f(i))
            self.minus10.place(x=530,y=n)
            self.m10.append(self.minus10)
            n += 30
    def reset(self,num):
        self.entries[num].config(text=0)
    def Minus(self,num):
        if self.entries[num].cget("text") >0:
            j = self.entries[num].cget("text")
            j -= 1
            self.entries[num].config(text= j)
    def plus(self,num):
        j = self.entries[num].cget("text")
        j += 1
        self.entries[num].config(text= j)
    def Minus10f(self,num):
        if self.entries[num].cget("text") >9:
            j = self.entries[num].cget("text")
            j -= 10
            self.entries[num].config(text= j)
        else:
            self.entries[num].config(text= 0)
    def plus10f(self,num):
        j = self.entries[num].cget("text")
        j += 10
        self.entries[num].config(text= j)
    def usdata(self):
        usd= tk.Tk()
        usd.wm_title("Your Data")
        usd.geometry('500x100')
        usd.attributes('-topmost', 'true')
        sql = "SELECT * FROM `USER` WHERE `userID`='" + self.getID() + "'"
        cursor.execute(sql)
        usda = cursor.fetchall()
        print (usda)
        for i in usda:
            self.usid = Label(usd, text='UserID : '+ str(i[0]),font=(15))
            self.usid.place(x=0,y=0)
            self.userPassword = Label(usd, text='UserPassWord : ******* (For security purpose, PassWord Can not be shown)',font=(15))
            self.userPassword.place(x= 0,y= 30)

    def usord(self):
        ord=tk.Tk()
        ord.wm_title("Your Order")
        ord.geometry('800x600')
        sql="SELECT * FROM invoice1 WHERE `userID`='" + self.getID() + "'"
        cursor.execute(sql)
        results = cursor.fetchall()
        n = 0
        for xa in results:
            self.usid = Label(ord, text='UserID : '+ str(xa[0]),font=(15))
            self.usid.place(x=0,y=n)
            self.orderID = Label (ord,text='OrderID : '+ str(xa[1]),font=(15))
            self.orderID.place(x=150,y=n)
            self.date = Label(ord,text='Date : ' +str(xa[2]),font=(15))
            self.date.place(x=300,y=n)
            self.tprice = Label(ord,text='Total price : '+str(xa[4]),font=(15))
            self.tprice.place(x=500,y=n)
            n +=50
    def Total(self):
        sql = "SELECT * FROM `PRODUCT`"
        cursor.execute(sql)
        results = cursor.fetchall()
        totalPrice = (self.entries[0].cget("text")*results[0][3] + self.entries[1].cget("text")*results[1][3] + self.entries[2].cget("text")*results[2][3]
        + self.entries[3].cget("text")*results[3][3] + self.entries[4].cget("text")*results[4][3] + self.entries[5].cget("text")*results[5][3]
        + self.entries[6].cget("text")*results[6][3] + self.entries[7].cget("text")*results[7][3] + self.entries[8].cget("text")*results[8][3]+ self.entries[9].cget("text")*results[9][3] + self.entries[10].cget("text")*results[10][3] + self.entries[11].cget("text")*results[11][3]
        + self.entries[12].cget("text")*results[12][3])
        self.totaltag.config(text= 'TotalPrice  :  $%.10s'%totalPrice)
    def confirmwindow(self):
        self.comfi= tk.Tk()
        self.comfi.wm_title("confirm Order ?")
        self.comfi.geometry('300x100')
        self.yes = Button(self.comfi,text='Yes!', command=self.confirm)
        self.yes.pack()
        self.no = Button(self.comfi,text='No!', command=self.comfi.destroy)
        self.no.pack()
    def confirm(self):
        self.yes.pack_forget()
        self.no.pack_forget()
        self.l = Label(self.comfi, text="Thank you for coming \n Your order has been confirmed", font=(20))
        self.l.grid(row=0, column=0)
        sql="SELECT orderID FROM order1 ORDER BY orderID"
        cursor.execute(sql)
        results = cursor.fetchall()
        for i in results:
            self.youroderIDis = Label(self.comfi, text='Your orderID is : ' +str(i[0]))
            self.youroderIDis.grid(row=1, column=0)
        canc=tk.Button(self.comfi, text='cancel',command=self.cancel)        
        canc.place(x=150,y=60)
        self.iun = Button(self.comfi,text = "Okay!",command=self.comfi.destroy)
        self.iun.place(x=90,y=60)
        sql1 = "SELECT * FROM `PRODUCT`"
        cursor.execute(sql1)
        results = cursor.fetchall()
        totalPrice = (self.entries[0].cget("text")*results[0][3] + self.entries[1].cget("text")*results[1][3] + self.entries[2].cget("text")*results[2][3]
        + self.entries[3].cget("text")*results[3][3] + self.entries[4].cget("text")*results[4][3] + self.entries[5].cget("text")*results[5][3]
        + self.entries[6].cget("text")*results[6][3] + self.entries[7].cget("text")*results[7][3] + self.entries[8].cget("text")*results[8][3]+ self.entries[9].cget("text")*results[9][3] + self.entries[10].cget("text")*results[10][3] + self.entries[11].cget("text")*results[11][3]
        + self.entries[12].cget("text")*results[12][3])
        self.totaltag.config(text='TotalPrice  :$%.10s' % totalPrice)

        sql2 = "INSERT INTO invoice1(userID, Date, Time, totalPrice) \
                       VALUES('%s','%s','%s','%s')" % \
               (self.getID(), date.today(), datetime.now().strftime("%H:%M:%S"), totalPrice)
        cursor.execute(sql2)
        for i in range(0,13):
            if self.entries[i].cget("text") > 0:
                cursor.execute("INSERT INTO order1(orderID) SELECT orderID FROM invoice1 ORDER BY orderID DESC LIMIT 1;")
                cursor.execute("UPDATE order1 SET `productID`='" + str(i+1) + "' , `quantity` ='" + str(
                    self.entries[i].cget("text")) + "'ORDER BY orderID DESC LIMIT 1")
        self.root.destroy()
        db.commit()
    def contact(self):
        cont = tk.Tk()
        cont.wm_title("Contact Us")
        cont.geometry('600x100')
        self.email = Label(cont,text="Email : allprojectezgroup@gamil.com", font = (15))
        self.email.pack()
        self.phone = Label(cont,text =" Phone Number : +852 9999 8888 (Avaliable at 9:00 am To 5:00 pm)", font = (15))
        self.phone.pack()
        self.iun = Button(cont,text = "Okay!",command =cont.destroy)
        self.iun.place(x=270,y=71)
    def info(self):
        infoo = tk.Tk()
        infoo.wm_title("About This Program")
        infoo.geometry('400x100')
        self.in1a = Label(infoo,text="Programmed by EZ Application Company Limited.", font = (20))
        self.in1a.place(x=1,y=1)
        self.in1b = Label(infoo,text="Enhanced by Group5.", font = (20))
        self.in1b.place(x=1,y=31)
        self.iun = Button(infoo,text = "Okay!",command =infoo.destroy)
        self.iun.place(x=150,y=61)
    def how(self):
        how = tk.Tk()
        how.wm_title("How to use")
        how.geometry('600x200')
        self.hw1a = Label(how,text="Step 1: Chose products you want.", font = (15))
        self.hw1a.place(x=51,y=1)
        self.hw1b = Label(how,text="Step 2: Enter how many you need by pressing +1/-1 +10/-10.", font = (15))
        self.hw1b.place(x=51,y=31)
        self.hw1 = Label(how,text="Step 3: Press sumbit to order.", font = (15))
        self.hw1.place(x=51,y=61)
        self.hw2 = Label(how,text="Step 4: Keep your receipt and want for staff to call your order number.", font = (15))
        self.hw2.place(x=51,y=91)
        self.hw3 = Label(how,text="Step 5: Enjoy your food!", font = (15))
        self.hw3.place(x=51,y=121)
        self.iun = Button(how,text = "Okay!",command =how.destroy)
        self.iun.place(x=250,y=151)
    def cancel(self):
        sql="DELETE FROM order1 WHERE orderID IN(SELECT orderID FROM(SELECT orderID FROM order1 ORDER BY orderID LIMIT 1)a)"
        cursor.execute(sql)
        canc = tk.Tk()
        canc.wm_title("Cancel")
        canc.geometry('200x50')
        canc.attributes('-topmost', 'true')
        
        canc1 = Label(canc,text="Order Cancelled", font = (20))
        canc1.place(x=50,y=0)
        self.comfi.destroy()
        db.commit()
    
def main():
    root = tk.Tk()
    gui(root)
    root.mainloop()
if __name__ == '__main__':
    main()
