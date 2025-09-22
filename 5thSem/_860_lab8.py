class Patient:
    def __init__(self):
        self.symptoms_dict = {
            'MEASLES': ['Clouding of cornea','Deep or extensive mouth ulcers','Pus draining from the eye'],
            'Malaria': ['Stiff neck','Bulging fontanelle','Fever'],
            'DIARRHOEA': ['Lethargic','Sunken eyes','Restless','DEHYDRATION','DYSENTERY'],
            'Pneumonia': ['Stridor in calm child','Chest indrawing','Fast breathing'],
            'jaundice' :['Convulsions','Nasal flaring','Palms and soles yellow']
        }
    def get_diseases(self, input_symptoms):
        matching_diseases = []
        for disease, symptoms in self.symptoms_dict.items():
            symptoms_present = any(symptom in input_symptoms for symptom in symptoms)
            if symptoms_present:
                matching_diseases.append(disease)
        return matching_diseases



# Get user input for symptoms
user_input_symptoms = input("Enter symptoms (comma-separated): ").split(',')

# Example usage
patient = Patient()
print("Input symptoms:", user_input_symptoms)
possible_diseases = patient.get_diseases(user_input_symptoms)

if possible_diseases:
    print("Possible diseases based on symptoms:", possible_diseases)
else:
    print("No matching diseases found for the given symptoms.")