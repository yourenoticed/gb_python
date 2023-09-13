from phonebook import Phonebook

class App():
    def run(self):
        self.intro()
        self.phonebook = Phonebook(self.file_path)
        self.main()

    def intro(self):
        print("Do you want to create a new phonebook or use an existing one?")
        choice = input("Options: new, existing\n").lower()
        if choice == "existing":
            self.file_path = input("Enter path to file: ")
            try:
                with open(self.file_path, "r"):
                    return
                    
            except Exception:
                print("Couldn't find a file under this file path. We created a new one for you")
                with open(self.file_path, "x"):
                    return
                    
        else:
            self.file_path = (input("Enter path to file: "))
            with open(self.file_path, "x"):
                return
            
    def main(self):
        print()
        self.phonebook.print_phonebook()
        running = True
        while running:
            action = input("Menu: print, search, add, edit, delete, exit\n").lower()
            if action == "print":
                self.phonebook.print_phonebook()
                
            elif action == "search":
                prompt = self.get_prompt()
                self.phonebook.search(prompt)
                
            elif action == "add":
                self.phonebook.add_contact()
                
            elif action == "edit":
                try:
                    prompt = self.get_prompt() 
                    self.phonebook.edit_contact(prompt)
                except Exception as e:
                    print(e)
            
            elif action == "delete":
                prompt = self.get_prompt()
                self.phonebook.delete_contact(prompt)
                
            elif action == "exit":
                running = False
                
            else:
                print("Enter a proper action")
                
    def get_prompt(self) -> str:
        print("Searching")
        prompt = input("Input prompt: ")
        print()
        return prompt
                
app = App()
app.run()