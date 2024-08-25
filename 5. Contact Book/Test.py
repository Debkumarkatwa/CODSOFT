class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:

    def add_contact(contact:Contact):
        with open(contact_file_path, 'a') as file:
            file.write(f"{contact.name}||{contact.phone_number}||{contact.email}||{contact.address}\n")

    def view_contacts():
        with open(contact_file_path, 'r') as file:
            line = file.readlines()[2:]
            for i in line:
                print(f'|| Name: {i.strip().split('||')[0]} || Phone Number: {i.strip().split("||")[1]} || Email: {i.strip().split("||")[2]} || Address: {i.strip().split("||")[3]} ||')
            
    def search_contact(search_term):
        with open(contact_file_path, 'r') as file:
            for i in file.readlines()[2:]:
                if search_term in {i.strip().split('||')[0].lower()} or search_term in {i.strip().split("||")[1]}:
                    print(f'|| Name: {i.strip().split('||')[0]} || Phone Number: {i.strip().split("||")[1]} || Email: {i.strip().split("||")[2]} || Address: {i.strip().split("||")[3]} ||')
                    break
            else:
                print("Contact not found")

    def update_contact(search_term): 
        with open(contact_file_path, 'r') as file:
            lines = file.readlines()
            
            for i in range(2, len(lines)):
                if search_term in lines[i].strip().split('||')[0].lower() or search_term in lines[i].strip().split('||')[1]:
                    print('Contact founded.......')
                    new_contact = Contact(input("Enter new name(Blank for keep old deta): "), input("Enter new phone number(Blank for keep old deta): "), input("Enter new email(Blank for keep old deta): "), input("Enter new address(Blank for keep old deta): "))                   
                    
                    new_contact.name = new_contact.name if new_contact.name else lines[i].strip().split('||')[0]
                    new_contact.phone_number = new_contact.phone_number if new_contact.phone_number else lines[i].strip().split('||')[1]
                    new_contact.email = new_contact.email if new_contact.email else lines[i].strip().split('||')[2]
                    new_contact.address = new_contact.address if new_contact.address else lines[i].strip().split('||')[3]
                    
                    lines[i] = f"{new_contact.name}||{new_contact.phone_number}||{new_contact.email}||{new_contact.address}\n"
                    with open(contact_file_path, 'w') as file:
                        for i in lines:
                            file.write(i)
                    
                    print("Contact updated successfully")
                    break
            else:
                print("Contact not found")

    def delete_contact(search_term):
        with open (contact_file_path, 'r') as file:
            lines = file.readlines()
            
            for i in range(2, len(lines)):
                if search_term in lines[i].strip().split('||')[0].lower() or search_term in lines[i].strip().split('||')[1]:
                    lines.pop(i)
                    with open(contact_file_path, 'w') as file:
                        for i in lines:
                            file.write(i)

                    print("Contact deleted successfully")
                    break
            else:
                print("Contact not found")

# # Example usage:
# contact_book = ContactBook()
global contact_file_path
contact_file_path = 'Contact_Details.csv'  
with open(contact_file_path, 'a+') as file: # create a file if not exists and write the header
    if file.tell() <= 0:
        file.write('--Name--||--Phone Number--||--Email--||--Address--\n\n')

# menu--------------------------------
while True:
    print("----------------------")
    print("0. Exit")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    
    choice = input("Enter your choice: ")
    if choice == '0': break

    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone_number, email, address)
        ContactBook.add_contact(contact)
        print("Contact added successfully")

    elif choice == '2':
        ContactBook.view_contacts()

    elif choice == '3':
        search_term = input("Enter search term: ")
        ContactBook.search_contact(search_term.lower())

    elif choice == '4':
        search_term = input("Enter search term: ")
        ContactBook.update_contact(search_term.lower())
        
    elif choice == '5':
        search_term = input("Enter search term: ")
        ContactBook.delete_contact(search_term.lower())
        

    else:
        print("Invalid choice")
