students = ["Satyam", "Riya", "Siya", "Ankit"]

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Student Name: ")
        students.append(name)
        print("Student Added!")

    elif choice == "2":
        print("\nStudents List:")
        for s in students:
            print("-", s)

    elif choice == "3":
        break
