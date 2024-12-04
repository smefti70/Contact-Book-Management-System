import load_contacts
def search_contact(name, contacts):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return
    print("Contact not found.")
    return