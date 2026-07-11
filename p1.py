#Develop a python program that demonstrates the use of required, keyword, default, and variable-length arguments through functions.

def required(name, rollno, grade):
    print(f"Student Name: {name}, Roll Number: {rollno}, Grade: {grade}")

def default(name, rollno, grade="A"):
    name= input("Enter name of the student: ")
    rollno= input("Enter roll number of the student: ")
    print(f"Student Name: {name}, Roll Number: {rollno}, Grade: {grade}")

def keyword(name, rollno, grade):
    print(f"Student Name: {name}, Roll Number: {rollno}, Grade: {grade}")

def variable_length(name, rollno, grade, *subjects):
    print(f"Student Name: {name}, Roll Number: {rollno}, Grade: {grade}")
    print("Favourite subjects: ",  subjects)

required("dfgd", "55", "b")
default("Alice", "456")
keyword(name="Bob", rollno="789", grade="C")
variable_length("Eve", "101", "A", "Math", "Science", "History")