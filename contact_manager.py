contacts = {
    "Satyam": "620xxxxxxx",
    "Riya": "967xxxxxxx",
    "Siya": "983xxxxxxx",
    "Ankit": "889xxxxxxx"
}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Contact Saved!")

    elif choice == "2":
        print("\nContacts:")
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        print("Goodbye!")
        break
