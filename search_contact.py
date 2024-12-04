import load_contacts
def search_contact(key, contacts):
    for contact in contacts:
        if key.isdigit():
            if contact['phone'] == key:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")
                return
        else:
            if contact['name'].lower() == key.lower() or contact['email'].lower() == key.lower():
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")
                return
    print("Contact not found.")
    return