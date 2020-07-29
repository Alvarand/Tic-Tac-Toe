import tkinter
from tkinter import messagebox
import config
from config import WIDTH, HEIGHT

root = tkinter.Tk()
root.title('TicTac')
root.geometry(''.join(str(WIDTH + 300)) + 'x' + ''.join(str(HEIGHT)))
root.resizable(width=False, height=False)
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.place(x=0, y=0)


def create_canvas():
    global CIRCLE_WIN, CROSS_WIN
    canvas.delete('all')
    for i in range(1, 4):
        line = canvas.create_line(i * WIDTH // 3, 0, i * WIDTH // 3, HEIGHT)
        line = canvas.create_line(0, i * HEIGHT // 3, WIDTH, i * HEIGHT // 3)
    label_cross = tkinter.Label(text='X: ' + ''.join(str(config.CROSS_WIN)), font='Arial 40')
    label_cross.place(x=700, y=160)
    label_circle = tkinter.Label(text='O: ' + ''.join(str(config.CIRCLE_WIN)), font='Arial 40')
    label_circle.place(x=700, y=360)
    label_flag = tkinter.Label(text='Ходит: ' + config.FLAG, font='Arial 40')
    label_flag.place(x=650, y=70)


create_canvas()
CROSS = tkinter.PhotoImage(file='figure/cross.png')
CIRCLE = tkinter.PhotoImage(file='figure/circle.png')
