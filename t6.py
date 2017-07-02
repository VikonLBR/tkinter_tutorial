import tkinter as tk

win = tk.Tk()
win.title('my 6th tk window')
win.geometry('400x500')




label = tk.Label(win, text='you have chosen nothing', bg='orange', width=20, height=1)
label.pack()

def print():
    if ((var1.get()==1)&(var2.get()==1)):
        label.config(text='I love both')
    elif ((var1.get()==1)&(var2.get()==0)):
        label.config(text='I love Python')
    elif ((var1.get()==0)&(var2.get()==1)):
        label.config(text='I love C++')
    else:
        label.config(text='I don\'t love either')


var1 = tk.IntVar()
var2 = tk.IntVar()

cb1 = tk.Checkbutton(win, text='Python', variable=var1, onvalue=1, offvalue=0, command=print)
cb2 = tk.Checkbutton(win, text='C++', variable=var2, onvalue=1, offvalue=0, command=print)

cb1.pack()
cb2.pack()





win.mainloop()



