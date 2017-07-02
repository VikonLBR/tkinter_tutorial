import tkinter as tk

win = tk.Tk()
win.title('my 7th tk window')
win.geometry('400x400')

canvas = tk.Canvas(win, bg='darkblue', height=200, width=200)
image_file = tk.PhotoImage(file='d:\\sweet.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
x0, y0, x1, y1 = 150, 150, 200, 200
line = canvas.create_line(x0, y0, x1, y1)
round = canvas.create_oval(x0, y0, x1, y1, fill='red')
square = canvas.create_rectangle(x0, y0, x1, y1)
arc = canvas.create_arc(x0-10, y0-10, x1-10, y1-10, start=0, extent=180)

canvas.pack()


def move():
    canvas.move(arc, -1, -1)

b = tk.Button(win, text='move', command=move)
b.pack()


win.mainloop()