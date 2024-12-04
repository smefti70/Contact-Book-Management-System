def view_contacts():
    print("Here are the contacts:")
    print(
        f"{'Name':<25}{'Phone No':<25}{'Email Address':<25}{'Address':<25}"
    )
    print(
        f"{'------':<25}{'--------':<25}{'--------------':<25}{'--------':<25}"
    )
    with open("Contacts.csv", "r") as file:
        for line in file:
            contact_details = line.strip().split(",")
            print(
                f"{contact_details[0]:<22}{contact_details[1]:<20}{contact_details[2]:<33}{contact_details[3]:<20}"
            )