students_marks={"lakhan":50,
            "chaman":45,
          "karan":40,
           "alice":49}
name=input("Enter the student's name: ")
if name in students_marks:
    print(f"{name}'s marks: {students_marks[name]}")
else:
    print("Student not found.")