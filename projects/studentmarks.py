students = {
    "student1": {
        "name": "A",
        "age": 20,
        "dsa_marks": 85,
        "python_marks": 60
    },
    "student2": {
        "name": "B",
        "age": 19,
        "dsa_marks": 80,
        "python_marks": 70
    },
    "student3": {
        "name": "C",
        "age": 20,
        "dsa_marks": 95,
        "python_marks": 75
    },
    "student4": {
        "name": "D",
        "age": 21,
        "dsa_marks": 65,
        "python_marks": 90
    },
    "student5": {
        "name": "E",
        "age": 20,
        "dsa_marks": 75,
        "python_marks": 50
    }
}
# while True: means “keep running forever until I tell you to stop.”
# In this case, it keeps asking for a student name until the user gives a valid one.
while True:
    # asks for the details
    print("Enter the required details.")
    # takes the name input from user
    name = input("name: ")

    # found = false is a flag
    # assumes that student is not found at the start
    found = False
    # Go through each student's key and information one by one.
    # for example, key is "student1"
    # # info is name, age, python_marks, dsa_marks
    for key, info in students.items():
        # Check if the entered name matches the student's name
        if name == info["name"]:
            # prints the students info.
            print("Name:", info["name"])
            print("Age:", info["age"])
            print("DSA Marks:", info["dsa_marks"])
            print("Python Marks:", info["python_marks"])
            # changes found to true if the student is found.
            found = True
            # stops checking for student details once the student is found.
            break
            # exits the for loop.
    # Using if found - “I found the student, so I can exit now.”
    if found:
        # stop asking again once a valid student is found.
        break
        # exits the while True loop.
    else:
        # asks the user to enter valid name
        print("Enter valid details.")

