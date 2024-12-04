import save_contact

def update_contact(phone, contacts):
    for contact in contacts:
        if contact['phone'] == phone:
            print("What you want to update?")
            print("(name, email, address, all)")
            choice = input("Enter your choice: ").lower()
            if choice == 'name':
                name = input("Enter new name for this contact: ")
                contact['name'] = name
                save_contact.save_contact(contacts)
                print(f"Name has been updated successfully")
                return

            elif choice == 'email':
                email = input("Enter new email for this contact: ")
                contact['email'] = email
                save_contact.save_contact(contacts)
                print(f"Email has been updated successfully")
                return

            elif choice == 'address':
                address = input("Enter new address for this contact: ")
                contact['address'] = address
                save_contact.save_contact(contacts)
                print(f"Address has been updated successfully")
                return

            elif choice == 'all':
                name = input("Enter new name for this contact: ")
                email = input("Enter new email for this contact: ")
                address = input("Enter new address for this contact: ")

                contact['name'] = name
                contact['email'] = email
                contact['address'] = address
                save_contact.save_contact(contacts)
                print(f"All details have been updated successfully")
                return

            else:
                print("Invalid Choice. Please try again with valid choice.")
                return

    print("No such contact found!")
    return
