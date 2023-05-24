class Employee:
    def __init__(self, emp_id, name, specialties, improvement_areas):
        self.emp_id = emp_id
        self.name = name
        self.specialties = specialties
        self.improvement_areas = improvement_areas
        self.performance_score = 0

    def evaluate_performance(self, score):
        self.performance_score = score


class PerformanceEvaluationSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, specialties, improvement_areas):
        employee = Employee(emp_id, name, specialties, improvement_areas)
        self.employees.append(employee)
        print("Employee added successfully.")

    def evaluate_employee_performance(self, emp_id, score):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.evaluate_performance(score)
                print("Employee performance evaluated successfully.")
                return
        print("Employee not found.")

    def view_employee_performance(self):
        if not self.employees:
            print("No employees available.")
        else:
            print("Employee Performance:")
            for employee in self.employees:
                print(f"Employee ID: {employee.emp_id}")
                print(f"Name: {employee.name}")
                print(f"Specialties: {', '.join(employee.specialties)}")
                print(f"Areas for Improvement: {', '.join(employee.improvement_areas)}")
                print(f"Performance Score: {employee.performance_score}")
                print("-------------------------")


def menu():
    evaluation_system = PerformanceEvaluationSystem()
    while True:
        print("\n--- Employee Performance Evaluation System ---")
        print("1. Add an employee")
        print("2. Evaluate employee performance")
        print("3. View employee performance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            specialties = input("Enter employee specialties (separated by commas): ").split(",")
            improvement_areas = input("Enter areas for improvement (separated by commas): ").split(",")
            evaluation_system.add_employee(emp_id, name, specialties, improvement_areas)

        elif choice == "2":
            emp_id = input("Enter employee ID to evaluate performance: ")
            score = float(input("Enter performance score: "))
            evaluation_system.evaluate_employee_performance(emp_id, score)

        elif choice == "3":
            evaluation_system.view_employee_performance()

        elif choice == "4":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
menu()