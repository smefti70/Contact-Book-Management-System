import save_contact
def delete_contact(name, contacts):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            save_contact.save_contact(contacts)
            print(f"Contact {name} deleted successfully.")
            return
    print("Contact not found.")
