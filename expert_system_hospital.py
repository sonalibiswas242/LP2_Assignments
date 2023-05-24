def add_patient(patients):
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    patients.append({"Name": name, "Age": age, "Gender": gender})
    print("Patient added successfully!")


def search_patient(patients):
    name = input("Enter patient name to search: ")
    found = False
    for patient in patients:
        if patient["Name"] == name:
            print("Patient found:")
            print("Name:", patient["Name"])
            print("Age:", patient["Age"])
            print("Gender:", patient["Gender"])
            found = True
            break
    if not found:
        print("Patient not found.")


def display_all_patients(patients):
    if not patients:
        print("No patients found.")
        return
    print("All patients:")
    for patient in patients:
        print("Name:", patient["Name"])
        print("Age:", patient["Age"])
        print("Gender:", patient["Gender"])


def predict_disease():
    symptoms = input("Enter the symptoms (separated by commas): ").lower().split(",")

    # Define the dictionary of symptoms and their associated probable diseases
    symptom_disease_mapping = {
        "fever": ["flu", "malaria", "dengue"],
        "cough": ["common cold", "bronchitis", "pneumonia"],
        "headache": ["migraine", "tension headache", "sinusitis"],
        "fatigue": ["chronic fatigue syndrome", "anemia", "hypothyroidism"],
        "abdominal pain": ["appendicitis", "gastritis", "gallstones"],
        "rash": ["allergic reaction", "eczema", "psoriasis"],
        # Add more symptom-disease mappings as needed
    }

    predicted_diseases = []
    for symptom in symptoms:
        if symptom in symptom_disease_mapping:
            predicted_diseases.extend(symptom_disease_mapping[symptom])

    if predicted_diseases:
        print("Predicted diseases:")
        for disease in set(predicted_diseases):
            print("- " + disease)
        suggest_best_doctor(predicted_diseases)
    else:
        print("No diseases found for the given symptoms.")


def suggest_best_doctor(predicted_diseases):
    # Define the dictionary of diseases and their associated best doctors
    disease_doctor_mapping = {
        "flu": "Dr. John Smith",
        "malaria": "Dr. Emily Johnson",
        "dengue": "Dr. Michael Davis",
        "common cold": "Dr. Sarah Thompson",
        "bronchitis": "Dr. David Wilson",
        "pneumonia": "Dr. Jennifer Anderson",
        "migraine": "Dr. Robert Thomas",
        "tension headache": "Dr. Samantha Roberts",
        "sinusitis": "Dr. Daniel Brown",
        "chronic fatigue syndrome": "Dr. Michelle Adams",
        "anemia": "Dr. Christopher Lee",
        "hypothyroidism": "Dr. Olivia Taylor",
        "appendicitis": "Dr. Andrew Clark",
        "gastritis": "Dr. Victoria Martinez",
        "gallstones": "Dr. Matthew Turner",
        "allergic reaction": "Dr. Ava Cooper",
        "eczema": "Dr. Benjamin Hall",
        "psoriasis": "Dr. Emily Scott",
        # Add more disease-doctor mappings as needed
    }

    print("Suggested best doctor(s):")
    for disease in set(predicted_diseases):
        if disease in disease_doctor_mapping:
            print("- " + disease_doctor_mapping[disease])
        else:
            print("- No specific doctor found for " + disease)


# Rest of the code...

def exit_program():
    print("Exiting the program. Goodbye!")
    exit()


def main():
    patients = []
    while True:
        print("\nHOSPITAL AND MEDICAL FACILITIES SYSTEM")
        print("1. Add Patient")
        print("2. Search Patient")
        print("3. Display All Patients")
        print("4. Predict Disease")
        print("5. Suggest Best Doctor")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_patient(patients)
        elif choice == "2":
            search_patient(patients)
        elif choice == "3":
            display_all_patients(patients)
        elif choice == "4":
            predict_disease()
        elif choice == "5":
            suggest_best_doctor()
        elif choice == "6":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()