# 2.Contact Book 
# Develop a contact book that can save, edit, and search contacts. 
# Handle errors such as duplicate entries, empty fields, and wrong phone number format. 


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add(self):
        try:
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone Number: ").strip()

            if not name or not phone:
                raise ValueError("Fields cannot be empty")

            if name in self.contacts:
                raise ValueError("Duplicate contact")

            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Invalid phone number format")

            self.contacts[name] = phone
            print("Contact added successfully")

        except ValueError as e:
            print("Error:", e)


    def edit(self):
        try:
            name = input("Enter contact name to edit: ").strip()

            if name not in self.contacts:
                raise KeyError("Contact not found")

            phone = input("Enter new phone number: ").strip()

            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Invalid phone number")

            self.contacts[name] = phone
            print("Contact updated")

        except (KeyError, ValueError) as e:
            print("Error:", e)

    def search(self):
        name = input("Enter name to search: ").strip()

        if name in self.contacts:
            print(f"Name: {name}, Phone: {self.contacts[name]}")
        else:
            print("Contact not found")

    def display(self):
        if not self.contacts:
            print("Contact book is empty")
        else:
            for name, phone in self.contacts.items():
                print(f"{name} : {phone}")


book = ContactBook()

while True:
    print("\n1.Add Contact")
    print("2.Edit Contact")
    print("3.Search Contact")
    print("4.Display Contacts")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book.add()
    elif choice == "2":
        book.edit()
    elif choice == "3":
        book.search()
    elif choice == "4":
        book.display()
    elif choice == "5":
        break
    else:
        print("Invalid choice")

