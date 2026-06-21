#Personal CLI Assistant
# Day 7 - Personal CLI Assistant
# import requests
# import json

# # ===== WEATHER FEATURE =====
# def get_weather(city):
#     api_key = "59761a3f0c36256a58da95cc5585b9ef"
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     try:
#         response = requests.get(url)
#         data = response.json()
#         if data["cod"] == 200:
#             temp = data["main"]["temp"]
#             humidity = data["main"]["humidity"]
#             condition = data["weather"][0]["description"]
#             print(f"\nWeather in {city}:")
#             print(f"Temperature : {temp}°C")
#             print(f"Humidity    : {humidity}%")
#             print(f"Condition   : {condition}")
#         else:
#             print("City not found!")
#     except:
#         print("No internet!")

# # ===== CONTACTS FEATURE =====
# def load_contacts():
#     try:
#         with open("contacts.txt", "r") as f:
#             return json.load(f)
#     except:
#         return []

# def save_contacts(contacts):
#     with open("contacts.txt", "w") as f:
#         json.dump(contacts, f)

# def add_contact(contacts):
#     name = input("Name: ")
#     phone = input("Phone: ")
#     contacts.append({"name": name, "phone": phone})
#     save_contacts(contacts)
#     print(f"{name} added!")

# def show_contacts(contacts):
#     if len(contacts) == 0:
#         print("No contacts!")
#     else:
#         for c in contacts:
#             print(f"{c['name']} → {c['phone']}")

# # ===== GRADE FEATURE =====
# def check_grade():
#     marks = int(input("Enter marks: "))
#     if marks >= 90:
#         print("A Grade!")
#     elif marks >= 70:
#         print("B Grade!")
#     elif marks >= 50:
#         print("C Grade!")
#     else:
#         print("Failed!")

# # ===== MAIN MENU =====
# contacts = load_contacts()

# while True:
#     print("\n===== CLI ASSISTANT =====")
#     print("1. Check Weather")
#     print("2. Add Contact")
#     print("3. Show Contacts")
#     print("4. Check Grade")
#     print("5. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         city = input("Enter city: ")
#         get_weather(city)
#     elif choice == "2":
#         add_contact(contacts)
#     elif choice == "3":
#         show_contacts(contacts)
#     elif choice == "4":
#         check_grade()
#     elif choice == "5":
#         print("Goodbye Sachin! Keep coding! 🔥")
#         break
#     else:
#         print("Invalid choice!")