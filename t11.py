import tkinter as tk

win = tk.Tk()
win.title('my 11th window')
win.geometry('400x400')

#pack
# tk.Label(win, text='top', bg='orange', width=10, height=10).pack(side='top')
#
# tk.Label(win, text='left', bg='orange', width=10, height=10).pack(side='left')
#
# tk.Label(win, text='right', bg='orange', width=10, height=10).pack(side='right')
#
# tk.Label(win, text='bottom', bg='orange', width=10, height=10).pack(side='bottom')

#grid
# for i in range(3):
#     for j in range(5):
#         tk.Label(win, text='test', bg='orange').grid(row=i, column=j, padx=10, pady=10, ipadx=3, ipady=3)#加i为内部扩展


#place精准放置
tk.Label(win, text='right', bg='orange', width=10, height=10).place(x=10, y=10, anchor='ne')





win.mainloop()