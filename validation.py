print("Day one on clinic appointment system!")
from datetime import datetime
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
            
def get_valid_admin_menu():
    #This function displays the options available
    #to an adminstrator.

    while True:
        print("=====ADMINISTRATOR MENU=====")
        print("1.Register new patient")
        print("2.Display all patients")
        print("3.Search patient")
        print("4.Update patient information")
        print("5.Add doctor")
        print("6.View appointments")
        print("7.Logout")
        
        try:
            choice = int(input("Choose an option(1-7): "))

            if choice < 1 or choice > 7:
                print("Selection out of range. Please select a number from 1-7 ")
                continue
            break
        except ValueError:
           print("Invalid format. Select a number from 1-7 ")       
                    
def get_valid_doctor_menu()  :                 
    while True:
        print("=====DOCTOR MENU=====")
        print("1.View appointment")
        print("2.View patient information")
        print("3.Update appointment")
        print("4.Logout")
        try:
            choice = int(input("Choose an option(1-4): "))
        
            if choice < 1 or choice > 4:
                print("Selection out of range. Please select a number from 1-7 ")
                continue
            break
        except ValueError:
            print("Invalid format. Select a number from 1-4 ")  
            
            
def get_valid_patient_menu():
    while True:
        print("========PATIENT MENU========")
        print("1.View my infomation")
        print("2.Book appointment")
        print("3.View my appointment")
        print("4.Cancel appointment")
        print("5.Logout")
        try:
            choice = int(input("Choose an option(1-5): "))
                    
            if choice < 1 or choice > 5:
                print("Selection out of range. Please select a number from 1-7 ")
                continue
            break
        except ValueError:
                print("Invalid format. Select a number from 1-5 ")  
        
            
def get_valid_firstname():
   while True:
    firstname=input("Please enter your first name: ").strip()
    if firstname=="":
        print("Oops sorry first name can not be left empty")
        continue
    if not firstname.isalpha():
        print("Invalid format. Please enter a valid name")
        continue
    if firstname.isalpha():
        return  firstname      
                
def get_valid_lastname():
    while True:
        lastname=input("Please enter your last name: ").strip()
        if lastname=="":
            print("Oops sorry lasst name can not be left empty")
            continue
        if not lastname.isalpha():
            print("Invalid format. Please enter a valid name")
            continue
        if lastname.isalpha():
            return  lastname      
           
        
                        
                            
def get_valid_date():
    while True:
        try:
            date_input= input("Please enter your appointment date: ")
            date = datetime.strptime(date_input, "%Y-%m-%d").date() 
            if date_input=="":
                print("Oops sorry date can not be left empty enter a valid dat")
                continue 
            break
        except ValueError:
            print("Invalid format. Please try again with this format date as, YYYY-MM-DD: ")
    return date

def get_valid_number():
    while True:
        try:
            number=input("Enter your phone number with your country code")
            
        except ValueError:
            print("Invalid format. Please enter a valid phone number")
        return number

def get_valid_id():
    pass


    
#
get_valid_date()


