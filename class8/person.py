class Person():
    def __init__(self, first_name: str, second_name: str | None, middle_name: str | None, phone_number: str):
        self.first_name = first_name
        self.second_name = second_name
        self.middle_name = middle_name
        self.phone_number = phone_number
    
    def __str__(self):
        return self.get_contact_info()
    
    def contains(self, sought: str) -> bool:
        if (sought in self.get_full_name()):
            return True
        return False
    
    def get_properties(self) -> str:
        properties = str()
        properties += f"First name: {self.first_name}\n"
        if self.second_name is not None:
            properties += f"Second name: {self.second_name}\n"
        if self.middle_name is not None:
            properties += f"Middle name: {self.middle_name}\n"
        properties += f"Phone number: {self.phone_number}"
        return properties    
    
    def get_full_name(self) -> str:
        if self.second_name is not None and self.middle_name is not None:
            return f"{self.first_name} {self.second_name} {self.middle_name}"
        elif self.middle_name is not None:
            return f"{self.first_name} {self.middle_name}"
        elif self.second_name is not None:
            return f"{self.first_name} {self.second_name}"
        return self.first_name
    
    def get_contact_info(self) -> str:
        return f"{self.get_full_name()}\n {self.phone_number}"