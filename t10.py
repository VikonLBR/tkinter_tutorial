import tkinter as tk
from tkinter import messagebox


win = tk.Tk()
win.title('my 9th window')
win.geometry('400x400')

def hit_me():
   # messagebox.showinfo(title='showinfo', message='23333')
   #  messagebox.showerror(title='showerror', message='2333')
   #  messagebox.showwarning(title='showwaring', message='2333')
   #  print(messagebox.askokcancel(title='ask_ok or cancel', message='do you love me?'))
   # print(messagebox.askquestion(title='question', message='do you love me?'))
    print(messagebox.askretrycancel(title='try or cancel', message='do you love me?'))





b = tk.Button(win, text='hit me', command=hit_me)
b.pack()
label = tk.Label(win)


win.mainloop()