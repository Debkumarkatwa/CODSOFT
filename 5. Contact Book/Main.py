from ttkbootstrap import *
from tkinter import messagebox, Listbox
import re

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

def add_contact(contact:Contact):
        global Contact_details_list,window
        Contact_details_list.append(contact)
        with open(contact_file_path, 'a') as file:
            file.write(f"{contact.name}||{contact.phone_number}||{contact.email}||{contact.address}\n")
        messagebox.showinfo('Contact Added', 'Contact added successfully!')
        window.destroy()
        number.focus_set()
        num.set(contact.name)

def update_contact(contact:Contact):
    global Contact_details_list, window
    Contact_details_list[listbox.curselection()[0]] = contact
    listbox.delete(0, END)
    for i in Contact_details_list:
        listbox.insert(END, f"{i.name}   -   {i.phone_number}")
    with open(contact_file_path, 'w') as file:
        file.write('--Name--||--Phone Number--||--Email--||--Address--\n\n')
        for i in Contact_details_list:
            file.write(f"{i.name}||{i.phone_number}||{i.email}||{i.address}\n")
    messagebox.showinfo('Contact Updated', 'Contact updated successfully!')
    window.destroy()
    number.focus_set()

def Add(search_term):
    global Contact_details_list, window
    for i in Contact_details_list:
        if search_term == i.name or search_term == i.phone_number:
            if not(messagebox.askyesno('ERROR','Contact already exists!\nDo you want to continue?')): return

    window = Toplevel('Add Contact', size=(320, 220), resizable=(0,0))

    new_name, new_number = StringVar(), IntVar()
    if search_term.isdigit() and len(search_term) >= 10:        new_number.set(int(search_term))
    elif search_term == 'Search Name/Number':       new_name.set('')
    else:       new_name.set(search_term)
    
    Label(window, text='\t   Add Contact   \t', font=('Imprint MT Shadow',15,'bold','underline')).grid(row=0, column=0, columnspan=2, pady=5, sticky='n')
    Label(window, text='Name:', font=('Imprint MT Shadow',12,'bold','underline')).grid(row=1, column=0, padx=4, pady=2)
    a = Entry(window, width=24, font=('Imprint MT Shadow', 12, 'bold'), bootstyle='warning', textvariable=new_name)
    a.grid(row=1, column=1, padx=2, pady=2)

    Label(window, text='Number:', font=('Imprint MT Shadow',12,'bold','underline')).grid(row=2, column=0, padx=4, pady=2)
    b = Entry(window, width=24, font=('Imprint MT Shadow', 12, 'bold'), bootstyle='warning', textvariable=new_number)
    b.grid(row=2, column=1, padx=2, pady=2)

    Label(window, text='Gmail:', font=('Imprint MT Shadow',12,'bold','underline')).grid(row=3, column=0, padx=4, pady=2)
    mail = Entry(window, width=36, font=('arial', 8, 'bold'), bootstyle='warning')
    mail.grid(row=3, column=1, padx=2, pady=2)
    Label(window, text='Address:', font=('Imprint MT Shadow',12,'bold','underline')).grid(row=4, column=0, padx=4, pady=2)
    address = Entry(window, width=36, font=('arial', 8, 'bold'), bootstyle='warning')
    address.grid(row=4, column=1, padx=2, pady=2)
    Button(window, text='Save Contact', style='outline-success', width=12, cursor='hand2', command=lambda:add_contact(Contact(a.get(), b.get(), mail.get(), address.get()))).grid(row=5, column=1, padx=2, pady=2, columnspan=2)
    window.mainloop()

def Delete(i):    
    global Contact_details_list    
    if not i:
        messagebox.showerror('ERROR','Select a contact to delete!')
        return
     
    for j in Contact_details_list:
        if j.name == i:
            i = Contact_details_list.index(j)
            break
        
    if messagebox.askyesno('Delete Contact', f"Confirm to delete - {Contact_details_list[i].name}'s - contact?"):
        Contact_details_list.pop(i[0])
        listbox.delete(i[0])
        with open(contact_file_path, 'w') as file:
            file.write('--Name--||--Phone Number--||--Email--||--Address--\n\n')
            for i in Contact_details_list:
                file.write(f"{i.name}||{i.phone_number}||{i.email}||{i.address}\n")

def Update(i):
    global Contact_details_list, window
    if not i:
        messagebox.showerror('ERROR','Select a contact to update!')
        return
 
    for j in Contact_details_list:
        if j.name == i:
            i = Contact_details_list.index(j)
            break

    window = Toplevel('Update Contact', size=(320, 220), resizable=(1,0))
    new_name, new_number = StringVar(), IntVar()
    new_name.set(Contact_details_list[i].name)
    new_number.set(Contact_details_list[i].phone_number)
    
    Label(window, text='\t   Update Contact   ', font=('Imprint MT Shadow',15,'bold','underline')).grid(row=0, column=0, columnspan=2, pady=5, sticky='n')
    Label(window, text='Name:', font=('Imprint MT Shadow',12,'bold','underline')).grid(row=1, column=0, padx=4, pady=2)
    a = Entry(window, width=24, font=('Imprint MT Shadow', 12, 'bold'), bootstyle='warning', textvariable=new_name)
    a.grid(row=1, column=1, padx=2, pady=2)

    Label(window, text='Number:', font=('Imprint MT Shadow',12,'bold','underline')).grid(row=2, column=0, padx=4, pady=2)
    b = Entry(window, width=24, font=('Imprint MT Shadow', 12, 'bold'), bootstyle='warning', textvariable=new_number)
    b.grid(row=2, column=1, padx=2, pady=2)

    Label(window, text='Gmail:', font=('Imprint MT Shadow',12,'bold','underline')).grid(row=3, column=0, padx=4, pady=2)
    mail = Entry(window, width=36, font=('arial', 8, 'bold'), bootstyle='warning')
    mail.grid(row=3, column=1, padx=2, pady=2)
    mail.insert(0, Contact_details_list[i].email)
    Label(window, text='Address:', font=('Imprint MT Shadow',12,'bold','underline')).grid(row=4, column=0, padx=4, pady=2)
    address = Entry(window, width=36, font=('arial', 8, 'bold'), bootstyle='warning')
    address.grid(row=4, column=1, padx=2, pady=2)
    address.insert(0, Contact_details_list[i].address)
    Button(window, text='Save Contact', style='outline-success', width=12, cursor='hand2', command=lambda:update_contact(Contact(a.get(), b.get(), mail.get(), address.get()))).grid(row=5, column=1, padx=2, pady=2, columnspan=2)
    window.mainloop()


