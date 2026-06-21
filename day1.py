#How to push github
# git add .
# git commit -m "Day 3 - Dictionaries and Contact Book"
# git push
#______________________________________________________________________________________________


# name = input("Enter your name: ")
# age = input("Enter your age:")
# print("Hello",name)
# print("You are",age,"years old")
# print("You will become a Full Stack Developer")


#program 2
# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade A-Excellent")
# elif marks >= 70:
#     print("Grade B-Good")
# elif marks >= 50:
#     print("Grade C-Pass")
# else:
#     print("Failed - Work harder")


#program 3- Guessing game
# import random
# # generate secret number
# secret = random.randint(1, 10)
# tries = 0
# print("Guess the secret number between 1 and 100")

# #keep asking until corect guess
# while True:
#     guess = int(input("Enter your guess: "))
#     tries += 1

#     #check the guess
#     if guess < secret:
#         print("Too low! Try again.")
#     elif guess > secret:
#         print("Too high! Try again.")
#     else:
#         print(f"Correct! You guessed the number in {tries} tries!")
#         break



# Program 4 - ATM Machine

# balance = 10000

# print("Welcome to Sachin's ATM!")

# while True:
#     print("\n1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")
    
#     choice = input("Enter choice: ")
    
#     if choice == "1":
#         print(f"Your balance: ₹{balance}")
    
#     elif choice == "2":
#         amount = int(input("Enter deposit amount: "))
#         balance = balance + amount
#         print(f"₹{amount} deposited!")
#         print(f"New balance: ₹{balance}")
    
#     elif choice == "3":
#         amount = int(input("Enter withdraw amount: "))
#         if amount > balance:
#             print("Insufficient funds!")
#         else:
#             balance = balance - amount
#             print(f"₹{amount} withdrawn!")
#             print(f"Remaining balance: ₹{balance}")
    
#     elif choice == "4":
#         print("Thank you! Goodbye!")
#         break
    
#     else:
#         print("Invalid choice!")


