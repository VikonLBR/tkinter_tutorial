import tkinter as tk

win = tk.Tk()
win.title('my 9th window')
win.geometry('400x400')

#Frame

tk.Label(win, text='on the window').pack()


frm = tk.Frame(win)
frm.pack()

fr1 = tk.Frame(frm)

fr1.pack(side='left')

fr2 = tk.Frame(frm)

fr2.pack(side='right')
tk.Label(fr2, text='fr2 label1').pack()
tk.Label(fr1, text='fr1 label1').pack()
tk.Label(fr1, text='fr1 label2').pack()
win.mainloop()