# main window----------------------------------------------
win = Window('Contact Book', 'solar', size=(350, 450), resizable=(0,0))

Label(win, text='     CONTACTS     ', font=('Imprint MT Shadow',20,'bold','underline')).grid(row=0, column=0, columnspan=2, pady=5, sticky='n')

f = Frame(win, bootstyle='warning', padding=5)
f.grid(row=1, column=0, columnspan=2, pady=2, padx=5)
frame = Frame(f, bootstyle='dark', padding=2)
frame.pack()

def on_entry_click(event):
   if num.get() == "Search Name/Number":
      num.set('')
def on_focus_out(event):
   if num.get() == "":
      num.set("Search Name/Number")
def get_data(*args):
    if num.get() == "Search Name/Number":    return

    listbox.delete(0, END)
    for i in Contact_details_list:
        if re.match(num.get(), i.name, re.IGNORECASE) or re.search(num.get(), i.phone_number, re.IGNORECASE):
            listbox.insert(END, f"{i.name}   -   {i.phone_number}")

num = StringVar()
num.set("Search Name/Number")
num.trace_add('write', get_data)
number = Entry(frame, width=35, textvariable=num, bootstyle='primary')
number.grid(row=0, column=0, padx=1)
number.focus_set() 
number.bind("<FocusIn>", on_entry_click)
number.bind("<FocusOut>", on_focus_out)
Button(frame, text='Add Contact', style='outline-success', width=12, command=lambda:Add(number.get()), cursor='hand2').grid(row=0, column=1, padx=1)

f1 = Frame(win, bootstyle='primary', padding=3)
f1.grid(row=2, column=0, columnspan=2, pady=5, padx=5, sticky='nswe')
frame1 = Labelframe(f1, bootstyle='warning', text='Contacts', padding=5)
frame1.pack(fill='both', expand=True)

Label(frame1, text='\tName', font=('arial', 10, 'bold', 'underline')).grid(row=0, column=0, padx=2, sticky='w')
Label(frame1, text='\tNumber ', font=('arial', 10, 'bold', 'underline')).grid(row=0, column=1, padx=2, sticky='w')

def Details(event):
    event = event.widget
    value = (event.get(event.curselection()[0])).split('   -   ')[0]
    for i in Contact_details_list:
        if i.name == value:
            if messagebox.askyesnocancel('Details', f'Name: {i.name}\nPhone Number: {i.phone_number}\nEmail: {i.email}\nAddress: {i.address}\n\n ---WANT TO UPDATE THE CONTACT??') :
                Update(Contact_details_list.index(i))
            break

listbox = Listbox(frame1, width=33, height=13, justify='center', cursor='hand2')
listbox.grid(row=1, column=0, padx=2, pady=2, sticky='w', columnspan=2)
listbox.bind('<Return>', Details)
listbox.configure(background='lightgray', foreground='black', selectbackground='blue', selectforeground='white', font=('Imprint-MT-Shadow', 12, 'underline'))

scroll = Scrollbar(frame1, command=listbox.yview , bootstyle='success rounded')
scroll.grid(row=1, column=2, sticky='ns')
listbox.config(yscrollcommand=scroll.set)

global Contact_details_list
contact_file_path = 'Contact_Details.csv'  
Contact_details_list:list[Contact] = []

try:
    with open(contact_file_path, 'r') as file: 
        for j,i in enumerate(file.readlines()[2:]):
            Contact_details_list.append(Contact(i.strip().split('||')[0], i.strip().split('||')[1], i.strip().split('||')[2], i.strip().split('||')[3]))
            listbox.insert(j, f"{Contact_details_list[j].name}   -   {Contact_details_list[j].phone_number}")
except FileNotFoundError:
    with open(contact_file_path, 'w') as file:
        file.write('--Name--||--Phone Number--||--Email--||--Address--\n\n')

f2 = Frame(win, bootstyle='primary', padding=3)
f2.grid(row=3, column=0, columnspan=2, pady=1, padx=5, sticky='nswe')

Button(f2, text='Delete Contact', style='outline-danger', width=14, command=lambda:Delete((listbox.get(listbox.curselection()[0])).split(' - ')[0]), cursor='hand2').grid(row=0, column=0, padx=1)
Button(f2, text='Update Contact', style='outline-info', width=14, command=lambda:Update((listbox.get(listbox.curselection()[0])).split(' - ')[0]), cursor='hand2').grid(row=0, column=1, padx=1)
Button(f2, text='Exit', style='warning', width=14, command=win.quit, cursor='hand2').grid(row=0, column=2, padx=1)


win.mainloop()
