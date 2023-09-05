class number_input():    
    def is_float(checked_value: str): # works for positive numbers only
        if checked_value.count('.') != 1:
            return False
        
        for i, val in enumerate(checked_value):
            if val == '.' and i != 0:
                continue
            
            if not val.isdigit():
                return False
            
        return True
        
            
    def input_any_number(msg: str):
        while True:
            user_input = input(msg + ': ')
            
            if user_input.isdigit():
                return int(user_input)
            
            elif number_input.is_float(user_input):
                return float(user_input)
            
            elif user_input[0] == '-':
            
                if user_input[1:].isdigit():
                    return int(user_input)
                elif number_input.is_float(user_input[1:]):
                    return float(user_input)
                else:
                    print('Please, enter a number')
            
            else:
                print('Please, enter a number')
    
    
    def input_positive_int(msg: str) -> int:
        while True:
            user_input = input(msg + ': ')
            
            if user_input.isdigit():
                return int(user_input)
            
            print('Please, enter a positive integer')
            
            
    def input_int(msg: str) -> int:
        while True:
            user_input = input(msg + ': ')
            
            if user_input.isdigit():
                return int(user_input)
            elif user_input[0] == '-':
                if user_input[1:].isdigit():
                    return int(user_input)
            else:
                print('Please, enter an integer')