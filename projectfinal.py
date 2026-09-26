def main():
    patient_records = {}

    while True:
        print("------------------------------") # User interface menu
        print("HOSPITAL PATIENT RECORD SYSTEM")
        print("------------------------------")
        print("1 Add New Patient Record")
        print("2 Search Patient Details")
        print("3 Update Patient Details")
        print("4 View All Patient Records")
        print("5 Exit System")
        print("------------------------------")

        choice = input("Select an option from 1-5 = ")
        if choice == "1": #case 1 is for adding the new patient data
            print("Add New Patient Record")
            print("----------------------")
            name = input("Enter Patient Full Name = ").strip().lower()
            age = input("Enter Patient Age = ")
            phone = input("Enter Phone Number = ")
            fee = input("Enter Total Consultancy Fee = ")
            last_visit = input("Enter Last Visited Date = ")
            gender = input("Enter Patient Gender (Male/Female/Other) = ").strip().lower()
            doc_ref = input("Which doctor referred this patient..? = ").strip().lower()
            if not doc_ref:
                doc_ref = "You may go inside"

            search_key = name.lower()
            patient_records[search_key] = {"Name": name,"Age": age,"Phone": phone,"Doctor Reference": doc_ref,"Consultancy Fee": fee,"Last Visited": last_visit,"Gender": gender,}

            print(f"Success...! Patient '{name}' registered successfully....!")
        elif choice == "2": #case 2 is for searching the recorded patient data
            print("Search Patient Details")
            print("----------------------")
            search_name = input("Enter Patient Name to search: ").lower()

            if search_name in patient_records:
                patient = patient_records[search_name]
                print("Full Name = ", patient["Name"])
                print("Age = ", patient["Age"])
                print("Gender = ", patient["Gender"])
                print("Phone Number = ", patient["Phone"])
                print("Doctor Reference = ", patient["Doctor Reference"])
                print("Consultancy Fee = ", patient["Consultancy Fee"])
                print("Last Visited = ", patient["Last Visited"])

            else:
                print("!Error! No patient record found with that name.....!! Please enter the Name again.")
        elif choice == "3": #case 3 is for updating the patient details
            print("Update Patient Details")
            print("----------------------")

            search_name = input("Enter Patient Name to update or type 'exit' to go back = ").lower() #if user by mistakenly enter 3, so for returning to the menu page

            if search_name == 'exit':
                print("Returning to Main Menu...")
                continue  #Directly wil return to main menu

            if search_name in patient_records:
                patient = patient_records[search_name]

                print(f"Current Record for '{patient['Name']}':")
                print(f"1 Age = {patient['Age']}")
                print(f"2 Phone Number = {patient['Phone']}")
                print(f"3 Doctor Reference = {patient['Doctor Reference']}")
                print(f"4 Consultancy Fee = {patient['Consultancy Fee']}")
                print(f"5 Last Visited = {patient['Last Visited']}")

                field_choice = input("Which data you want to update from 1-5 = ")

                if field_choice == "1":
                    new_age = input("Enter new Age: ")
                    patient['Age'] = new_age
                    print("Success...! Age updated successfully.....!")
                elif field_choice == "2":
                    new_phone = input("Enter new Phone Number: ")
                    patient['Phone'] = new_phone
                    print("Success...! Phone Number updated successfully....!")
                elif field_choice == "3":
                    new_doc = input("Enter new Referring Doctor: ")
                    patient['Doctor Reference'] = new_doc
                    print("Success...! Doctor Reference updated successfully.....!")
                elif field_choice == "4":
                    new_fee = input("Enter new Consultancy Fee: ")
                    patient['Consultancy Fee'] = new_fee
                    print("Success...! Consultancy Fee updated successfully.....!")
                elif field_choice == "5":
                    new_visit = input("Enter new Last Visited Date: ")
                    patient['Last Visited'] = new_visit
                    print("Success...! Last Visited date updated successfully.....!")
                else:
                    print("Error! Invalid option selected, Please enter a number between 1 and 5.")
            else:
                print("Error! No patient record found with that name.")
        elif choice == "4": #case 4 is for viewing all the patient data
            print("All Patient Records")
            print("-------------------")

            if not patient_records:
                print("No patient records found in the system")
            else:
                ptcnt = 1 #ptcnt means Patient count =1
                for key in patient_records:
                    p = patient_records[key]

                    print(f"Patient {ptcnt}")
                    print("------------------------")
                    print(f"Name = {p['Name']}")
                    print(f"Age = {p['Age']}")
                    print(f"Phone = {p['Phone']}")
                    print(f"Referred By = {p['Doctor Reference']}")
                    print(f"Fee = {p['Consultancy Fee']}")
                    print(f"Last Visited = {p['Last Visited']}")
                    print("----------------------------------------------------")

                    ptcnt = ptcnt+1

        elif choice == "5": #case 5 is for exiting the software
            ch = str(input("Are you sure you want to exit?, if yes press (y) for exit or press (n)for no = ")).strip().lower()
            if ch == "y":
                print("Exiting System...")
                break
            elif ch == "n":
                print("Returning to main menu.....")
            else:
                print("Error! Please select (Y) for yes or (N) for no")
        else:
            print("Error! Invalid choice, Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()