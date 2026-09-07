print("========================================")
print("Clinic Appointment And Management System")
print("========================================")

def main():  # this particular function will control the main flow
              #of the application'

    while True:
        #Keep the system running until the user chooses to exit
        print("Clinic system is running ...")  

    #Ask the user for their ID or type Exit 
        user_id =input("Enter your ID or type Exit")
        
        if user_id =="Exit":
            #close the system when the user chooses Exit
            print("Thank you for using the Clinic Management System.")
            print("System closed successfully")
            break

    print("Welcome to the System!")