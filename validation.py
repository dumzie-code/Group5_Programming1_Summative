print("Day one on clinic appointment system!")
import datetime
def get_valid_menu():
    while True:
        try:
            menu=int(input("select an option(1-4): "))
            if menu < 1 or menu > 4:
                print("Selection out of range. Please select a number from 1-4 ")
                continue
            break
        except ValueError:
            print("Invalid format. Select a number from 1-4 ")       
        
            
def get_valid_name():
    while True:
            name=input("Please enter your name") 
            if name:
                return name  
            else:
                print("Invalid format. Please enter a valid name")
            
    
def get_valid_date():
     while True:
            try:
                due_date_input= input("Please enter your appointment date")
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date() 
            except ValueError:
                pass
def get_valid_time():
    while True:
        try:
            due_date_input= input("Please enter your appointment time")
            due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date() 
        except ValueError:
            pass
def get_valid_number():
    while True:
        try:
            number=input("Enter your phone number with your country code")
        except ValueError:
            print("Invalid format. Please enter a valid phone number")
def get_valid_pin():
    while True:
        try:
            pin=input("Enter your pin")
        except ValueError:
            print("Invalid format. Please enter a pin")
    
    
#



