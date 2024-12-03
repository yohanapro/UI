# ListLayoutUI.py
from Employee import Employee
from Manager import Manager

class ListLayoutUI:
    def __init__(self, employee_data=None, manager_data=None):
        # Store data for different entities
        self.employee_data = employee_data if employee_data else []
        self.manager_data = manager_data if manager_data else []

    def menu(self, user_role):
        choice = ""
        while choice != "0":
            if user_role == "employee":
                print("\n--- Starfsmaður Valmynd (Employee Menu) ---")
                print("1. Skoða lista yfir starfsmenn (View Employee List)")
                print("2. Sía starfsmenn eftir staðsetningu (Filter Employees by Location)")
                print("0. Til baka (Back)")
            elif user_role == "manager" or user_role == "admin":
                print("\n--- Yfirmaður Valmynd (Manager Menu) ---")
                print("1. Skoða lista yfir starfsmenn (View Employee List)")
                print("2. Skrá nýjan starfsmann (Add New Employee)")
                print("3. Breyta starfsmanni (Edit Employee)")
                print("4. Eyða starfsmanni (Delete Employee)")
                print("5. Sía starfsmenn eftir staðsetningu (Filter Employees by Location)")
                print("0. Til baka (Back)")

            choice = input("Veldu aðgerð: ").strip()

            if user_role == "employee":
                if choice == "1":
                    self.view_employee_list()
                elif choice == "2":
                    self.filter_employees_by_location()
                elif choice == "0":
                    print("Til baka í aðalvalmynd...")
                else:
                    print("Rangur innsláttur, reyndu aftur.")

            elif user_role == "manager" or user_role == "admin":
                if choice == "1":
                    self.view_employee_list()
                elif choice == "2":
                    self.add_new_employee()
                elif choice == "3":
                    self.edit_employee()
                elif choice == "4":
                    self.delete_employee()
                elif choice == "5":
                    self.filter_employees_by_location()
                elif choice == "0":
                    print("Til baka í aðalvalmynd...")
                else:
                    print("Rangur innsláttur, reyndu aftur.")

    def view_employee_list(self):
        print("\n--- Listi yfir starfsmenn (Employee List) ---")
        for emp in self.employee_data:
            print(emp)
            print('-' * 50)  # Divider line for readability

    def filter_employees_by_location(self):
        location = input("\nSláðu inn staðsetningu til að sía starfsmenn (Enter Location to Filter Employees): ").strip()
        filtered_employees = [emp for emp in self.employee_data if location.lower() in emp.address.lower()]

        if filtered_employees:
            print("\n--- Starfsmenn á Staðsetningu ---")
            for emp in filtered_employees:
                print(emp)
                print('-' * 50)  # Divider line for readability
        else:
            print(f"Engir starfsmenn fundust á staðsetningunni: {location}")

    def add_new_employee(self):
        print("\n--- Skrá nýjan starfsmann (Add New Employee) ---")
        name = input("Nafn: ")
        kennitala = input("Kennitala: ")
        email = input("Netfang: ")
        address = input("Heimilisfang: ")
        phone = input("Símanúmer: ")
        gsm = input("GSM: ")

        new_employee = Employee(name, kennitala, email, address, phone, gsm)
        self.employee_data.append(new_employee)
        print(f"Starfsmaður '{name}' hefur verið skráður.")

    def edit_employee(self):
        name = input("Sláðu inn nafn starfsmanns til að breyta (Enter Employee Name to Edit): ").strip()
        for emp in self.employee_data:
            if emp.name.lower() == name.lower():
                emp.name = input(f"Nafn ({emp.name}): ") or emp.name
                emp.kennitala = input(f"Kennitala ({emp.kennitala}): ") or emp.kennitala
                emp.email = input(f"Netfang ({emp.email}): ") or emp.email
                emp.address = input(f"Heimilisfang ({emp.address}): ") or emp.address
                emp.phone = input(f"Símanúmer ({emp.phone}): ") or emp.phone
                emp.gsm = input(f"GSM ({emp.gsm}): ") or emp.gsm
                print(f"Upplýsingar um '{emp.name}' hafa verið uppfærðar.")
                return
        print("Starfsmaður fannst ekki.")

    def delete_employee(self):
        name = input("Sláðu inn nafn starfsmanns til að eyða (Enter Employee Name to Delete): ").strip()
        for emp in self.employee_data:
            if emp.name.lower() == name.lower():
                self.employee_data.remove(emp)
                print(f"Starfsmanni '{name}' hefur verið eytt.")
                return
        print("Starfsmaður fannst ekki.")
