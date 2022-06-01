from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("First game")
Active_player = 1
p1_lst = list()
p2_lst = list()

b1 = Button(root, padx=40, pady=40, command=lambda: play(1))
b1.grid(row=0, column=0)

b2 = Button(root, padx=40, pady=40, command=lambda: play(2))
b2.grid(row=0, column=1)

b3 = Button(root, padx=40, pady=40, command=lambda: play(3))
b3.grid(row=0, column=2)

b4 = Button(root, padx=40, pady=40, command=lambda: play(4))
b4.grid(row=1, column=0)

b5 = Button(root, padx=40, pady=40, command=lambda: play(5))
b5.grid(row=1, column=1)

b6 = Button(root, padx=40, pady=40, command=lambda: play(6))
b6.grid(row=1, column=2)

b7 = Button(root, padx=40, pady=40, command=lambda: play(7))
b7.grid(row=2, column=0)

b8 = Button(root, padx=40, pady=40, command=lambda: play(8))
b8.grid(row=2, column=1)

b9 = Button(root, padx=40, pady=40, command=lambda: play(9))
b9.grid(row=2, column=2)


def play(x):
    global Active_player
    global p1_lst
    global p1_lst
    if Active_player == 1:
        click(x, "X")
        root.title("Player2")
        p1_lst.append(x)
        Active_player = 2

    elif Active_player == 2:
        click(x, text="O")
        root.title("Player1")
        p2_lst.append(x)
        Active_player = 1
    print(p1_lst)
    print(p2_lst)
    winner()


def click(x, text):
    if x == 1:
        b1.config(text=text)
        b1["state"] = DISABLED
    if x == 2:
        b2.config(text=text)
        b2["state"] = DISABLED
    if x == 3:
        b3.config(text=text)
        b3["state"] = DISABLED
    if x == 4:
        b4.config(text=text)
        b4["state"] = DISABLED
    if x == 5:
        b5.config(text=text)
        b5["state"] = DISABLED
    if x == 6:
        b6.config(text=text)
        b6["state"] = DISABLED
    if x == 7:
        b7.config(text=text)
        b7["state"] = DISABLED
    if x == 8:
        b8.config(text=text)
        b8["state"] = DISABLED
    if x == 9:
        b9.config(text=text)
        b9["state"] = DISABLED


def winner():

def winner():
    if 1 in p1_lst and 2 in p1_lst and 3 in p1_lst or 4 in p1_lst and 5 in p1_lst and 6 in p1_lst or 7 in p1_lst and 8 in p1_lst and 9 in p1_lst or 1 in p1_lst and 4 in p1_lst and 7 in p1_lst or 2 in p1_lst and 5 in p1_lst and 8 in p1_lst or 3 in p1_lst and 6 in p1_lst and 9 in p1_lst or 1 in p1_lst and 5 in p1_lst and 9 in p1_lst or 3 in p1_lst and 5 in p1_lst and 7 in p1_lst:
        messagebox.showinfo(title="Congratulations", message="Player 1 is the winner")

    if 1 in p2_lst and 2 in p2_lst and 3 in p2_lst or 4 in p2_lst and 5 in p2_lst and 6 in p2_lst or 7 in p2_lst and 8 in p2_lst and 9 in p2_lst or 1 in p2_lst and 4 in p2_lst and 7 in p2_lst or 2 in p2_lst and 5 in p2_lst and 8 in p2_lst or 3 in p2_lst and 6 in p2_lst and 9 in p2_lst or 1 in p2_lst and 5 in p2_lst and 9 in p2_lst or 3 in p2_lst and 5 in p2_lst and 7 in p2_lst:
        messagebox.showinfo(title="Congratulations", message="Player 2 is the winner")



root.mainloop()
