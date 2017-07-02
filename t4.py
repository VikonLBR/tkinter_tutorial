import tkinter as tk

win = tk.Tk()
win.title('my 3rd tk window')
win.geometry('400x500')


var1 = tk.StringVar()

label = tk.Label(win, text='empty', bg='orange', width=20, height=1)
label.pack()

def print():
    label.config(text='you have chosen '+var1.get())



t1 = tk.Radiobutton(win, text='Option A', variable=var1, value='A', command=print)
t2 = tk.Radiobutton(win, text='Option A', variable=var1, value='B', command=print)
t3 = tk.Radiobutton(win, text='Option A', variable=var1, value='C', command=print)

t1.pack()
t2.pack()
t3.pack()





win.mainloop()



