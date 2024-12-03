# Manager.py
class Manager:
    def __init__(self, name, kennitala, email, address, phone, gsm, location):
        self.name = name
        self.kennitala = kennitala
        self.email = email
        self.address = address
        self.phone = phone
        self.gsm = gsm
        self.location = location

    def __str__(self):
        return (f"Nafn       : {self.name}\n"
                f"Kennitala  : {self.kennitala}\n"
                f"e-mail     : {self.email}\n"
                f"Heim.      : {self.address}\n"
                f"Sími       : {self.phone}\n"
                f"GSM        : {self.gsm}\n"
                f"Staðsetning: {self.location}\n")
