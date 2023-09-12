class Phonebook():
    book = list()
    file_path = str()
    
    def __init__(self):
        self.intro()
        self.main()
        
    def intro(self):
        print("Do you want to create a new phonebook or use an existing one?")
        choice = input("Options: new, existing, exit\n").lower()
        if choice == "existing":
            self.file_path = input("Enter path to file: ")
            try:
                with open(self.file_path, "r"):
                    return
                    
            except Exception:
                print("Couldn't find a file under this file path. We created a new one for you")
                with open(self.file_path, "w"):
                    return
                
    def main(self):
        self.initialize_phonebook(self.file_path)
        print()
        self.print_phonebook()
        running = True
        while running:
            action = input("Menu: print, search, add, edit, delete, exit\n").lower()
            if action == "print":
                self.print_phonebook()
                
            elif action == "search":
                self.search()
                
            elif action == "add":
                self.add_contact()
                
            elif action == "edit":
                try: 
                    self.edit_contact()
                except Exception as e:
                    print(e)
            
            elif action == "delete":
                self.delete_contact()
                
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
            if person.contains(criteria):
                response.append(i)
                print(f"{person}\n")
        if len(response) == 0:
            print("No contact was found")
        return response
    
    def edit_file(self):
        with open(self.file_path, "w") as editor:
            for person in self.book:
                editor.write(person.get_contact_info() + "\n")
    
    def print_search_result(self, result: list[int]):
        count = 1
        for search_index in result:
            print(f"{count}. {self.book[search_index]}")
            count += 1
        
    def search_single_person(self) -> int:
        search_result = self.search()
        if len(search_result) > 1:
            finding_user = True
            choice = int()
            while finding_user:
                self.print_search_result(search_result)
                choice = self.__input_number__("Enter an edited contact index")
                if choice <= len(search_result):
                    finding_user = False
                else: 
                    print("Wrong index")
            return search_result[choice - 1]
                    
        elif len(search_result) == 1:
            return search_result[0]
        else:
            return -1
    
    def delete_contact(self):
        contact_index = self.search_single_person()
        if contact_index == -1:
            raise Exception("Can't find such contact")
        self.book.pop(contact_index)
        self.edit_file()     
    
    def edit_contact(self):
        contact_index = self.search_single_person()
        if contact_index == -1:
            raise Exception("Can't find such contact")
        
        print()
        
        editing = True
        while editing:
            print(self.book[contact_index].get_properties() + "\n")
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
                self.edit_file()
                
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
        self.append_output(-1)
        
    def append_output(self, contact_index):
        with open(self.file_path, 'a') as writer:
            writer.write(f"\n{self.book[contact_index].get_contact_info()}")
    
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
    
Phonebook()