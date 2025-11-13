from utils.file_handler import save_students, load_students
from utils.helpers import generate_student_summary

print("=== AI Programming Project ===")

students = load_students()

while True:
    name = input("Enter student name (or 'q' to quit): ")
    if name.lower() == 'q':
        break

    student_id = input("Enter student ID: ")
    favorite_ai_tool = input("Enter favorite AI tool: ")

    student = {
        "name": name,
        "student_id": student_id,
        "favorite_ai_tool": favorite_ai_tool
    }

    students.append(student)
    save_students(students)

    print("\nStudent added successfully!\n")

print("\n=== Students Summary ===")
print(generate_student_summary(students))

