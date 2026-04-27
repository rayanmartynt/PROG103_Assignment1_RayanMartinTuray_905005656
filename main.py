#Attendance status
ATTENDANCE_STATUS_OPTIONS = {
    "1": "Present",
    "2": "Absent",
    "3": "Late"
}
MENU_EXIT = "3"

#New attendance function
def add_attendance(records):
    print("\n___Add new Attendance Record___")

    #Capturing data from the user
    name = input("Enter the name of the Student:")
    while name == "":
        print("This field is required. Please enter a valid name.")
        name = input("Enter the name of the Student:")

    date = input("Date (DD/MM/YYYY):")
    while date == "":
        print("This field is required. Please enter a valid date.")
        date = input("Date (DD/MM/YYYY):")


    print("\n Status options")
    print("1. Present")
    print("2. Absent")
    print("3. Late")

    choice = int(input("Enter choice (1/2/3):"))
    while choice == "":
        print("This field is required. Please enter a valid choice.")
        choice = int(input("Enter choice (1/2/3):"))

    if choice == 1:
        status = ATTENDANCE_STATUS_OPTIONS["1"]
    elif choice == 2:
        status = ATTENDANCE_STATUS_OPTIONS["2"]
    elif choice == 3:
        status = ATTENDANCE_STATUS_OPTIONS["3"]
    else:
        print("Invalid choice. Please enter a valid choice.")
        return

    records.append({
        "name": name,
        "date": date,
        "status":status
    })

    print(f"Attendance record added: {name} - {date} - {status}")


# Calling the above function add_attendance(Initial call to test my code)
# add_attendance()

"Function 2: Process all records and display summary report."
def generate_attendance_report(records):
    if records == []:
        print("No attendance records found.")
        return

    # This is an empty dictionary to store student's stats
    student_stats = {}

    for record in records:
        name = record["name"],
        # date = record["date"],
        status = record["status"]

        if name not in student_stats:
            student_stats[name] = {"Present": 0, "Absent": 0, "Late": 0}
        student_stats[name][status] += 1

    # Printing individual student report
    print("\n ====== ATTENDANCE SUMMARY REPORT ======")
    for name, stats in student_stats.items():
        total = stats["Present"] + stats["Absent"] + stats["Late"]
        attendance_percentage = (stats["Present"] / total) * 100 if total > 0 else 0

        print(f"\n Student: {name}")
        print(f" Present: {stats['Present']} | Absent: {stats['Absent']} | Late: {stats['Late']}")
        print(f"Attendance Percentage: {attendance_percentage:.1f}%")

    # Calculating the total number of student present, late, and absent
    total_present = sum(stats["Present"] for stats in student_stats.values())
    total_absent = sum(stats["Absent"] for stats in student_stats.values())
    total_late = sum(stats["Late"] for stats in student_stats.values())
    total_records = total_present + total_absent + total_late
    print("====== CLASS TOTAL: ======")
    print(f"Total Present: {total_present}")
    print(f"Total Absent: {total_absent}")
    print(f"Total Late: {total_late}")
    print(f"Total Records: {total_records}")

    #Calculating the percentage of attendance
    if total_records > 0:
        class_attendance = (total_present / total_records) * 100
        print(f"Overall attendance: {class_attendance:.1f}%")


def main():
    records = []

    #Using while loop to iterate menu choices
    while True:
        print("\n ====== ATTENDANCE TRACKING SYSTEM MENU ======")
        print("1. Add new Attendance")
        print("2. Generate Attendance Summary Report")
        print("3. Exit")

        # Using try-catch method to handle data type error (choice can only be an integer)
        try:
            menu_choices = int(input("Enter your choice:"))
            if menu_choices == 1:
                add_attendance(records)
            elif menu_choices == 2:
                generate_attendance_report(records)
            elif menu_choices == 3:
                print("Exiting program.")
                break
        except ValueError:
                print("Invalid choice. Please enter a valid choice.")


if __name__ == "__main__":
    main()