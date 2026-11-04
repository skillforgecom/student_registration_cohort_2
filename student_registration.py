students = []
student_names = []
unique_students = set()

for i in range(5):
    student_name = input(f"Enter student {i+1}: ").strip().capitalize()
    student_age = int(input(f"Enter student {i+1}'s age: ").strip())
    fav_sub = input(f"Enter student {i+1}'s favourite subject: ").strip().capitalize()
    student = (student_name,student_age,fav_sub) #model
    students.append(student)
    student_names.append(student_name)

print(f"Registered students: {student_names}")

#Getting student set
# for i in range(len(students)):
#     unique_students.add(students[i][0])

for i in range(len(student_names)):
    unique_students.add(student_names[i])

print(f"Unique Students: {unique_students}")
print(f"Total Unique Students: {len(unique_students)}")

for i in range(len(students)):
    print(f"student {i+1} = {students[i]}")

#searching for a student
student_to_search = input("Enter name of student to search: ").strip().capitalize()
if student_to_search in student_names:
    print(f"{student_to_search} is registered in class!")
