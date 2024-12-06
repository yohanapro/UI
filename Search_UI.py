from Logic.logic_api import LogicAPI

class SearchUI:
	def __init__(self, employees, orders, locations, properties, reports):
		"""Initialize the SearchUI with data and LogicAPI."""
		self.employees = employees
		self.orders = orders
		self.locations = locations
		self.properties = properties
		self.reports = reports
		self.logic_api = LogicAPI()  # Initialize LogicAPI instance

	def employee(self, display=True):
		"""Search for employees by a given query."""
		search = input("Leita að starfsmanni: ").strip()
		results = self.logic_api.search_employee(search, self.employees)
		if not results:
			if display:
				print("Enginn starfsmaður fannst.")
			return []  # Return an empty list if no results

		if display:
			print("Leitarniðurstöður:")
			for employee in results:
				print(f"Kennitala: {employee['ssn']}, Nafn: {employee['name']}, Netfang: {employee['email']}, "
					  f"Sími: {employee['landline']}, GSM: {employee['gsm']}, Heimilisfang: {employee['address']}")
		return results

	def order(self, display=True):
		"""Search for orders by a given query."""
		search = input("Leita að verkbeiðni: ").strip()
		results = self.logic_api.search_order(search, self.orders)
		if not results:
			if display:
				print("Engin verkbeiðnisnúmer fundust.")
			return []  # Return an empty list if no results

		if display:
			print("Leitarniðurstöður:")
			for order in results:
				print(f"Verkbeiðnisnúmer: {order['order_number']}, Fasteignarnúmer: {order['property_id']}, "
					  f"Starfsmaður: {order['employee_id']}, Dagsetning: {order['date']}, Verð: {order['price']}")
		return results

	def location(self, display=True):
		"""Search for locations by a given query."""
		search = input("Leita að staðsetningu: ").strip()
		results = self.logic_api.search_location(search, self.locations)
		if not results:
			if display:
				print("Engin staðsetning fannst.")
			return []  # Return an empty list if no results

		if display:
			print("Leitarniðurstöður:")
			for location in results:
				print(f"Staðsetning: {location['name']}, Heimilisfang: {location['address']}, "
					  f"Sími: {location['landline']}, GSM: {location['gsm']}")
		return results

	def property(self, display=True):
		"""Search for properties by a given query."""
		search = input("Leita að fasteign: ").strip()
		results = self.logic_api.search_property(search, self.properties)
		if not results:
			if display:
				print("Engin fasteign fannst.")
			return []  # Return an empty list if no results

		if display:
			print("Leitarniðurstöður:")
			for property in results:
				print(f"Fasteignarnúmer: {property['property_id']}, Heimilisfang: {property['address']}, "
					  f"Staðsetning: {property['location']}, Stærð: {property['size']} fermetrar, "
					  f"Herbergi: {property['rooms']}, Upplýsingar: {property['description']}")
		return results

	def reports(self, display=True):
		"""Search for reports by a given query."""
		search = input("Leita að skýrslu: ").strip()
		results = self.logic_api.search_report(search, self.reports)
		if not results:
			if display:
				print("Engin skýrsla fannst.")
			return []  # Return an empty list if no results

		if display:
			print("Leitarniðurstöður:")
			for report in results:
				print(f"Skýrslunúmer: {report['report_id']}, Fasteignarnúmer: {report['property_id']}, "
					  f"Dagsetning: {report['date']}, Skýrsla: {report['description']}")
		return results

# Example Initialization with Empty Data
employees = []  # Populate dynamically if needed
orders = []
locations = []
properties = []
reports = []

# Instantiate the SearchUI
search_ui = SearchUI(employees, orders, locations, properties, reports)

# Example Usage
search_ui.employee(display=True)  # Print employee search results
order_results = search_ui.order(display=False)  # Return order search results for further processing
print(order_results)  # Example of using returned data
