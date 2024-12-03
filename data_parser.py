# data_parser.py
from Employee import Employee
from Manager import Manager
import re

def parse_employees_from_file(file_path):
    """Parses employee data from the given file path and returns a list of Employee objects."""
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    employee_pattern = re.compile(
        r"Nafn\s*:\s*(.*?)\n"
        r"Kennitala\s*:\s*(.*?)\n"
        r"e-mail\s*:\s*(.*?)\n"
        r"Heim\.\s*:\s*(.*?)\n"
        r"Sími\s*:\s*(.*?)\n"
        r"GSM\s*:\s*(.*?)\n",
        re.DOTALL
    )

    employees = []
    for match in employee_pattern.finditer(file_content):
        name = match.group(1).strip()
        kennitala = match.group(2).strip()
        email = match.group(3).strip()
        address = match.group(4).strip()
        phone = match.group(5).strip()
        gsm = match.group(6).strip()
        employees.append(Employee(name, kennitala, email, address, phone, gsm))

    return employees

def parse_managers_from_file(file_path):
    """Parses manager data from the given file path and returns a list of Manager objects."""
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    manager_pattern = re.compile(
        r"Yfirmaður á (.*?):\s*"
        r"Nafn\s*:\s*(.*?)\n"
        r"Kennitala\s*:\s*(.*?)\n"
        r"e-mail\s*:\s*(.*?)\n"
        r"Heim\.\s*:\s*(.*?)\n"
        r"Sími\s*:\s*(.*?)\n"
        r"GSM\s*:\s*(.*?)\n",
        re.DOTALL
    )

    managers = []
    for match in manager_pattern.finditer(file_content):
        location = match.group(1).strip()
        name = match.group(2).strip()
        kennitala = match.group(3).strip()
        email = match.group(4).strip()
        address = match.group(5).strip()
        phone = match.group(6).strip()
        gsm = match.group(7).strip()
        managers.append(Manager(name, kennitala, email, address, phone, gsm, location))

    return managers
