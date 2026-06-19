import json
student = {}
lst = []
def add_students():
    name = input("Enter student name: ")
    id = int(input("Enter student ID: "))
    if name in student:
        print("Student already exists!")
    else:
        student[name] = {"id": id, "attendance": []}
        print("Student added successfully!")
def mark_attendance(name):
    if name not in student:
        print("Student not found!")
        return
    date = input("Enter date (DD-MM-YYYY): ")
    status = input("Student present? (Y/N): ").upper()
    if status == "Y":
        student[name]["attendance"].append({"date": date, "status": "P"})
    elif status == "N":
        student[name]["attendance"].append({"date": date, "status": "A"})
    else:
        print("Invalid input! Enter Y or N.")
def view_attendance(name):
    if name not in student:
        print("Student not found")
        return
    print("id: ", student[name]["id"])
    print("name: ", name)
    print("attendance: ")
    for record in student[name]["attendance"]:
        print(f"  Date: {record['date']}, Status: {record['status']}")
def attendance_percentage(name):
    if name not in student:
        print("Student not found")
        return

    presents = 0
    absents = 0

    for record in student[name]["attendance"]:
        if record["status"] == "P":
            presents += 1
        else:
            absents += 1

    total = presents + absents

    if total == 0:
        return 0

    percent = (presents / total) * 100
    return percent
while True:
    print("\n===== Attendance Management System =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Attendance Percentage")
    print("5. View All Students")
    print("6. Search Student")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            add_students()

        case 2:
            name = input("Enter student name: ")
            mark_attendance(name)

        case 3:
            name = input("Enter student name: ")
            view_attendance(name)

        case 4:
            name = input("Enter student name: ")
            print(f"Attendance Percentage: {attendance_percentage(name):.2f}%")

        case 5:
            print(student)
        case 6:
            name = input("Enter student name: ")
            if name in student:
                print("Student found:")
                print("ID:", student[name]["id"])
                print("Name:", name)
                print("Attendance Records:")
                for record in student[name]["attendance"]:
                    print(f"  Date: {record['date']}, Status: {record['status']}")
            else:
                print("Student not found.")
        case 7:
            print("Exiting...")
            break
        case _:
            print("Invalid choice!")
with open("students.json","w") as f:
    json.dump(student,f)
with open("students.json","r") as f:
    student = json.load(f)