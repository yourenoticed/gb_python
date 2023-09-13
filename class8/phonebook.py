from person import Person
class Phonebook():
    def __init__(self, file_path: str):
        self.book = list()
        self.file_path = file_path
        self.initialize_phonebook()
    
    def search(self, prompt: str) -> list[int]:
        response = list()
        for i, person in enumerate(self.book):
            if person.contains(prompt):
                response.append(i)
                print(f"{person.get_properties()}\n")
        if len(response) == 0:
            print("No contact was found")
        return response
    
    def edit_file(self):
        with open(self.file_path, "w") as editor:
            for i, person in enumerate(self.book):
                if i < len(self.book) - 1:
                    editor.write(person.get_contact_info() + "\n")
                else:
                    editor.write(person.get_contact_info())
    
    def print_search_result(self, result: list[int]):
        count = 1
        for search_index in result:
            print(f"{count}. {self.book[search_index]}")
            count += 1
        
    def search_single_person(self, search_prompt: str) -> int:
        search_result = self.search(search_prompt)
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
    
    def delete_contact(self, search_prompt: str):
        contact_index = self.search_single_person(search_prompt)
        if contact_index == -1:
            raise Exception("Can't find such contact")
        deleting = True
        while deleting:
            action = input("Are you sure you want to delete this contact? y\\n\n").lower()
            if action in ["y", "yes"]:
                self.book.pop(contact_index)
                self.edit_file() 
                deleting = False
            elif action in ["n", "no"]:
                deleting = False
            
    def edit_contact(self, search_prompt: str):
        contact_index = self.search_single_person(search_prompt)
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
        if len(self.book) <= 1: self.edit_file()
        else: self.append_output()
        
    def append_output(self):
        with open(self.file_path, 'a') as writer:
            writer.write(f"\n{self.book[-1].get_contact_info()}")
    
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
                             
    def initialize_phonebook(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines),2):
                first_name, second_name, middle_name, phone_number = self.get_contact_info(f"{''.join(lines[i])}{lines[i + 1]}")
                self.book.append(Person(first_name, second_name, middle_name, phone_number))