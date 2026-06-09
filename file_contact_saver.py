while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")

        file = open("contacts.txt", "a")
        file.write(name + " : " + phone + "\n")
        file.close()

        print("Contact Saved!")

    elif choice == "2":
        try:
            file = open("contacts.txt", "r")
            print("\nContacts:")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No contacts found!")

    elif choice == "3":
        print("Goodbye!")
        break
