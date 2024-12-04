def save_contact(contacts):
    with open("Contacts.csv", "w") as file:
        for contact in contacts:
            content = f"{contact['name']},{contact['phone']},{contact['email']},{contact['address']}\n"
            file.write(content)
