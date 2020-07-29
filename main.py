from menu import *
import config


def b1(event):
    y, x = event.y // 200, event.x // 200
    if x <= 2:
        global FLAG, MAP
        if FLAG == 'x' and MAP[y][x] == 0:
            MAP[y][x] = FLAG
            canvas.create_image(x * 200 + 100, y * 200 + 100, image=CROSS)
            FLAG = 'o'
            check()
        elif FLAG == 'o' and MAP[y][x] == 0:
            MAP[y][x] = FLAG
            canvas.create_image(x * 200 + 100, y * 200 + 100, image=CIRCLE)
            FLAG = 'x'
            check()


def check():
    global MAP, CIRCLE_WIN, CROSS_WIN
    MAP_ZERO = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    if MAP[0][0] == MAP[1][1] == MAP[2][2] and MAP[0][0] != 0:
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
