from turtle import *
from tkinter import *
from tkinter import filedialog
from math import *
from tkinter.ttk import Combobox


def move(x, y):
    penup()
    goto(x, y)
    pendown()


def Check_num(x, y):
    global click_num, mas
    i = 0
    num = 0
    while i < mas[2] - 1 and num == 0:
        if (abs(x - mas[0][i * 2]) < size * 2) and (abs(y + size - mas[0][i * 2 + 1]) < size * 2):
            num = i + 1
        i += 1
    return num


def dot(mas, size, color, x, y, N):
    move(x, y)
    fillcolor(color)
    begin_fill()
    circle(size)
    move(x, y + size / 2)
    pencolor('black')
    write(N)
    pencolor(color)
    end_fill()


def DrawGraph(mas, color, size):
    for j in range(len(mas[1])):
        for k in range(len(mas[1][j])):
            if mas[1][j][k] == 1:
                draw_edge(mas, j+1, k+1)
    for i in range((len(mas[0]))//2):
        dot(mas, size, color, mas[0][i * 2], mas[0][i * 2 + 1] - size, i + 1)


def delete_dot(mas, x, y):
    num = Check_num(x, y)
    for i in range(mas[2] - 1):
        if mas[1][num - 1][i - 1] == 1:
            delete_edge(mas, num, i)
    pencolor('white')
    move(mas[0][num * 2 - 2] - size, mas[0][num * 2 - 1] + size)
    fillcolor('white')
    begin_fill()
    for i in range(4):
        forward(size * 2)
        right(90)
    end_fill()
    mas[0].pop(num * 2 - 1)
    mas[0].pop(num * 2 - 2)
    mas[1].pop(num - 1)
    for i in range(mas[2] - 2):
        mas[1][i].pop(num - 1)
    mas[2] -= 1
    pencolor(color)
    for i in range(num, mas[2]):
        dot(mas, size, color, mas[0][i * 2 - 2], mas[0][i * 2 - 1] - size, i)


def draw_edge(mas, n1, n2):
    move(mas[0][n1 * 2 - 2], mas[0][n1 * 2 - 1])
    goto(mas[0][n2 * 2 - 2], mas[0][n2 * 2 - 1])
    mas[1][n1 - 1][n2 - 1] = 1
    mas[1][n2 - 1][n1 - 1] = 1


def delete_edge(mas, n1, n2):
    move(mas[0][n1 * 2 - 2], mas[0][n1 * 2 - 1])
    pencolor('white')
    goto(mas[0][n2 * 2 - 2], mas[0][n2 * 2 - 1])
    mas[1][n1 - 1][n2 - 1] = 0
    mas[1][n2 - 1][n1 - 1] = 0
    pencolor('orange')
    dot(mas, size, color, mas[0][n1 * 2 - 2], mas[0][n1 * 2 - 1] - size, n1)
    dot(mas, size, color, mas[0][n2 * 2 - 2], mas[0][n2 * 2 - 1] - size, n2)


def reset(mas, color, size):
    mas = [mas[0], mas[1], N]
    move(-500, -500)
    fillcolor('white')
    begin_fill()
    for i in range(4):
        forward(1000)
        left(90)
    end_fill()
    DrawGraph(mas, color, size)


def exit_file():
    Screen().bye()
    tk.destroy()


def save_file(mas):
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    text = str(mas)
    with open(filename, "w") as file:
        file.write(text)


def open_file():
    global color, size, mas
    move(-500, -500)
    fillcolor('white')
    begin_fill()
    for i in range(4):
        forward(1000)
        left(90)
    end_fill()
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        file_txt = file.read()
    check = file_txt
    check1 = check[check.find('[', 1) + 1:check.find(']')]
    check1 = check1.replace(' ', '')
    check1 = check1.split(',')
    for i in range(len(check1)):
        check1[i] = float(check1[i])
    check = check[check.find(']') + 3:]
    N = int(file_txt[-2])
    check2 = check[:-4]
    check2 = check2.replace('[', '')
    check2 = check2.replace(']', '')
    check2 = check2.replace(' ', '')
    check2 = check2.split(',')
    a = []
    for i in range(len(check2)):
        check2[i] = int(check2[i])
    for i in range(round((sqrt(len(check2))))):
        a = a + [check2[i*(N-1):(i+1)*(N-1)]]
    check2 = a
    mas = [check1] + [check2] + [N]
    DrawGraph(mas, color, size)

def BFS(N, mas):
    check = [N]
    queue = [N]
    visited = [False] * mas[2]
    visited[N - 1] = True
    dot(mas, size, 'green', mas[0][N * 2 - 2], mas[0][N * 2 - 1] - size, N)
    while len(queue) != 0:
        for i in range(mas[2] - 1):
            if mas[1][queue[0] - 1][i] == 1:
                if not visited[i]:
                    queue += [i + 1]
                    check += [i + 1]
                    visited[i] = True
                    dot(mas, size, 'green', mas[0][i * 2], mas[0][i * 2 + 1] - size, i + 1)
        dot(mas, size, 'purple', mas[0][queue[0] * 2 - 2], mas[0][queue[0] * 2 - 1] - size, queue[0])
        queue = queue[1:]

    if set(check) == set(range(1, mas[2])):
        print("Граф зв'язаний")
    else:
        print("Граф не зв'язаний")
    pencolor(color)

def DFS(N, mas):
    stack = [N]
    visited = [False] * mas[2]
    visited[N - 1] = True
    check = [N]
    dot(mas, size, 'green', mas[0][N * 2 - 2], mas[0][N * 2 - 1] - size, N)
    while len(stack) != 0:
        current = stack[-1]
        found_next = False
        for i in range(mas[2] - 1):
            if mas[1][current - 1][i] == 1:
                if not visited[i]:
                    stack.append(i + 1)
                    visited[i] = True
                    check += [i + 1]
                    dot(mas, size, 'green', mas[0][i * 2], mas[0][i * 2 + 1] - size, i + 1)
                    found_next = True
                    break
        if not found_next:
            stack.pop()
            dot(mas, size, 'purple', mas[0][current * 2 - 2], mas[0][current * 2 - 1] - size, current)

    if set(check) == set(range(1, mas[2])):
        move(-350, 270)
        write("Граф зв'язаний", font=(20))
    else:
        move(-350, 270)
        write("Граф не зв'язаний", font=(20))
    pencolor(color)

def draw_left(x, y):
    global N, click_num, click, click_save, temp_x, temp_y, num_save, mas
    if tools.get() == 'draw':
        var = True
        click += 1
        click_num = 1
        if mas[2] > 1:
            i = 0
            while (i < mas[2] - 1) and (var == True):
                if (abs(x - mas[0][i * 2]) < size * 3) and (abs(y + size - mas[0][i * 2 + 1]) < size * 3):
                    var = False
                i += 1
            if var:
                move(x, y)
                dot(mas, size, color, x, y, mas[2])
                mas[2] += 1
                click_num += 1
                mas[0] += [x] + [y + size]
                for i in range(mas[2] - 2):
                    mas[1][i].append(0)
                mas[1].append([])
                for i in range(mas[2] - 1):
                    mas[1][mas[2] - 2].append(0)

        else:
            move(x, y)
            dot(mas, size, color, x, y, mas[2])
            mas[2] += 1
            mas[0] += [x] + [y + size]
            click_num += 1
            mas[1][0].append(0)

        num = Check_num(x, y)

        if click_num == 1:
            if Check_num(x, y) == num_save and click_save == click - 1:
                delete_dot(mas, x, y)
                temp_x = 0
                temp_y = 0
                click_save = 0
            elif click_save == click - 1 and Check_num(x, y) != num_save:
                num = Check_num(x, y)
                if mas[1][num - 1][num_save - 1] == 1:
                    delete_edge(mas, num, num_save)
                else:
                    draw_edge(mas, num, num_save)
                click_save = 0
                num_save = 0
            else:
                click_save = click
                num_save = Check_num(x, y)
    elif tools.get() == 'BFS':
        click_num = 1
        i = 0
        var = True
        while (i < mas[2] - 1) and (var == True):
            if (abs(x - mas[0][i * 2]) < size * 3) and (abs(y + size - mas[0][i * 2 + 1]) < size * 3):
                var = False
            i += 1
        if var:
            click_num += 1
        if click_num == 1:
            BFS(Check_num(x, y), mas)
    elif tools.get() == 'DFS':
        click_num = 1
        i = 0
        var = True
        while (i < mas[2] - 1) and (var == True):
            if (abs(x - mas[0][i * 2]) < size * 3) and (abs(y + size - mas[0][i * 2 + 1]) < size * 3):
                var = False
            i += 1
        if var:
            click_num += 1
        if click_num == 1:
            DFS(Check_num(x, y), mas)


speed(0)
N = 1
color = '#FF8000'
size = 25
click = 0
coordinates = []
connection = [[]]
onscreenclick(draw_left, 1)
pencolor(color)
click_save = 0
temp_x = 0
temp_y = 0
num_save = 0
mas = [coordinates, connection, N]
tools_list = ['draw', 'BFS', 'DFS']
tk = Tk()
res = Button(tk, text='reset', command=lambda: reset(mas, color, size))
open_file_button = Button(tk, text='open', command=lambda: open_file())
exit_button = Button(tk, text='exit', command=lambda: exit_file())
save_file_button = Button(tk, text='save', command=lambda: save_file(mas))
tools = Combobox(tk, values=tools_list)
tools.current(0)
res.pack()
open_file_button.pack()
exit_button.pack()
save_file_button.pack()
tools.pack()
mainloop()