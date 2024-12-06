from Logic.logic_api import LogicAPI
import datetime

class EditUI:
    def __init__(self, employees, properties, orders, reports, locations):
        self.employees = employees
        self.properties = properties
        self.orders = orders
        self.reports = reports
        self.locations = locations
        self.logic_api = LogicAPI()  # Initialize the LogicAPI instance once

    def edit_employee(self):
        user_role = self.get_user_role()
        if user_role not in [2, 3]:
            print("Enginn aðgangur fyrir þessa starfsheiti.")
            return

        employee_id = input("Sláðu inn kennitölu: ").strip()
        employee = self.logic_api.get_employee_by_id(employee_id, self.employees)
        if not employee:
            print("Starfsmaður fannst ekki.")
            return

        # Update employee information
        employee["name"] = input("Nafn: ")
        try:
            employee["ssn"] = int(input("Kennitala: "))
            employee["landline"] = int(input("Sími: "))
            employee["gsm"] = int(input("GSM: "))
        except ValueError:
            print("Kennitala, Sími og GSM verða að vera tölur.")
            return
        employee["email"] = input("Netfang: ")
        employee["address"] = input("Heimilisfang: ")

        print(f"Upplýsingar um '{employee['name']}' hafa verið uppfærðar.")

    def edit_property(self):
        user_role = self.get_user_role()
        if user_role not in [2, 3]:
            print("Enginn aðgangur fyrir þessa starfsheiti.")
            return

        property_id = input("Sláðu inn fasteignarnúmer: ").strip()
        property = self.logic_api.get_property_by_id(property_id, self.properties)
        if not property:
            print("Fasteign fannst ekki.")
            return

        # Update property information
        property["address"] = input("Heimilisfang: ")
        try:
            property["size"] = int(input("Stærð í fermetrum: "))
            property["rooms"] = int(input("Fjöldi herbergja: "))
        except ValueError:
            print("Stærð og Fjöldi herbergja verða að vera tölur.")
            return
        property["location"] = input("Staðsetning: ")
        property["description"] = input("Sláðu inn nýja upplýsingu um fasteign: ")

        print(f"Upplýsingar um fasteign með fasteignarnúmer '{property['fasteignanúmer']}' hafa verið uppfærðar.")

    def edit_order(self):
        user_role = self.get_user_role()
        if user_role not in [2, 3]:
            print("Enginn aðgangur fyrir þessa starfsheiti.")
            return

        order_id = input("Sláðu inn verkbeiðnisnúmer: ").strip()
        order = self.logic_api.get_order_by_id(order_id, self.orders)
        if not order:
            print("Verkbeiðnisnúmer fannst ekki.")
            return

        try:
            order["fasteignanúmer"] = int(input("Sláðu inn fasteignanúmer: "))
        except ValueError:
            print("Fasteignanúmer verður að vera tala.")
            return
        order["status"] = input("Hefur starfsmaður framkvæmt verkefnið? (Já/Nei): ").strip().lower()
        order["address"] = input("Heimilisfang: ")
        order["contractor"] = input("Verktakandi: ")

        print(f"Upplýsingar um verkbeiðni með verkbeiðnisnúmer '{order['verkbeiðnisnúmer']}' hafa verið uppfærðar.")

    def edit_report(self):
        user_role = self.get_user_role()
        if user_role != 1:
            print("Enginn aðgangur fyrir þessa starfsheiti.")
            return

        report_id = input("Sláðu inn skýrslunúmer: ").strip()
        report = self.logic_api.get_report_by_id(report_id, self.reports)
        if not report:
            print("Skýrslunúmer fannst ekki.")
            return

        report["report"] = input("Sláðu inn nýja skýrslu: ")
        report["status"] = input("Gat starfsmaður klárað verkið? (Já/Nei): ").strip().lower()

        print(f"Skýrsla með skýrslunúmer '{report['skýrslunúmer']}' hefur verið uppfærð.")

    def edit_location(self):
        user_role = self.get_user_role()
        if user_role not in [2, 3]:
            print("Enginn aðgangur fyrir þessa starfsheiti.")
            return

        location_id = input("Sláðu inn staðsetningarnúmer: ").strip()
        location = self.logic_api.get_location_by_id(location_id, self.locations)
        if not location:
            print("Staðsetning fannst ekki.")
            return

        location["address"] = input("Heimilisfang: ")
        location["city"] = input("Staðsetning: ")

        print(f"Upplýsingar um staðsetningu með staðsetningarnúmer '{location_id}' hafa verið uppfærðar.")

    def get_user_role(self):
        """Helper method to get the user's role with error handling."""
        try:
            return int(input("Sláðu inn starfsheiti: (1. Starfsmaður, 2. Yfirmaður, 3. Stjórnandi): ").strip())
        except ValueError:
            print("Ógilt gildi. Vinsamlegast sláðu inn tölu.")
            return -1


# Pre-populated data for testing
employees = [
    {"id": "1234567890", "name": "John Doe", "ssn": 1234567890, "landline": 1234567, "gsm": 89101112, "email": "john@example.com", "address": "123 Main St"}
]
properties = [
    {"id": "P123", "address": "456 Elm St", "size": 120, "rooms": 3, "location": "Reykjavik", "description": "Nice property"}
]
orders = []
reports = []
locations = []

# Instantiate and call methods
edit_ui = EditUI(employees, properties, orders, reports, locations)
edit_ui.edit_employee()  # Example call
