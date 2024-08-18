from ttkbootstrap import *
from tkinter import messagebox
from random import choice

def Check(user_input):
    global user_wins, computer_wins, tie, Total
    result = 'You Won :)'
    Total += 1

    computer_pick = choice(['Rock', 'Paper', 'Scissors'])

    if user_input == computer_pick:
        tie += 1
        user_wins += 1
        computer_wins += 1
        result = "It is a tie!"

    elif user_input == "Rock" and computer_pick == "Scissors":
        user_wins += 1

    elif user_input == "Paper" and computer_pick == "Rock":
        user_wins += 1

    elif user_input == "Scissors" and computer_pick == "Paper":
        user_wins += 1

    else:
        computer_wins += 1
        result = 'You Lost :('

    lable.config(text=f' You picked {user_input} \n Computer picked {computer_pick}.\n {result}' )
    sre.set(f'{user_wins} / {Total} ')


win = Window(title='Rock Paper Scissors Game', themename='solar', size=(320, 200), resizable=(0, 0))
# win.iconbitmap('rock.ico')
win.grid_anchor('n')

user_wins, computer_wins, tie, Total = 0, 0, 0, 0
sre = StringVar()
sre.set(f'{user_wins} / {computer_wins} ')

Label(win, text='Rock Paper Scissors Game', font=('Arial', 12)).grid(row=0, column=0, columnspan=4, pady=5)
Score = Labelframe(win, text='Score', bootstyle='primary')
Score.grid(row=0, column=4, pady=5)
Label(Score, textvariable= sre ).pack()

Separator(win, orient='horizontal', bootstyle='danger').grid(row=1, column=0, columnspan=5, sticky='ew')

Label(win, text='Choose Your Option:').grid(row=2, column=0, columnspan=2, pady=10)

combobox = Combobox(win, values=['Rock', 'Paper', 'Scissors'], state='readonly', bootstyle='success')
combobox.grid(row=2, column=2, columnspan=2, pady=10)
combobox.set('Rock')
combobox.focus()

def Quit():
    if messagebox.askokcancel('Quit', 'Are you sure you want to quit?'):
        messagebox.showinfo('Result', f'You won {user_wins - tie} times.\n Computer won {computer_wins - tie} times.\n tie {tie} times.')
        win.destroy()

Button(win, text='Play', command=lambda: Check(combobox.get())).grid(row=3, column=2)
Button(win, text='Quit', command=lambda:Quit()).grid(row=3, column=3)

f = Labelframe(win, text='Result', bootstyle='primary')
f.grid(row=4, column=0, columnspan=4)
lable = Label(f, text='', font=('Arial', 10))
lable.pack()

win.mainloop()