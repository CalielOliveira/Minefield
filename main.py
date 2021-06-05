import tkinter
import random
from tkinter import messagebox


def easy_mode():
    global n, m, k
    n, m, k = 8, 8, 10
    restart_game()


def medium_mode():
    global n, m, k
    n, m, k = 16, 16, 40
    restart_game()


def hard_mode():
    global n, m, k
    n, m, k = 24, 24, 90
    restart_game()


def restart_game():
    global matrix_of_squares, list_of_squares
    for row in list_of_squares:
        for square in row:
            square.destroy()
    matrix_of_squares = create_camp(n, m, k)
    create_buttons()
    for line in matrix_of_squares:
        print(line)


def create_buttons():
    global list_of_squares
    list_of_squares = [
        [tkinter.Button(squares_buttons, command=lambda x=x, y=y: [reveal(x, y)], width=4, height=2) for y in range(n)]
        for x in range(m)]
    for x in range(n):
        for y in range(m):
            list_of_squares[x][y].bind('<Button-3>', put_mark)
            list_of_squares[x][y].grid(row=x, column=y)


def create_camp(n, m, k):
    matrix = [[0 for i in range(m)] for j in range(n)]
    bombs = 0
    while bombs < k:
        place = [random.randint(1, n - 1), random.randint(1, m - 1)]
        if matrix[place[0]][place[1]] != 1:
            matrix[place[0]][place[1]] = 1
            bombs += 1
    return matrix


def check_disponible_places(x, y):
    i1 = i3 = -1
    i2 = i4 = 2
    if x == 0:
        i1 = 0
    if x == n - 1:
        i2 = 1
    if y == 0:
        i3 = 0
    if y == m - 1:
        i4 = 1
    return [i1, i2, i3, i4]


def count_bombs_around(n, m, disponible_places):
    counter = 0
    for i in range(disponible_places[0], disponible_places[1]):
        for j in range(disponible_places[2], disponible_places[3]):
            if matrix_of_squares[n + i][m + j] == 1:
                counter += 1
    return counter


def reveal(x, y):
    global list_of_squares
    if matrix_of_squares[x][y] == 1:
        tkinter.messagebox.showinfo("Alert!", "Você clickou em uma bomba e ela explodiu!")
        restart_game()
    else:
        disponible_places = check_disponible_places(x, y)
        bombs_around = count_bombs_around(x, y, disponible_places)
        if bombs_around == 0:
            list_of_squares[x][y].destroy()
            list_of_squares[x][y] = tkinter.Label(squares_buttons, text=" ", width=4, height=2)
            for a in range(disponible_places[0], disponible_places[1]):
                for b in range(disponible_places[2], disponible_places[3]):
                    i = x + a
                    j = y + b
                    if type(list_of_squares[i][j]) == tkinter.Button and matrix_of_squares[i][j] != 1:
                        reveal(i, j)
        else:
            list_of_squares[x][y].destroy()
            list_of_squares[x][y] = tkinter.Label(squares_buttons, text=bombs_around, width=4, height=2)
        list_of_squares[x][y].grid(row=x, column=y)


def put_mark(event):
    if event.widget['text'] == 'X':
        event.widget['text'] = ' '
    else:
        event.widget['text'] = 'X'


n = 8
m = 8
k = 10
matrix_of_squares = create_camp(n, m, k)
for line in matrix_of_squares:
    print(line)

window = tkinter.Tk()

main_buttons = tkinter.Frame(window)
squares_buttons = tkinter.Frame(window)

easy_button = tkinter.Button(main_buttons, text='easy', command=easy_mode)
medium_button = tkinter.Button(main_buttons, text='medium', command=medium_mode)
hard_button = tkinter.Button(main_buttons, text='hard', command=hard_mode)
restart_button = tkinter.Button(main_buttons, text='restart', command=restart_game)

main_buttons.grid(row=0, column=0)
squares_buttons.grid(row=1, column=0)

create_buttons()

easy_button.grid(row=0, column=0)
medium_button.grid(row=0, column=1)
hard_button.grid(row=0, column=2)
restart_button.grid(row=0, column=3)

window.mainloop()