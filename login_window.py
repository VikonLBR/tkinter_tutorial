import tkinter as tk
import re
from tkinter import messagebox


win = tk.Tk()
win.title('Login')
win.geometry('1500x1000')

canvas = tk.Canvas(win, width=580, height=870)
image_file = tk.PhotoImage(file='lp.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.place(x=0, y=0, anchor='nw')

db = {'vikon':'ldsldh1991', 'lbr':'ldsldh1991'}


def identify():
    global db
    uname = entry1.get()
    pwd = entry2.get()

    if (uname in db.keys()) and (db[uname] == pwd):
        messagebox.showinfo(title='Welcome aboard', message='welcome '+uname)
    else:
        messagebox.showwarning(title='Warning', message='wrong user name or password, check again plz')



def create():
    global db
    signp = tk.Tk()
    signp.title('regist page')
    signp.geometry('500x300')

    uname = tk.Entry(signp, width=20)
    pwd1 = tk.Entry(signp, width=20, show='*')
    pwd2 = tk.Entry(signp, width=20, show='*')

    uname.place(x=30, y=30, anchor='nw')
    pwd1.place(x=30, y=70, anchor='nw')
    pwd2.place(x=30, y=110, anchor='nw')


    def sign():
        global db
        unames = uname.get()
        if(re.match('.*\W+.*', str(unames)) is None)&(unames not in db.keys()):
            if pwd1.get() is not '':
                print('start insert')
                db[str(unames)] = str(pwd1.get())
                print(db)
                messagebox.showinfo(title='Congratrulations', message='regist successfully')
                signp.destroy()
            else:
                messagebox.showwarning(title='Warning', message='password should not be None')
        else:
            messagebox.showwarning(title='Warning', message='invalid user name or user name already exist')



    b1 = tk.Button(signp, text='sign up', command=sign)
    b2 = tk.Button(signp, text='quit', command=signp.destroy)
    b1.place(x=190, y=50, anchor='nw')
    b2.place(x=190, y=100, anchor='nw')
    signp.mainloop()


frm = tk.Frame(win, width=920, height=1000, bg='orange')

entry1 = tk.Entry(frm, show=None, width=30)
entry2 = tk.Entry(frm, show='*', width=30)

entry1.place(x=200, y=500, anchor='nw')
entry2.place(x=200, y=533, anchor='nw')


fr1 = tk.Frame(frm, width=920, height=40, bg='orange')

b1 = tk.Button(fr1, text='sign in', width=20, height=1, bg='lightblue', command=identify)

b2 = tk.Button(fr1, text='sign up', width=20, height=1, bg='lightblue', command=create)



b1.place(x=120, y=0, anchor='nw')
b2.place(x=350, y=0, anchor='nw')


fr1.place(x=0, y=580, anchor='nw')

frm.place(x=580, y=00, anchor='nw')




win.mainloop()