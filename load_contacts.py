import os

def load_contacts(file_path="Contacts.csv"):
    contacts = []
    if not os.path.exists(file_path):
        return "No 'Contact.csv' file exists!"
    with open(file_path, "r") as file:
        for line in file:
            name, phone, email, address = line.strip().split(",")
            contacts.append({
                "name" : name,
                "phone" : phone,
                "email" : email,
                "address" : address
            })
        return contacts