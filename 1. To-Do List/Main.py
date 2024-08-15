from ttkbootstrap import *
from tkinter import messagebox, Listbox
from time import strftime, localtime


class Task:
    def __init__(self, name, description, date=None):
        self.name = name
        self.description = description
        self.date = date if date else strftime('%d-%m-%Y {%H:%M:%S}', localtime())

    def __str__(self):
        return f"{self.name} - {self.description} - {self.date}"


class TodoList:
    global window

    def __init__(self, file_path):
        self.tasks:list[Task] = []
        self.file_path = file_path
        try:
            with open(self.file_path, 'r') as f:
                for line in f.readlines()[2:]:
                    name, description, date = line.strip().split('||')
                    self.tasks.append(Task(name, description, date))
        except FileNotFoundError:
            with open (filepath, 'w') as f:
                f.write('--Name--||--Description--||--Date--\n\n')   # if file not exists, create a new file with header

    def add_task(self, task:Task):
        self.tasks.append(task)
        listbox.insert(END, task.name)
        with open(self.file_path, 'a') as f:
            f.write(f"{task.name}||{task.description}||{task.date}\n")
        
        messagebox.showinfo('Task Added', 'Task added successfully!')
        window.destroy()

    def update_task(self, new_name, new_description, i):
        self.tasks[i].name = new_name if new_name else self.tasks[i].name
        self.tasks[i].description = new_description if new_description else self.tasks[i].description
        self.tasks[i].date = strftime('%d-%m-%Y {%H:%M:%S}', localtime())
                
        listbox.delete(0, END)
        for task in self.tasks:    listbox.insert(END, task.name)

        with open(self.file_path, 'w') as f:
            f.write('--Name--||--Description--||--Date--\n\n')
            for task in self.tasks:
                f.write(f"{task.name}||{task.description}||{task.date}\n")

        messagebox.showinfo('Task Updated', 'Task updated successfully!')
        window.destroy()


def Add(name):
    if not name:
        messagebox.showerror('ERROR','Task name cannot be empty!')
        return
    Name.delete(0, END)
    global window
    window = Toplevel(win, size=(300, 200))

    Label(window, text='Enter task description:', bootstyle='primary').pack()
    description = Entry(window, font=('arial', 12, 'bold'))
    description.pack()
    Button(window, text='Save', command=lambda: todolist.add_task(Task(name, description.get())), bootstyle='outline-warning').pack()


def Delete(task):
    global todolist
    for i, t in enumerate(todolist.tasks):
        if t.name == task:
            todolist.tasks.pop(i)
            listbox.delete(0, END)
            for task in todolist.tasks:    listbox.insert(END, task.name)
            with open(filepath, 'w') as f:
                f.write('--Name--||--Description--||--Date--\n\n')
                for task in todolist.tasks:
                    f.write(f"{task.name}||{task.description}||{task.date}\n")
            break
    else:
        messagebox.showerror('ERROR','Task not found!\nPlease select a task from list to delete.')


def display(task):
    global todolist
    for i, t in enumerate(todolist.tasks):
        if t.name == task:
            messagebox.showinfo('Task', f"Name: {t.name}\nDescription: {t.description}\nDate: {t.date}")
            break
    else:
        messagebox.showerror('ERROR','Task not found!\nPlease select a task from list to display.')


def update(task):
    global todolist , window
    for i, t in enumerate(todolist.tasks):
        if t.name == task:
            window = Toplevel(win, size=(300, 200))
            Label(window, text='Enter new name:', bootstyle='primary').pack()
            new_name = Entry(window, font=('arial', 12, 'bold'))
            new_name.pack()
            Label(window, text='Enter new description:', bootstyle='primary').pack()
            new_description = Entry(window, font=('arial', 12, 'bold'))
            new_description.pack()
            Button(window, text='Submit', command=lambda: todolist.update_task(new_name.get(),new_description.get(),i), bootstyle='outline-warning').pack()
            break
    else:
        messagebox.showerror('ERROR','Task not found!\nPlease select a task from list to update.')


win = Window(title='To-Do List', themename='solar', size=(290,340), resizable=(0,0))
# win.iconbitmap()

filepath = 'tasks.csv'
todolist = TodoList(file_path = filepath)

f1 = Frame(win, padding=10, relief='flat', borderwidth=5)
f1.pack(side=TOP, fill=X)

Label(f1, text='Enter New Task Name', bootstyle='primary', font=('arial', 10, 'bold')).grid(row=0, column=0, sticky='w')
Name = Entry(f1, font=('arial', 12, 'bold'), bootstyle='warning')
Name.grid(row=1, column=0)
Name.focus()
Button(f1, text='Add', command=lambda:Add(Name.get()),cursor='hand2', bootstyle='outline-primary', width=5).grid(row=1, column=1)

f2 = Frame(win, padding=1, relief='flat', borderwidth=5, bootstyle='secondary')
f2.pack(fill=BOTH)
listbox = Listbox(f2, font=('arial', 12, 'bold'))
listbox.pack(fill=X, expand=True, side=LEFT)
scroll = Scrollbar(f2, command=listbox.yview, bootstyle='info rounded')
scroll.pack(fill=Y, side=RIGHT)
listbox.config(yscrollcommand=scroll.set)
for task in todolist.tasks:
    listbox.insert(END, task.name)

f3 = Frame(win, relief='flat', borderwidth=5, bootstyle='success')
f3.pack(fill=BOTH, side=BOTTOM)

Button(f3, text='Display Task', command=lambda:display(str(listbox.get(ANCHOR))), bootstyle='primary', cursor='hand2').grid(row=0, column=0, padx=2)
Button(f3, text='Update Task', command=lambda:update(str(listbox.get(ANCHOR))), bootstyle='warning', cursor='hand2').grid(row=0, column=1, padx=2)
Button(f3, text='COMPLETED', command=lambda:Delete(str(listbox.get(ANCHOR))), bootstyle='danger', cursor='hand2').grid(row=0, column=2, padx=2)



win.mainloop()