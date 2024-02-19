from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def wynik(chosen, enemy):  # who wins
    if (chosen == enemy):
        tie()
    elif (chosen == 'rock'):
        if (enemy == 'paper'):
            lose()
        elif (enemy == 'scissors'):
            win()
    elif (chosen == 'paper'):
        if (enemy == 'rock'):
            win()
        elif (enemy == 'scissors'):
            lose()
    elif (chosen == 'scissors'):
        if (enemy == 'rock'):
            lose()
        elif (enemy == 'paper'):
            win()

def random_choice():
    choose = ['rock','paper','scissors']
    return random.choice(choose)


def battler():  # If player picks rock
    enemy=random_choice()
    mess1.config(text="Rock vs " + (enemy.capitalize()), bg='black', fg="White", width=500,
                 font=('Helvetica', 25, 'bold'))
    wynik('rock', enemy)


def battlep():  # If player picks paper
    enemy=random_choice()
    mess1.config(text="Paper vs " + (enemy.capitalize()), bg='black', fg="white", width=500,
                 font=('Helvetica', 25, 'bold'))
    wynik('paper', enemy)


def battles():  # If player picks scissors
    enemy=random_choice()
    mess1.config(text="Scissors vs " + (enemy.capitalize()), bg='black', fg="white", width=500,
                 font=('Helvetica', 25, 'bold'))
    wynik('scissors', enemy)


def end():  # Button CLOSES WINDOW
    root.destroy()


def info():  # Button shows info
    messagebox.showinfo("showinfo", "The rock-paper-scissors program operates by prompting players to choose one of three options (rock, paper, or scissors) and then determining the winner based on the rules: rock crushes scissors, scissors cuts paper, and paper covers rock. Enemy's choice is random.")


def win():  # Player Won
    mess.config(text="You Win!", bg='black', fg="green", width=500, font=('Helvetica', 50, 'bold'))


def lose():  # Player Lose
    mess.config(text="You Lose!", bg='black', fg="Red", width=500, font=('Helvetica', 50, 'bold'))


def tie():  # Both players picked the same option
    mess.config(text="It is a tie!", bg='black', fg="blue", width=500, font=('Helvetica', 50, 'bold'))


root = Tk()
root.title("Rock paper scissors")
root.geometry("500x500")
icon = PhotoImage(file="ico.png")
root.iconphoto(True, icon)
root.resizable(width=False, height=False)
root.config(bg="Black")

mess = Message(root, text="Welcome to the Rock, Paper, Scissors Game", bg='Black', fg="White", width=500, padx=20,
               pady=20, font=('Helvetica', 30, 'bold'))
mess.pack()

canvas = Canvas(root, width=500, height=500, bg='black', highlightthickness=0)
canvas.pack()
mess = Message(canvas, text="Choose wisely!", bg='black', fg="white", width=350, padx=20, pady=20,
               font=('Helvetica', 10, 'bold'), borderwidth='0')
mess.grid(sticky=W + E, row=0, column=1)
rockphoto = PhotoImage(file="1.png")
paperphoto = PhotoImage(file="3.png")
scissorsphoto = PhotoImage(file="2.png")
button1 = Button(canvas, image=rockphoto, text="Rock", bg='white', height='68', activebackground='black',
                 activeforeground='white', borderwidth='0', command=battler)
button2 = Button(canvas, image=paperphoto, text="Paper", bg='white', height='68', activebackground='black',
                 activeforeground='white', borderwidth='0', command=battlep)
button3 = Button(canvas, image=scissorsphoto, text="Scissors", bg='white', height='68', activebackground='black',
                 activeforeground='white', borderwidth='0', command=battles)
button1.grid(row=1, column=0, sticky=N, pady=5)
button2.grid(row=1, column=1, sticky=N, pady=5)
button3.grid(row=1, column=3, sticky=N, pady=5)
c2 = Frame(root, width=500, height=300, bg='black', highlightthickness=0)
c2.pack()
mess1 = Message(c2, text="", background='BLACK', fg="white", width='1000', font=('Helvetica', 20))
mess1.grid(row=1, column=1)
mess = Message(c2, text=":)", bg='black', font=('Helvetica', 30, 'bold'))
mess.grid(row=2, column=1)
c3 = Frame(root, width=200, height=200, bg='black', highlightthickness=1)
c3.pack()
button3 = Button(c3, text="END", bg='white', height='2', width=20, activebackground='black', activeforeground='white',
                 borderwidth=1, command=end)
button3.pack(side=RIGHT)
button3 = Button(c3, text="INFO", bg='white', height='2', width=20, activebackground='black', activeforeground='white',
                 borderwidth=1, command=info)
button3.pack(side=RIGHT)
root.mainloop()
