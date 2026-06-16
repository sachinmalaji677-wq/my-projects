# def greet(name):
#     print(f"Hello{name}!")
#     print("Welcome to python")

# greet("Sachin")
# greet("Developer")
# greet("Future Engineer")

#grade calculator using funtion
# def calculate_grade(marks):
#     if marks >= 90:
#         return "Grade A-Excellent"
#     elif marks >= 70:
#         return "Grade B-Good"
#     elif marks >= 50:
#         return "Grade C-Pass"
#     else:
#         return "Failed - Work harder"
# marks = int(input("Enter your marks: "))
# grade = calculate_grade(marks)
# print(f"Your grade: {grade}")
# print 


#You wrote the logic--called it 3 times--3 different results--zero repeated code--ONE funtion INFINITE uses.
# def calculate_grade(marks):
#     if marks >= 90:
#         return "A Grade"
#     elif marks >= 70:
#         return "B Grade"
#     elif marks >= 50:
#         return "C Grade"
#     else:
#         return "Failed"
# grade = calculate_grade(95)
# print(grade)
# grade2 = calculate_grade(45)
# print(grade2)
# grade3 = calculate_grade(75)
# print(grade3)

#LISTS
#Lists = storing multiple values together
# students = ["Sachin", "Ravi","Priya"]
# marks = [95, 72, 45]
# print(students)
# print(marks)
# print(students[0]) #accessing first element
# print(marks[0]) #accessing first element

#Looping through lists
# students = ["Sachin", "Ravi","Priya"]
# marks = [95, 72, 45]
# for i in range(len(students)):
#     print(students[i],"->",marks[i])

# Student Grade Tracker

def calculate_grade(marks):
    if marks >= 90:
        return "A Grade"
    elif marks >= 70:
        return "B Grade"
    elif marks >= 50:
        return "C Grade"
    else:
        return "Failed"

students = []
marks_list = []

while True:
    print("\n1. Add Student")
    print("2. Show All Students")
    print("3. Show Passed Students")
    print("4. Show Highest Marks")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students.append(name)
        marks_list.append(marks)
        print(f"{name} added!")

    elif choice == "2":
        if len(students) == 0:
            print("No students yet!")
        else:
            for i in range(len(students)):
                grade = calculate_grade(marks_list[i])
                print(f"{students[i]} → {marks_list[i]} → {grade}")

    elif choice == "3":
        for i in range(len(students)):
            if marks_list[i] >= 50:
                print(f"{students[i]} passed!")

    elif choice == "4":
        if len(students) == 0:
            print("No students yet!")
        else:
            highest = max(marks_list)
            index = marks_list.index(highest)
            print(f"Highest: {students[index]} with {highest} marks!")

    elif choice == "5":
        print("Goodbye!")
        break





