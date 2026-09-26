1. Problem statement:-
Small clinics and independent medical practitioners often rely on manual, 
paper-based systems to track patient details, consultancy fees, and visit histories.
This manual approach leads to lost records, slow data retrieval during emergencies, 
and difficulty in updating patient information efficiently.
There is a need for a lightweight, accessible digital system to organize and manage patient data instantly.

2. Scope of the project:-
This project is a localized, command-line-based application designed to manage fundamental patient records.
It focuses on in-memory data processing, allowing users to create, search, update, and 
view patient profiles sequentially. 
The scope is limited to administrative front-desk operations and does not 
include complex external database integrations, graphical user interfaces (GUI),
or network-based syncing.

3. Target users:-
* Hospital receptionists and front desk operators.
* Independent doctors managing their own patient files.
* Medical data entry staff at small clinics.

# High-level features

* Patient Registration:- Capture essential demographic and visit details 
                        (Name, Age, Gender, Phone, Doctor Reference, Fee, Last Visit).
* Targeted Search:- Instantly retrieve a specific patient's full medical 
                    administrative file using their registered name.
* Dynamic Updating:- Modify specific data points like a new phone number or an updated consultancy fee
                     without overwriting the entire record.
* Database Viewing:- Display a formatted, numbered registry of all currently enrolled patients in the system.
* Data Validation & Safe Exit:- Built-in error handling for incorrect menu selections and a 
                                confirmation prompt to prevent accidental data loss upon closing.