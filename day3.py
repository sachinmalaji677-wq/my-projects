#Dictionaries= It stores data as key-value pairs where each key is unique and used to access its value.
#p1
# student = {"name": "John", "age": 25, "city": "New York"}
# print(student["name"])  # Output: John
# print(student["age"])   # Output: 25
# print(student["city"])  # Output: New York
# student["age"] = 26 # Update the age
# print(student["age"])   # Output: 26
# student["country"] = "USA" # Add a new key-value pair
# print(student["country"])  # Output: USA


# Contact Book App

contacts = []

while True:
    print("\n1. Add Contact")
    print("2. Show All Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }
        contacts.append(contact)
        print(f"{name} added!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts yet!")
        else:
            for contact in contacts:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print("---")


    elif choice == "3":
        search = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact["name"] == search:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                found = True
        if not found:
            print("Contact not found!")

    elif choice == "4":
        print("Goodbye!")
        break