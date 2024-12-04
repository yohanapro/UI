# ListLayoutUI.py
from Employee import Employee
from Manager import Manager
from SearchUI import SearchUI

class ListLayoutUI:
	def __init__(self, employee_data=None, manager_data=None):
		# Store data for different entities
		self.employee_data = employee_data if employee_data else []
		self.manager_data = manager_data if manager_data else []

	def menu(self, user_role):
		choice = ""
		while choice != "0":
			if user_role == "employee":
				print("\n--- Starfsmaður Valmynd ---")
				print("1. Skoða lista yfir starfsmenn")
				print("2. Sía starfsmenn eftir staðsetningu")
				print("3. Skoða fasteigna lista")
				print("4. Sía fasteignir eftir staðsetningu")
				print("5. Leita í gagnagrunni")
				print("0. Til baka")
			elif user_role == "manager" or user_role == "admin":
				print("\n--- Yfirmaður Valmynd ---")
				print("1. Skoða lista yfir starfsmenn")
				print("2. Skrá nýjan starfsmann")
				print("3. Eyða starfsmann úr starfmanna lista")
				print("4. Sía starfsmenn eftir staðsetningu")
				print("5. Skoða yfirmanna lista")
				print("6. Eyða yfirmanni úr yfirmanna lista")
				print("7. Skoða fasteigna lista")
				print("8. Sía fasteignir eftir staðsetningu")
				print("9. Eyða fasteign úr fasteigna lista")
				print("10. Leita í gagnagrunni")
				print("0. Til baka")

			choice = input("Veldu aðgerð: ").strip()

			if user_role == "employee":
				if choice == "1":
					self.view_employee_list()
				elif choice == "2":
					self.filter_employees_by_location()
				elif choice == "3":
					self.view_property_list()
				elif choice == "4":
					self.filter_properties_by_location()
				elif choice == "5":
					self.search_database()
				
				elif choice == "0":
					print("Til baka...")
				else:
					print("Rangur innsláttur, reyndu aftur.")

			elif user_role == "manager" or user_role == "admin":
				if choice == "1":
					self.view_employee_list()
				elif choice == "2":
					self.add_new_employee()
				elif choice == "3":
					self.remove_employee()
				elif choice == "4":
					self.filter_employees_by_location()
				elif choice == "5":
					self.view_managers_list()
				elif choice == "6":
					self.search_database()
				elif choice == "7":
					self.view_property_list()
				elif choice == "8":
					self.filter_properties_by_location()
				elif choice == "9":
					self.remove_property()
				elif choice == "10":
					self.search_database()
				elif choice == "0":
					print("Til baka...")
				else:
					print("Rangur innsláttur, reyndu aftur.")

	def view_employee_list(self):
		# Display the list of employees
		print("\n--- Starfsmanna Lista ---")
		for emp in self.employee_data:
			print(emp)
			print('-' * 50)  # Divider line for readability

	def filter_employees_by_location(self):
		# Filter and display employees by location
		location = input("\nSláðu inn staðsetningu til að sía: ").strip()
		filtered_employees = [emp for emp in self.employee_data if location.lower() in emp.address.lower()]

		if filtered_employees:
			print("\n--- Starfsmenn á staðsetningu ---")
			for emp in filtered_employees:
				print(emp)
				print('-' * 50)  # Divider line for readability
		else:
			print(f"Engir starfsmenn fundust á staðsetningunni: {location}")

	def view_managers_by_location(self):
		# Filter and display managers by location
		location = input("\nSláðu inn staðsetningu til að skoða yfirmenn: ").strip()
		filtered_managers = [mgr for mgr in self.manager_data if location.lower() in mgr.location.lower()]

		if filtered_managers:
			print("\n--- Yfirmenn á staðsetningu ---")
			for mgr in filtered_managers:
				print(mgr)
				print('-' * 50)  # Divider line for readability
		else:
			print(f"Engir yfirmenn fundust á staðsetningunni: {location}")

	def add_new_employee(self):
		# Add a new employee
		print("\n--- Skrá nýjan starfsmann ---")
		name = input("Nafn: ")
		kennitala = input("Kennitala: ")
		email = input("Netfang: ")
		address = input("Heimilisfang: ")
		landline = input("Sími: ")
		gsm = input("GSM: ")

		# Create a new Employee object
		new_employee = Employee(name, kennitala, email, address, landline, gsm)
		self.employee_data.append(new_employee)

		# Save the new employee to the file
		with open('starfsmenn.txt', 'a', encoding='utf-8') as file:
			file.write(f"Nafn       : {new_employee.name}\n")
			file.write(f"Kennitala  : {new_employee.kennitala}\n")
			file.write(f"e-mail     : {new_employee.email}\n")
			file.write(f"Heim.      : {new_employee.address}\n")
			file.write(f"Sími       : {new_employee.landline}\n")
			file.write(f"GSM        : {new_employee.gsm}\n")
			file.write("\n")  # Add an empty line to separate employees

		print(f"Starfsmaður '{name}' hefur verið skráður.")

	def edit_employee(self):
		# Edit an existing employee
		name = input("Sláðu inn nafn starfsmanns til að breyta: ").strip()
		for emp in self.employee_data:
			if emp.name.lower() == name.lower():
				emp.name = input(f"Nafn ({emp.name}): ") or emp.name
				emp.kennitala = input(f"Kennitala ({emp.kennitala}): ") or emp.kennitala
				emp.email = input(f"Netfang ({emp.email}): ") or emp.email
				emp.address = input(f"Heimilisfang ({emp.address}): ") or emp.address
				emp.landline = input(f"Sími  ({emp.landline}): ") or emp.landline
				emp.gsm = input(f"GSM ({emp.gsm}): ") or emp.gsm
				print(f"Upplýsingar um '{emp.name}' hafa verið uppfærðar.")
				return
		print("Starfsmaður fannst ekki.")

	def remove_employee(self):
		# Remove an existing employee
		kennitala = input("Sláðu inn kennitölu starfsmanns til að eyða: ").strip()
		list_of_employees = self.employee_data.copy()
		for emp in list_of_employees:
			if emp.kennitala == kennitala:
				self.employee_data.remove(emp)

	def view_property_list(self):
		# Display the list of properties
		print("\n--- Fasteigna Lista ---")
		for prop in self.property_data:
			print(prop)
			print('-' * 50)

	def filter_properties_by_location(self):
		# Filter and display properties by location
		location = input("\nSláðu inn staðsetningu til að sía: ").strip()
		filtered_properties = [prop for prop in self.property_data if location.lower() in prop.location.lower()]

		if filtered_properties:
			print("\n--- Fasteignir á staðsetningu ---")
			for prop in filtered_properties:
				print(prop)
				print('-' * 50)
		else:
			print(f"Engar fasteignir fundust á staðsetningunni: {location}")

	def view_managers_list(self):
		# Display the list of managers
		print("\n--- Yfirmanna Lista ---")
		for mgr in self.manager_data:
			print(mgr)
			print('-' * 50)

	def add_new_manager(self):
		# Add a new manager
		print("\n--- Skrá nýjan yfirmann ---")
		name = input("Nafn: ")
		kennitala = input("Kennitala: ")
		email = input("Netfang: ")
		location = input("Staðsetning: ")
		landline = input("Sími: ")
		gsm = input("GSM: ")

		# Create a new Manager object
		new_manager = Manager(name, kennitala, email, location, landline, gsm)
		self.manager_data.append(new_manager)

		# Save the new manager to the file
		with open('yfirmenn.txt', 'a', encoding='utf-8') as file:
			file.write(f"Nafn       : {new_manager.name}\n")
			file.write(f"Kennitala  : {new_manager.kennitala}\n")
			file.write(f"e-mail     : {new_manager.email}\n")
			file.write(f"Staðsetning : {new_manager.location}\n")
			file.write(f"Sími       : {new_manager.landline}\n")
			file.write(f"GSM        : {new_manager.gsm}\n")
			file.write("\n")

		print(f"Yfirmaður '{name}' hefur verið skráður.")

	def edit_manager(self):
		# Edit an existing manager
		name = input("Sláðu inn nafn yfirmanns til að breyta: ").strip()
		for mgr in self.manager_data:
			if mgr.name.lower() == name.lower():
				mgr.name = input(f"Nafn ({mgr.name}): ") or mgr.name
				mgr.kennitala = input(f"Kennitala ({mgr.kennitala}): ") or mgr.kennitala
				mgr.email = input(f"Netfang ({mgr.email}): ") or mgr.email
				mgr.location = input(f"Staðsetning ({mgr.location}): ") or mgr.location
				mgr.landline = input(f"Sími  ({mgr.landline}): ") or mgr.landline
				mgr.gsm = input(f"GSM ({mgr.gsm}): ") or mgr.gsm
				print(f"Upplýsingar um '{mgr.name}' hafa verið uppfærðar.")
				return
		print("Yfirmaður fannst ekki.")

	def remove_manager(self):
		# Remove an existing manager
		kennitala = input("Sláðu inn kennitölu yfirmanns til að eyða: ").strip()


	def search_database(self):
		# Use SearchUI to perform searches in the database
		search_ui = SearchUI(employee_data=self.employee_data, manager_data=self.manager_data)
		search_ui.menu()
