# SearchUI.py

class SearchUI:
    def __init__(self, employee_data=None, manager_data=None):
        # Store data for different entities
        self.employee_data = employee_data if employee_data else []
        self.manager_data = manager_data if manager_data else []

    def menu(self):
        # Search menu for different entities
        choice = ""
        while choice != "0":
            print("\n--- Leitarvalmynd ---")
            print("1. Leita að starfsmanni (nafn)")
            print("2. Leita að starfsmanni með kennitölu")
            print("3. Leita að yfirmanni (nafn)")
            print("4. Leita að yfirmanni með kennitölu")
            print("0. Til baka")

            choice = input("Veldu aðgerð: ").strip()

            if choice == "1":
                self.search_employee_by_name()
            elif choice == "2":
                self.search_employee_by_kennitala()
            elif choice == "3":
                self.search_manager_by_name()
            elif choice == "4":
                self.search_manager_by_kennitala()
            elif choice == "0":
                print("Til baka í fyrri valmynd...")
            else:
                print("Rangur innsláttur, reyndu aftur.")

    def search_employee_by_name(self):
        # Search for an employee by name
        name = input("\nSláðu inn nafn starfsmanns til að leita: ").strip()
        results = [emp for emp in self.employee_data if name.lower() in emp.name.lower()]

        if results:
            print("\n--- Niðurstöður leitar ---")
            for emp in results:
                print(emp)
                print('-' * 50)  # Divider line for readability
        else:
            print("Enginn starfsmaður fannst með þetta nafn.")

    def search_employee_by_kennitala(self):
        # Search for an employee by kennitala (ID number)
        kennitala = input("\nSláðu inn kennitölu starfsmanns til að leita: ").strip()
        results = [emp for emp in self.employee_data if kennitala == emp.kennitala]

        if results:
            print("\n--- Niðurstöður leitar ---")
            for emp in results:
                print(emp)
                print('-' * 50)  # Divider line for readability
        else:
            print("Enginn starfsmaður fannst með þessa kennitölu.")

    def search_manager_by_name(self):
        # Search for a manager by name
        name = input("\nSláðu inn nafn yfirmanns til að leita: ").strip()
        results = [mgr for mgr in self.manager_data if name.lower() in mgr.name.lower()]

        if results:
            print("\n--- Niðurstöður leitar ---")
            for mgr in results:
                print(mgr)
                print('-' * 50)  # Divider line for readability
        else:
            print("Enginn yfirmaður fannst með þetta nafn.")

    def search_manager_by_kennitala(self):
        # Search for a manager by kennitala (ID number)
        kennitala = input("\nSláðu inn kennitölu yfirmanns til að leita: ").strip()
        results = [mgr for mgr in self.manager_data if kennitala == mgr.kennitala]

        if results:
            print("\n--- Niðurstöður leitar ---")
            for mgr in results:
                print(mgr)
                print('-' * 50)  # Divider line for readability
        else:
            print("Enginn yfirmaður fannst með þessa kennitölu.")
