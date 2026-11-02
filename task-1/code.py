

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Validate charges
if (age < 0 or consultation < 0 or
    diagnostic < 0 or treatment < 0):

    print("Invalid patient details or charges")

else:
    # Calculate total bill
    total = consultation + diagnostic + treatment

    concession = 0

    # Senior citizen concession
    if age >= 60:
        concession += total * 0.10

    # Bill-based concession
    if total >= 10000:
        concession += total * 0.05

    # Calculate final bill
    final_bill = total - concession

    # Patient classification
    if final_bill < 5000:
        category = "Low Payment"

    elif final_bill <= 15000:
        category = "Medium Payment"

    else:
        category = "High Payment"

    # Display bill details
    print("\n----- HOSPITAL BILL -----")
    print("Patient Name:", name)
    print("Patient Age:", age)
    print("Consultation Charges:", consultation)
    print("Diagnostic Charges:", diagnostic)
    print("Treatment Charges:", treatment)
    print("Total Bill:", total)
    print("Total Concession:", concession)
    print("Final Bill:", final_bill)
    print("Patient Category:", category)
