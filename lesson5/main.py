class Student:
    def __init__(self, first_name, last_name, class_name):
        self.first_name = first_name
        self.last_name = last_name
        self.class_name = class_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Teacher:
    def __init__(self, first_name, last_name, subject):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject
        self.classes = []

    def add_class(self, class_name):
        self.classes.append(class_name)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Homeroom_Teacher:
    def __init__(self, first_name, last_name, class_name):
        self.first_name = first_name
        self.last_name = last_name
        self.class_name = class_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

students = []
teachers = []
homeroom_teachers = []

while True:
    print("\nAvailable commands: create, manage, end")
    command = input("Type a command: ")

    if command == "create":
        print("\nAvailable commands: student, teacher, homeroom teacher, end")
        command = input(("Type a command: "))
        if command == "student":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            class_name = input("Enter class name: ")

            new_student = Student(first_name, last_name, class_name)
            students.append(new_student)
            print("New Student Created")


        elif command == "teacher":

            first_name = input("Enter first name: ")

            last_name = input("Enter last name: ")

            subject = input("Enter subject taught: ")

            new_teacher = Teacher(first_name, last_name, subject)

            print("Enter classes (one per line). Leave blank to finish:")

            while True:

                class_name = input()

                if class_name == "":
                    break

                new_teacher.add_class(class_name)

            teachers.append(new_teacher)

            print("Teacher created.\n")

        elif command == "homeroom teacher":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            class_name = input("Enter class name: ")
            new_homeroom_teacher = Homeroom_Teacher(first_name, last_name, class_name)
            homeroom_teachers.append(new_homeroom_teacher)
            print("Homeroom teacher created. \n")

        elif command == "end":
            continue
        else:
            print("Invalid command")


    elif command == "manage":

        print("\nAvailable commands: class, student, teacher, homeroom teacher, end")

        command = input("Type a command: ")

        if command == "class":

            class_name = input("Enter class name: ")



            for student in students:
                print(f"Listing all students in class {class_name}:")

                if student.class_name == class_name:
                    print(student.full_name())

            for teacher in teachers:
                print(f"Listing all teachers in class {class_name}:")
                if class_name in teacher.classes:
                    print(teacher.full_name())

            for homeroom_teacher in homeroom_teachers:
                print(f"Listing all homeroom teachers in class {class_name}:")
                if homeroom_teacher.class_name == class_name:
                    print(homeroom_teacher.full_name())

        elif command == "student":
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")

            for student in students:
                if student.first_name == first_name and student.last_name == last_name:

                    print(f"\nStudent: {student.full_name()}")
                    print(f"Class: {student.class_name}")
                    print("Teachers for this class:")

                    for teacher in teachers:
                        if student.class_name in teacher.classes:
                            print(f"- {teacher.full_name()} ({teacher.subject})")

                    for homeroom_teacher in homeroom_teachers:
                        if student.class_name == homeroom_teacher.class_name:
                            print(f"Homeroom Teacher: {homeroom_teacher.full_name()}")
                    break

            else:
                print("Student not found.")

        elif command == "teacher":
            first_name = input("Enter teacher's first name: ")
            last_name = input("Enter teacher's last name: ")

            for teacher in teachers:
                if teacher.first_name == first_name and teacher.last_name == last_name:
                    print(f"\nTeacher: {teacher.full_name()}")
                    print(f"Subject: {teacher.subject}")
                    print("Classes taught:")
                    for class_name in teacher.classes:
                        print(f"- {class_name}")
                    break
            else:
                print("Teacher not found.")

        elif command == "homeroom teacher":
            first_name = input("Enter homeroom teacher's first name: ")
            last_name = input("Enter homeroom teacher's last name: ")

            for homeroom_teacher in homeroom_teachers:
                if homeroom_teacher.first_name == first_name and homeroom_teacher.last_name == last_name:
                    print(f"\nHomeroom Teacher: {homeroom_teacher.full_name()}")
                    print(f"Assigned to class: {homeroom_teacher.class_name}")
                    break
            else:
                print("Homeroom teacher not found.")

        elif command == "end":
            continue
        else:
            print("Invalid command")



    elif command == "end":
        print("Exiting program.")
        break


    else:
        print("Invalid command")



















