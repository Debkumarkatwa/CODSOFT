from ttkbootstrap import *
from random import choice
import string


def Generator(length, num, schar):
    global Output

    characters = string.ascii_letters
    if num:    characters += string.digits
    if schar:    characters += '#$%&*./?@|'

    password = ''
    for x in range(length):
        password += choice(characters)

    if num and schar:
        password = password[:-2] + choice('#$%&*./?@|') + choice(string.digits) 

    elif num:
        password = password[:-1] + choice(string.digits)
    
    elif schar:
        password = password[:-1] + choice('#$%&*./?@|')
    
    Output.set(password)


win = Window("PASSWORD GENERATOR", 'solar', size=(450,250), resizable=(0, 0) )

heading = Label(win, text = 'PASSWORD GENERATOR', font ='arial 15 bold').pack()

Num = BooleanVar()
Schar = BooleanVar()
Output = StringVar()
###select password length
Label(win, text = 'PASSWORD LENGTH', font = 'arial 10 bold').place(x = 50, y= 50)
Input = Spinbox(win, from_= 8, to_ = 20, width = 15, bootstyle='warning')
Input.place(x = 200, y= 50)
Input.focus()
Input.set(8)
Checkbutton(win, text = 'INCLUDE NUMBERS', variable= Num, bootstyle='info-round-toggle', cursor='hand2').place(x = 50, y= 80)
Checkbutton(win, text = 'INCLUDE SPECIAL CHARACTERS', variable= Schar, bootstyle='info-round-toggle', cursor='hand2').place(x = 50, y= 110)

Button(win, text = "GENERATE PASSWORD", command = lambda:Generator(int(Input.get()), Num.get(), Schar.get()), cursor='hand2').place(x = 150, y= 130)

f = Frame(win, bootstyle='success', padding=5)
f.place(x = 25, y= 170)
frame = Frame(f, bootstyle='dark', padding=2)
frame.pack()
# YOUR PASSWORD
Label(frame, text = '--- YOUR PASSWORD ---', font = 'arial 10 bold').grid(row=0, column=0, padx=5)
Entry(frame, width=50, textvariable=Output, bootstyle='warning', justify='center', font='arial 10').grid(row=1, column=0, padx=5)



win.mainloop()
