import tkinter
from tkinter import messagebox
from config import *

root = tkinter.Tk()
root.title('TicTac')
root.maxsize(WIDTH, HEIGHT)
root.minsize(WIDTH, HEIGHT)
canvas = tkinter.Canvas(root, width=WIDTH + 300, height=HEIGHT)
canvas.grid()

line_1 = canvas.create_line(WIDTH // 3, 0, WIDTH // 3, HEIGHT)
line_2 = canvas.create_line(2 * WIDTH // 3, 0, 2 * WIDTH // 3, HEIGHT)
line_3 = canvas.create_line(0, HEIGHT // 3, WIDTH, HEIGHT // 3)
line_4 = canvas.create_line(0, 2 * HEIGHT // 3, WIDTH, 2 * HEIGHT // 3)

CROSS = tkinter.PhotoImage(file='figure/cross.png')
CIRCLE = tkinter.PhotoImage(file='figure/circle.png')
