# #OOPs(classes and objects)
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Marks: {self.marks}")
#     def get_grade(self):
#         if self.marks >= 90:
#             return "A Grade"
#         elif self.marks >= 70:
#             return "B Grade"
#         elif self.marks >= 50:
#             return "C Grade"
#         else:
#             return "Failed"

# #creating objects of the Student class
# student1 = Student("Alice", 95)
# student2 = Student("Bob", 72)

# student1.show_details()
# student2.show_details()

# print(student1.get_grade())  # Output: B Grade
# print(student2.get_grade())  # Output: C Grade



# Bank Account System

class BankAccount:
    def __init__(self, owner, account_no, balance):
        self.owner = owner
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited!")
        print(f"New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn!")
            print(f"Remaining: ₹{self.balance}")

    def show_details(self):
        print(f"Owner: {self.owner}")
        print(f"Account No: {self.account_no}")
        print(f"Balance: ₹{self.balance}")


# Create accounts
account1 = BankAccount("Sachin", "SB001", 10000)
account2 = BankAccount("Ravi", "SB002", 5000)

# Test
account1.show_details()
account1.deposit(2000)
account1.withdraw(3000)
account1.withdraw(15000)

print("---")
account2.show_details()