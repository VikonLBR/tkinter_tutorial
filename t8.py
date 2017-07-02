import tkinter as tk

win = tk.Tk()
win.title('my 8th tk window')
win.geometry('400x400')

label = tk.Label(win, text='menubar', bg='red')
label.pack()

count = 0
def donew():
    global count
    count += 1
    label.config(text='number is '+ str(count))


menubar = tk.Menu(win)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='file', menu=filemenu)
filemenu.add_command(label='new', command=donew)
filemenu.add_command(label='open', command=donew)
filemenu.add_separator()


submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='submenu',menu=submenu)
submenu.add_command(label='sub1', command=donew)


win.config(menu=menubar)




win.mainloop()