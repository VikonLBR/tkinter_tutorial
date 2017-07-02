import re
import tkinter as tk
from tkinter import messagebox
import numpy as np
import PIL.Image as Image

# image = Image.open('lp.gif').convert('RGB')
# print(image.getpixel((0, 0)))


# image = Image.open('lp.gif')
# p = image.load()
# size = image.size
# print(p)
# pic_matrix = np.zeros(size)
# width = size[0]
# height = size[1]
# for x in range(width):
#     for y in range(height):
#         pic_matrix[x, y] = p[x, y]
#
# np.save('lp_pic_matrix', pic_matrix)


# image = Image.open('lp.gif').convert('L')
# width, height = image.size
# data = image.getdata()
# print(np.matrix(data))
# data = np.matrix(data)
# new_data = np.reshape(data, (height, width))#height first
# Image.fromarray(new_data).show()


image = Image.open('lp.gif').convert('RGB')
data = image.load()
R, G, B = [],[],[]
width, height = image.size
for i in range(height):
    for j in range(width):
        r, g, b=data[j, i]
        R.append(r)
        G.append(g)
        B.append(b)

R = np.array(R).reshape(height,width)
G = np.array(G).reshape(height,width)
B = np.array(B).reshape(height,width)

# im = Image.new('RGB', (width, height))
# for i in range(0,height):
#     for j in range(0,width):
#         im.putpixel((j, i),(int(R[i, j]), int(G[i, j]), int(B[i, j])))
# im.show()

np.save('lp_R', R)
np.save('lp_G', G)
np.save('lp_B', B)



# image.show()