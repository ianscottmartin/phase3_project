

def start():
    print("welcome")
    print("1. My Comic")
    print("2. Add Comic")
    print("3. Exit")

    user_input = input("please select (1-3)")

    handle_user_input(user_input)

def handle_user_input(input):
    is_number = input.isdigit()
    if is_number:
        selection = int(input)
        if 1 <= selection >= 3:
            handle_selection(selection)
    else: 
        print("select again")
        start()
        
start()
