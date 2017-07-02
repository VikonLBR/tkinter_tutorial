import tkinter as tk

win = tk.Tk()
win.title('my 1s tk window')
win.geometry('400x500')


var = tk.StringVar()
label = tk.Label(win, textvariable=var, bg='orange', font=('Arial', 12), width=12, height=2)
label.pack()


flag = False

def hit_me():
    global flag
    if not flag:
        flag = True
        var.set('I\'m here')
    else:
        flag = False
        var.set('')


button = tk.Button(win, text='hit me', width=5, height=5, command=hit_me)
button.pack()

win.mainloop()



