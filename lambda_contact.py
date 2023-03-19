import sqlite3

# Connect to the database
conn = sqlite3.connect('contacts.db')

# Create a table to store contacts
conn.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  phone TEXT);''')

# Add a contact to the database
add_contact = lambda name, phone: conn.execute("INSERT INTO contacts (name, phone) VALUES (?, ?);", (name, phone))

# Remove a contact from the database
remove_contact = lambda id: conn.execute("DELETE FROM contacts WHERE id = ?;", (id,))

# Retrieve all contacts from the database
retrieve_all = lambda: conn.execute("SELECT * FROM contacts;").fetchall()

# Update an existing contact
update_contact = lambda id, name, phone: conn.execute("UPDATE contacts SET name = ?, phone = ? WHERE id = ?;", (name, phone, id))

# Loop to receive user input
while True:
    print("\nSelect an option:\n1. Add contact\n2. Remove contact\n3. Retrieve all contacts\n4. Update contact\n5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
        conn.commit()
    elif choice == "2":
        id = input("Enter contact ID to remove: ")
        remove_contact(id)
        conn.commit()
    elif choice == "3":
        contacts = retrieve_all()
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            for contact in contacts:
                print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}")
    elif choice == "4":
        id = input("Enter contact ID to update: ")
        name = input("Enter new name: ")
        phone = input("Enter new phone number: ")
        update_contact(id, name, phone)
        conn.commit()
    elif choice == "5":
        print("Exiting program...")
        conn.close()
        break
    else:
        print("Invalid choice. Try again.")
