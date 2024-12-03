# StartupUI.py
from ListLayoutUI import ListLayoutUI
from data_parser import parse_employees_from_file, parse_managers_from_file

class StartupUI:
    def __init__(self):
        try:
            self.employee_data = parse_employees_from_file('starfsmenn.txt')
            self.manager_data = parse_managers_from_file('yfirmenn.txt')
        except FileNotFoundError as e:
            print(f"Error: {e}")
            self.employee_data = []
            self.manager_data = []

    def display_log_in_menu(self):
        choice = ""
        while choice != "0":
            print("\n---Velkominn í NaN Airlines---")
            print("1. Starfsmaður ")
            print("2. Yfirmaður ")
            print("3. Stjórnandi ")
            print("0. Hætta ")

            choice = input("Vinsamlegast skráðu þig inn: ")

            if choice == "1":
                list_layout_ui = ListLayoutUI(employee_data=self.employee_data)
                list_layout_ui.menu(user_role="employee")
            elif choice == "2":
                list_layout_ui = ListLayoutUI(employee_data=self.employee_data, manager_data=self.manager_data)
                list_layout_ui.menu(user_role="manager")
            elif choice == "3":
                list_layout_ui = ListLayoutUI(employee_data=self.employee_data, manager_data=self.manager_data)
                list_layout_ui.menu(user_role="admin")
            elif choice == "0":
                print("Þú ert að hætta ")
            else:
                print("Rangur innsláttur, veldu rétt innsláttur.")

if __name__ == "__main__":
    startup_ui = StartupUI()
    startup_ui.display_log_in_menu()
