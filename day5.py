#File Handlig and Error Handling
#writing to a file
# file=open("test.txt","w")
# file.write("Hello Sachin")
# file.write("\nYou are a developer")
# file.close()

# print("File saved")
# #Reading from a file
# file=open("test.txt","r")
# content=file.read()
# file.close()
# print(content)

# #with(professional way)--->automatially closess ,file when done ,bo need to write file.close().
# file=open("test.txt","w")
# file.write("Hello Sachin")
# file.write("\nYou are a developer")
# file.close()

# print("File saved")
# #Reading from a file
# with open("test.txt","r") as file:
#     content=file.read()
# print(content)

#Error Handling
# try:
#     age=int(input("Enter your age:"))
#     print(f"your age is {age}")
# except:
#     print("Please enter a valid number")



# Contact Book with File Saving
# import json

# def save_contacts(contacts):
#     with open("contacts.txt", "w") as file:
#         json.dump(contacts, file)
#     print("Contacts saved!")

# def load_contacts():
#     try:
#         with open("contacts.txt", "r") as file:
#             return json.load(file)
#     except:
#         return []

# contacts = load_contacts()

# while True:
#     print("\n1. Add Contact")
#     print("2. Show All Contacts")
#     print("3. Search Contact")
#     print("4. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         name = input("Enter name: ")
#         phone = input("Enter phone: ")
#         contact = {
#             "name": name,
#             "phone": phone
#         }
#         contacts.append(contact)
#         save_contacts(contacts)

#     elif choice == "2":
#         if len(contacts) == 0:
#             print("No contacts yet!")
#         else:
#             for contact in contacts:
#                 print(f"Name: {contact['name']}")
#                 print(f"Phone: {contact['phone']}")
#                 print("---")

#     elif choice == "3":
#         search = input("Enter name: ")
#         found = False
#         for contact in contacts:
#             if contact["name"] == search:
#                 print(f"Name: {contact['name']}")
#                 print(f"Phone: {contact['phone']}")
#                 found = True
#         if not found:
#             print("Not found!")

#     elif choice == "4":
#         print("Goodbye!")
#         break