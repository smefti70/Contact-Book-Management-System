import save_contact

def add_contact(contacts):
    name = input("Enter the name of the contact: ").strip()
    if not all(part.isalpha() for part in name.split()):
        print("Name must contain only alphabets.")
        return

    phone = input("Enter the phone number of the contact: ").strip()
    if not phone.isdigit():
        print("Phone number must be numeric.")
        return

    for existing_contact in contacts:
        if existing_contact["phone"] == phone:
            print("Contact already exists.")
            return

    email = input("Enter the email of the contact: ")
    if "@" not in email or "." not in email:
        print("Invalid email format.")
        return

    address = input("Enter the address of the contact: ")

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(new_contact)
    save_contact.save_contact(contacts)
    print(f"Contact {name} added successfully.")