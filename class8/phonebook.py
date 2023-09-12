class Phonebook():
    book = list()
    def __init__(self):
        self.main()
    
    def main(self):
        file_path = input("Enter path to file: ")
        self.initialize_phonebook(file_path)
        print()
        self.print_phonebook()
        running = True
        while running:
            action = input("Menu: print, search, add, edit, exit\n").lower()
            if action == "print":
                self.print_phonebook()
                
            elif action == "search":
                self.search()
                
            elif action == "add":
                self.add_contact()
                
            elif action == "edit":
                try: 
                    self.edit_contact()
                except Exception as e: print(e)
                
            elif action == "exit":
                running = False
                
            else:
                print("Enter a proper action")
    
    def search(self) -> list[int]:
        response = list()
        print("Searching")
        criteria = input("Input prompt: ")
        print()
        for i, person in enumerate(self.book):
            if criteria in [person.first_name, person.second_name, person.middle_name]:
                response.append(i)
                print(f"{person}\n")
        if len(response) == 0:
            print("No contact was found")
        return response
    
    def print_search_result(self, result: list[int]):
        count = 1
        for search_index in result:
            print(f"{count}. {self.book[search_index]}")
            count += 1
        
    def search_single_person(self) -> int:
        search_result = self.search()
        if len(search_result) > 1:
            self.print_search_result(search_result)
            choice = self.__input_number__("Enter an edited contact index")
            return search_result[choice - 1]
        elif len(search_result) == 1:
            return search_result[0]
        else:
            return -1
            
    def edit_contact(self):
        contact_index = self.search_single_person()
        if contact_index == -1:
            raise Exception("Can't find such contact")
        editing = True
        while editing:
            print("What do you want to change?")
            edit_part = input("Options: first name, second name, middle name, number, exit\n").lower()
            if edit_part == "first name":
                edit = input(f"\nEditing {self.book[contact_index].first_name} to ")
                self.book[contact_index].first_name = edit
            elif edit_part == "second name":
                edit = input(f"\nEditing {self.book[contact_index].second_name} to ")
                self.book[contact_index].second_name = edit
            elif edit_part == "middle name":
                edit = input(f"\nEditing {self.book[contact_index].middle_name} to ")
                self.book[contact_index].middle_name = edit
            elif edit_part == "number":
                edit = input(f"\nEditing {self.book[contact_index].phone_number} to ")
                self.book[contact_index].phone_number = edit
            elif edit_part == "exit":
                editing = False
            else:
                print("Enter a valid parameter")  
        
    def __input_number__(self, msg: str) -> int:
        while True:
            text = input(msg + ": ")
            if text.isdigit() and int(text) > 0:
                return int(text)
            elif int(text) <= 0:
                print("Please, input a valid index")
            else:
                print("Please enter a positive integer number")
                
    def print_phonebook(self):
        print()
        for person in self.book:
            print(f"{person}\n")
            
    def add_contact(self):
        print()
        first_name = input("Enter a first name: ")
        second_name = input("Enter a second name (optional): ")
        middle_name = input("Enter a middle name (optional): ")
        phone_number = input("Enter a phone number: ")
        if second_name == "":
            second_name = None
        if middle_name == "":
            middle_name = None
            
        self.book.append(Person(first_name, second_name, middle_name, phone_number))
        self.append_output(self.book[-1])
        
    def append_output(self, contact_index):
        pass
    
    def clean_contact_info(self, infos: list[str]):
        for i, val in enumerate(infos):
            infos[i] = val.strip("\n").strip(" ")
            
    def get_contact_info(self, line: str):
        first_name = str()
        second_name = None
        middle_name = None
        phone_number = str()
        
        contact_info = line.split()
        self.clean_contact_info(contact_info)
        
        if len(contact_info) < 2:
            raise Exception("Wrong contact information found")
        else:
            first_name = contact_info[0]
            phone_number = contact_info[-1]
            
            if len(contact_info) == 3:
                second_name = contact_info[1]
            elif len(contact_info) >= 4:
                middle_name = contact_info[-2]
                second_name = " ".join([word for word in contact_info[1:-2]])    
            return (first_name, second_name, middle_name, phone_number)
                
                
    def initialize_phonebook(self, file_path: str):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines),2):
                    first_name, second_name, middle_name, phone_number = self.get_contact_info(f"{''.join(lines[i])}{lines[i + 1]}")
                    self.book.append(Person(first_name, second_name, middle_name, phone_number))
        except(FileNotFoundError):
            print("Fuck you, wrong path")


class Person():
    def __init__(self, first_name: str, second_name: str | None, middle_name: str | None, phone_number: str):
        self.first_name = first_name
        self.second_name = second_name
        self.middle_name = middle_name
        self.phone_number = phone_number
    
    def __str__(self):
        return self.get_contact_info()
    
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
    
Phonebook()