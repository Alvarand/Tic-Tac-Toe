from menu import *
import config
from config import MAP


def b1(event):
    y, x = event.y // 200, event.x // 200
    if x <= 2:
        global MAP
        if config.FLAG == 'x' and MAP[y][x] == 0:
            MAP[y][x] = config.FLAG
            canvas.create_image(x * 200 + 100, y * 200 + 100, image=CROSS)
            config.FLAG = 'o'
            check()
            label_flag = tkinter.Label(text='Ходит: ' + config.FLAG, font='Arial 40')
            label_flag.place(x=650, y=70)
        elif config.FLAG == 'o' and MAP[y][x] == 0:
            MAP[y][x] = config.FLAG
            canvas.create_image(x * 200 + 100, y * 200 + 100, image=CIRCLE)
            config.FLAG = 'x'
            check()
            label_flag = tkinter.Label(text='Ходит: ' + config.FLAG, font='Arial 40')
            label_flag.place(x=650, y=70)


def check():
    global MAP, CIRCLE_WIN, CROSS_WIN
    MAP_ZERO = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    if MAP[0][0] == MAP[1][1] == MAP[2][2] and MAP[0][0] != 0:
        line = canvas.create_line(0, 0, WIDTH, HEIGHT, width=10, fill='red')
        if MAP[2][2] == 'x':
            tkinter.messagebox.showinfo("Победа", 'Первый игрок победил')
            MAP = MAP_ZERO
            config.CROSS_WIN += 1
            create_canvas()
        else:
            tkinter.messagebox.showinfo("Победа", 'Второй игрок победил')
            MAP = MAP_ZERO
            config.CIRCLE_WIN += 1
            create_canvas()
    elif MAP[0][2] == MAP[1][1] == MAP[2][0] and MAP[1][1] != 0:
        line = canvas.create_line(WIDTH, 0, 0, HEIGHT, width=10, fill='red')
        if MAP[2][0] == 'x':
            tkinter.messagebox.showinfo("Победа", 'Первый игрок победил')
            MAP = MAP_ZERO
            config.CROSS_WIN += 1
            create_canvas()
        else:
            tkinter.messagebox.showinfo("Победа", 'Второй игрок победил')
            MAP = MAP_ZERO
            config.CIRCLE_WIN += 1
            create_canvas()
    elif MAP[0][0] == MAP[0][1] == MAP[0][2] and MAP[0][0] != 0:
        line = canvas.create_line(0, HEIGHT // 6, WIDTH, HEIGHT // 6, width=10, fill='red')
        if MAP[0][0] == 'x':
            tkinter.messagebox.showinfo("Победа", 'Первый игрок победил')
            MAP = MAP_ZERO
            config.CROSS_WIN += 1
            create_canvas()
        else:
            tkinter.messagebox.showinfo("Победа", 'Второй игрок победил')
            MAP = MAP_ZERO
            config.CIRCLE_WIN += 1
            create_canvas()
    elif MAP[1][0] == MAP[1][1] == MAP[1][2] and MAP[1][0] != 0:
        line = canvas.create_line(0, 3 * HEIGHT // 6, WIDTH, 3 * HEIGHT // 6, width=10, fill='red')
        if MAP[1][2] == 'x':
            tkinter.messagebox.showinfo("Победа", 'Первый игрок победил')
            MAP = MAP_ZERO
            config.CROSS_WIN += 1
            create_canvas()
        else:
            tkinter.messagebox.showinfo("Победа", 'Второй игрок победил')
            MAP = MAP_ZERO
            config.CIRCLE_WIN += 1
            create_canvas()
    elif MAP[2][0] == MAP[2][1] == MAP[2][2] and MAP[2][0] != 0:
        line = canvas.create_line(0, 5 * HEIGHT // 6, WIDTH, 5 * HEIGHT // 6, width=10, fill='red')
        if MAP[2][1] == 'x':
            tkinter.messagebox.showinfo("Победа", 'Первый игрок победил')
            MAP = MAP_ZERO
            config.CROSS_WIN += 1
            create_canvas()
        else:
            tkinter.messagebox.showinfo("Победа", 'Второй игрок победил')
            MAP = MAP_ZERO
            config.CIRCLE_WIN += 1
            create_canvas()
    elif MAP[0][0] == MAP[1][0] == MAP[2][0] and MAP[0][0] != 0:
        line = canvas.create_line(WIDTH // 6, 0, WIDTH // 6, HEIGHT, width=10, fill='red')
        if MAP[1][0] == 'x':
            tkinter.messagebox.showinfo("Победа", 'Первый игрок победил')
            MAP = MAP_ZERO
            config.CROSS_WIN += 1
            create_canvas()
        else:
            tkinter.messagebox.showinfo("Победа", 'Второй игрок победил')
            MAP = MAP_ZERO
            config.CIRCLE_WIN += 1
            create_canvas()
    elif MAP[0][1] == MAP[1][1] == MAP[2][1] and MAP[0][1] != 0:
        line = canvas.create_line(3 * WIDTH // 6, 0, 3 * WIDTH // 6, HEIGHT, width=10, fill='red')
        if MAP[1][1] == 'x':
            tkinter.messagebox.showinfo("Победа", 'Первый игрок победил')
            MAP = MAP_ZERO
            config.CROSS_WIN += 1
            create_canvas()
        else:
            tkinter.messagebox.showinfo("Победа", 'Второй игрок победил')
            MAP = MAP_ZERO
            config.CIRCLE_WIN += 1
            create_canvas()
    elif MAP[0][2] == MAP[1][2] == MAP[2][2] and MAP[0][2] != 0:
        line = canvas.create_line(5 * WIDTH // 6, 0, 5 * WIDTH // 6, HEIGHT, width=10, fill='red')
        if MAP[0][2] == 'x':
            tkinter.messagebox.showinfo("Победа", 'Первый игрок победил')
            MAP = MAP_ZERO
            config.CROSS_WIN += 1
            create_canvas()
        else:
            tkinter.messagebox.showinfo("Победа", 'Второй игрок победил')
            MAP = MAP_ZERO
            config.CIRCLE_WIN += 1
            create_canvas()
    elif not (0 in MAP[0] or 0 in MAP[1] or 0 in MAP[2]):
        tkinter.messagebox.showinfo("Ничья", 'Ничья')
        MAP = MAP_ZERO
        create_canvas()


def escape(event):
    root.quit()


root.bind('<Button-1>', b1)
root.bind('<Escape>', escape)

if __name__ == '__main__':
    root.mainloop()
