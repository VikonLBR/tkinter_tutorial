import tkinter as tk

win = tk.Tk()
win.title('my 3rd tk window')
win.geometry('400x500')


var1 = tk.StringVar()

label = tk.Label(win, textvariable=var1, bg='orange', width=10, height=1)
label.pack()

var2 = tk.StringVar()
var2.set((1, 2, 3, 4, 5))
listbox = tk.Listbox(win, listvariable=var2)
list = [6, 7, 8, 9]
for item in list:
    listbox.insert('end', item)

listbox.insert(2, 'just insert one item each time')

listbox.pack()



def print():
    var = listbox.get(listbox.curselection())
    var1.set(var)
button_1 = tk.Button(win, text='print selection', width=15, height=2, command=print)
button_1.pack()






win.mainloop()



