import tkinter as tk

win = tk.Tk()
win.title('my 2rd tk window')
win.geometry('400x500')

entry = tk.Entry(win, show='*', bg='orange')
entry.pack()
text = tk.Text(win, height=2)

def insert():
    var = entry.get()
    text.insert('insert', var)

def insert_end():
    var = entry.get()
    text.insert('1.1', var)

button_1 = tk.Button(win, text='insert here', width=5, height=5, command=insert)
button_2 = tk.Button(win, text='insert to the end', width=15, height=5, command=insert_end)
button_1.pack()
button_2.pack()

text.pack()



win.mainloop()



