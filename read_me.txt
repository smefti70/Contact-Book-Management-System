Contact Book Management System
------------------------------
This project is a Python-based Contact Book Management System designed to add, view, search, update, and delete contacts. It uses a modular approach, with each functionality implemented in separate Python files.

Dependencies:
- Python Standard Library (no external libraries required)
- CSV file to store contact data (Contacts.csv)

How to Run:
1. Ensure Python 3.x is installed on your system.
2. Place all the files in the same folder.
3. Run `main.py` to start the Contact Book Management System.

File Structure:
main.py (Entry Point):
|-- add_contact.py      # Adds new contacts
|-- view_contact.py     # Displays all contacts in a formatted manner
|-- load_contact.py     # Loads contacts from the CSV file
|-- save_contact.py     # Saves updated contacts to the CSV file
|-- search_contact.py   # Searches for contact by name
|-- update_contact.py   # Updates contact details
|-- delete_contact.py   # Deletes a contact by name