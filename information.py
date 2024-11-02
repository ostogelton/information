# Simple Contact Book

# Dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact for {name} added!")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("\nContacts:")
        for name, details in contacts.items():
            print(f"{name} - Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("No contacts available.")

# Function to search for a contact
def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        details = contacts[name]
        print(f"Found: {name} - Phone: {details['phone']}, Email: {details['email']}")
    else:
        print(f"No contact found with the name {name}.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted!")
    else:
        print(f"No contact found with the name {name}.")

# Main program loop
while True:
    print("\nChoose an option:")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
