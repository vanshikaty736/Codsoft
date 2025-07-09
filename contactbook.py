def add_contact(contacts):
    """Adds a new contact to the contact list."""
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    """Displays all contacts in the contact list."""
    if not contacts:
        print("No contacts to display.")
        return
    print("\n--- Your Contacts ---")
    for i, contact in enumerate(contacts):
        print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}")
    print("---------------------")

def search_contact(contacts):
    """Searches for a contact by name or phone number."""
    search_term = input("Enter name or phone number to search: ").lower()
    found_contacts = []
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            found_contacts.append(contact)

    if not found_contacts:
        print("No matching contacts found.")
        return

    print("\n--- Search Results ---")
    for contact in found_contacts:
        print(f"Name: {contact['name']}")
        print(f"  Phone: {contact['phone']}")
        print(f"  Email: {contact['email']}")
        print(f"  Address: {contact['address']}")
        print("--------------------")

def update_contact(contacts):
    """Updates an existing contact's details."""
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter the number of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print(f"Updating contact: {contact['name']}")
            contact['name'] = input(f"Enter new name (current: {contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Enter new phone (current: {contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_contact(contacts):
    """Deletes a contact from the contact list."""
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            print(f"Contact '{deleted_contact['name']}' deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the contact book application."""
    contacts = []

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
