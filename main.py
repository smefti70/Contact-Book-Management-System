import add_contact
import view_contacts
import load_contacts
import search_contact
import delete_contact
import update_contact

contacts = load_contacts.load_contacts()

while True:
    print("\nContact Book Management System")
    print("1. Add a Contact")
    print("2. View All Contacts")
    print("3. Search a Contact")
    print("4. Update a Contact")
    print("5. Delete a Contact")
    print("0. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Choice!\nPlease enter a number.")
        continue

    if choice == 1:
        add_contact.add_contact(contacts)

    elif choice == 2:
        if not contacts:
            print("No contacts available")
        else:
            view_contacts.view_contacts()

    elif choice == 3:
        if not contacts:
            print("No contacts available")
        else:
            name = input("Enter the contact name to search: ")
            search_contact.search_contact(name, contacts)

    elif choice == 4:
        phone = input("Enter the Contact Number you want to update: ")
        print(f"Your entered number is {phone}!")
        update_contact.update_contact(phone, contacts)

    elif choice == 5:
        view_contacts.view_contacts()
        name = input("Enter the Contact Name to be deleted: ")
        delete_contact.delete_contact(name, contacts)

    elif choice == 0:
        print("\nThanks for using Contact Book Management System.")
        break

    else:
        print("Invalid choice.\nPlease try again with a valid choice.")
