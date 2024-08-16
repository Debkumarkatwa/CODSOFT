from tkinter import *
from tkinter import messagebox


# making a class for the buttons
class button:
    
    def __init__(self, text, row, column):
        self.text = text
        self.row = row
        self.column = column
        self.button = Button(btns_frame, text = self.text, fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(self.text)).grid(row = self.row, column = self.column, padx = 1, pady = 1)


# function for input button
def btn_click(item,text=None):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


# function for clear the input field
def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")


#function for backspace
def bt_back():
    global expression
    expression = expression[:-1]
    input_text.set(expression)


# to calculate the expression 
def bt_equal():
    global expression
    try: 
        result = str(eval(expression))
    except:
        messagebox.showerror("ERROR","Invaild Syntax")
    else:
        input_text.set(result)
        expression = result


# function for keyboard input
def key_press(event):
    global expression
    if event.char == '\r':
        bt_equal()
    elif event.char == '\b':
        bt_back()
    elif event.char == '\x1b':
        bt_clear()
    elif event.char == ',':
        pass
    elif event.char == '=':
        pass
    else:
        btn_click(event.char)


# binding the keys to the function
def bind_keys():
    for i in range(40,58):
        win.bind(chr(i),key_press)
    win.bind("<Return>",key_press)
    win.bind("<BackSpace>",key_press)
    win.bind("<Escape>",key_press)
    win.bind("=",key_press)
    
    # win.bind("<Key>",key_press)


# main() function--------------------------------
win = Tk() 
win.geometry("312x330")  
win.resizable(0, 0)  
win.title("Calculator")
# win.iconbitmap('cal logo.ico')
win.configure(background="white")

expression = ""
input_text = StringVar()
bind_keys()
 
# frame for the input field
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
#input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=20, bg="#eee", bd=0, justify=RIGHT, fg="#000",state='readonly').grid(row=0, column=0)

# making a button for backspace
back=Button(input_frame, text = "⌫",font=("arial",9,'bold'),fg = "white", width = 5, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: bt_back()).grid(row = 0, column = 1)

#'Frame' for the button 
btns_frame = Frame(win, width=312, height=272.5, bg="dark gray")
btns_frame.pack(side=RIGHT)

# first row
clear = Button(btns_frame, text = "C", fg = "white", width = 10, height = 3, bd = 0, bg = "green", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, padx = 1, pady = 1)

bra = button("(", 0, 1)
ket = button(")", 0, 2) 
divide = button("/", 0, 3,)
 
# second row
seven = button("7", 1, 0,)
eight = button("8", 1, 1)
nine = button("9", 1, 2) 
multiply = button("*", 1, 3)

# third row
four = button("4", 2, 0)
five = button("5", 2, 1)
six = button("6", 2, 2) 
minus = button("-", 2, 3)

# fourth row
one = button("1", 3, 0)
two = button("2", 3, 1)
three = button("3", 3, 2) 
plus = button("+", 3, 3)

# fifth row
zero = button("0", 4, 0)
point = button(".", 4, 1)
equals = Button(btns_frame, text = "=", fg = "white", width = 21, height = 3, bd = 0, bg = "green", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 2, padx = 1, pady = 1,columnspan=2)


win.mainloop()
