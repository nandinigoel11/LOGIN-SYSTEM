from tkinter import*
from tkinter import messagebox

class loginsystem:
    def __init__(self,scr):
        self.scr = scr
        self.scr.title('LOGIN SYSTEM')
        self.scr.geometry('1350x700+0+0')

        self.bg = PhotoImage(file='C:/nandini/py4e/new1.png')
        self.icon = PhotoImage(file = 'C:/nandini/py4e/download.png')

        bglab = Label(self.scr,image = self.bg).pack()

        title = Label(self.scr,text='LOGIN SYSTEM',font=('times new roman',40,'bold'),bg='black',fg='turquoise',bd=10,relief='raised')
        title.place(x=0,y=0,relwidth=1 )

        loginframe = Frame(self.scr)
        loginframe.place(x =480,y=170)

        iconlbl = Label(loginframe,image = self.icon).grid(row=0,columnspan=2)

        userlbl = Label(loginframe,text='Username',compound=LEFT,font=('times new roman',20))
        userlbl.grid(row=1,column=0,pady=5)

        self.textuser = Entry(loginframe,bd=5,relief='raised',font=('',12))
        self.textuser.grid(row=1,column=1,padx=10)

        userpass = Label(loginframe,text='Password',compound=LEFT,font=('times new roman',20))
        userpass.grid(row=2,column=0)

        self.textpass = Entry(loginframe,bd=5,relief='raised',font=('',12))
        self.textpass.grid(row=2,column=1,padx=10)

        btnlogin = Button(loginframe,text='Login',command=self.login,width=15,font=('times new roman',12,'bold'),bg='black',fg='turquoise')
        btnlogin.grid(row=3,columnspan=2,pady=10)




    def login(self):
        if self.textuser.get()=='' or self.textpass.get()=='':
             messagebox.showerror('Error','All fields are required',parent=self.scr)
        elif self.textuser.get()=='Nandini' and self.textpass.get()=='123456':
             messagebox.showinfo('Successful',f'Welcome {self.textuser.get()}',parent=self.scr)
        else:
             messagebox.showerror('Error','Invalid Usename or password',parent=self.scr)



scr = Tk()
obj = loginsystem(scr)
scr.mainloop()
