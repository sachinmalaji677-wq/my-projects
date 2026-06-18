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

contacts = []#initialize an empty list to store contacts

while True:#infinite loop to keep the program running until the user chooses to exit
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
        print(f"\nTotal Contacts: {len(contacts)}")
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
        found = False#it is used to track whether a contact with the given name was found in the contacts list. Initially, it is set to False, indicating that no contact has been found yet. If a contact with the matching name is found during the search, found is set to True. After the search loop, if found remains False, it means that no contact with the specified name was found, and a message is printed to inform the user. 
        for contact in contacts:#it iterates through each contact in the contacts list to check if the name matches the search query. If a match is found, it prints the contact's details and sets found to True.
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

    