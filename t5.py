import tkinter as tk

win = tk.Tk()
win.title('my 3rd tk window')
win.geometry('400x500')


var1 = tk.StringVar()

label = tk.Label(win, text='you have chosen nothing', bg='orange', width=20, height=1)
label.pack()

def print(v):
    label.config(text='you have chosen '+v)


scale = tk.Scale(win, label='try me', from_=1, to_=10, orient=tk.HORIZONTAL, length=500, showvalue=0, tick=1, resolution=0.001, command=print)
#会自动向command的函数里传入当前的值
scale.pack()







win.mainloop()



