
from db.models import User, Comic, UserComic
from sqlalchemy.orm import Table
from prettycli import yellow, red, color
from banners import Banner

banners = Banner()


   
def start(self):
        self.clear(40)
        banners.welcome()
        self.clear(4)
        
        return self.welcome()
    
    
def welcome(self):
        print("Are you new here?")
        selection = input.yes_no(option="Exit")
        if selection == "Yes":
            self.sign_up()
        elif selection == "Exit":
            self.exit()
        else:
            self.login()


def sign_up(self):
        username = self.collect_data("What is your username?")
        if User.find_by(username=username):
            print(red("That username is taken! Please try again."))
            self.sign_up()
        else:
            password = self.collect_data("What is your password?")
            self.current_user = User.create(username=username, password=password)
        
        if self.current_user:
            self.main_menu()
        else:
            print("Please try again.\n")
            self.welcome()    
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
    
    
    
    
    
 
    

    