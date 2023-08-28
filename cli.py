from sqlalchemy.orm import Table


def start():
    print("***Welcome to Comic Selector***")
    print("1. Select Comic")
    print("2. ADD Comic ")
    print("3. Exit ")
    
    
start()
    
    
user_input = input("Please Select a number(1-3)")
    
        #handle_user_input(user_input)
    
def handle_user_input(input):
        is_number = input.isdigit()
    if is_number:
        selection = int(input)
        if 1<= selection <= 3:
            handle_selection(selection)
        else:
            print("try again")        
        
start()
    
    
    
    
    
 
    

    