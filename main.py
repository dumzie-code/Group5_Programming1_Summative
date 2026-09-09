from validation import get_valid_menu
print("========================================")
print("Clinic Appointment And Management System")
print("========================================")


def main():  # this particular function will control the main flow
   

    while True:
        #Keep the system running until the user chooses to exit
        print("Clinic system is running ...")  

    #Ask the user for their ID or type Exit 
        user_id =input("Enter your ID or type Exit: ")

        if user_id =="Exit":
            #close the system when the user chooses Exit
            print("Thank you for using the Clinic Management System.")
            print("System closed successfully")
            break
        elif user_id =="NEW":  #start the registration process for a new patient
            print("Starting new patient registration")

        elif user_id.startswith("A-"): # An ID starting with A belongs to the Adminstrator 
            print("Opening Adminstrator Menu")

        elif user_id.startswith("DR-"):
            print("Opening Doctor Menu ")

        elif user_id.startswith("P"):
            #an ID starting with P belongs to a doctor.
            print("Opening Patient Menu")


        else:
            #this runs when the ID does not match
            #any of the accepted ID formats
            print("Invalid ID.Please enter a valid ID.")


    print("Welcome to the System!")
menu =get_valid_menu() 
if menu==1:
    main()