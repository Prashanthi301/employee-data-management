from employee_manager import add_employee, list_employees, get_employee, update_skills

def menu():
    while True:
        print("\nEmployee Data Management System")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. List All Employees")
        print("4. Update Employee Skills")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            age = int(input("Age: ").strip())
            dept = input("Department: ").strip()
            skills = [s.strip() for s in input("Skills (comma separated): ").split(",") if s.strip()]
            print(add_employee(name, age, dept, skills))

        elif choice == "2":
            name = input("Enter employee name: ").strip()
            emp = get_employee(name)
            print(emp if emp else "Not found")

        elif choice == "3":
            employees = list_employees()
            if not employees:
                print("No employees found.")
            for e in employees:
                print(e)

        elif choice == "4":
            name = input("Name: ").strip()
            skill = input("New Skill: ").strip()
            print(update_skills(name, skill))

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
