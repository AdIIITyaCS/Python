class DiseaseSymptomGraph:
    def __init__(self, diseases, symptoms):
        self.diseases = diseases
        self.symptoms = symptoms
        self.num_diseases = len(diseases)
        self.num_symptoms = len(symptoms)

        # Initialize the adjacency matrix with zeros
        self.adj_matrix = []
        for i in range(self.num_diseases):
            row = []
            for j in range(self.num_symptoms):
                row.append(0)
            self.adj_matrix.append(row)

    def add_association(self, disease, symptom):
        disease_index = self.diseases.index(disease)
        symptom_index = self.symptoms.index(symptom)
        self.adj_matrix[disease_index][symptom_index] = 1
        self.adj_matrix[symptom_index][disease_index] = 1

    def remove_association(self, disease, symptom):
        disease_index = self.diseases.index(disease)
        symptom_index = self.symptoms.index(symptom)
        self.adj_matrix[disease_index][symptom_index] = 0
        self.adj_matrix[symptom_index][disease_index] = 0

    def display_matrix(self):
        for row in self.adj_matrix:
            print(row)

# Example usage
diseases = ["Flu", "Cold", "Diarrhea"]
symptoms = ["Fever", "Cough", "Fatigue"]

disease_symptom_graph = DiseaseSymptomGraph(diseases, symptoms)


print("Initial adjacency matrix:")
disease_symptom_graph.display_matrix()

print("\nSetting up some relation: ")
disease_symptom_graph.add_association("Flu", "Fever")
disease_symptom_graph.add_association("Flu", "Cough")
disease_symptom_graph.add_association("Cold", "Cough")
disease_symptom_graph.add_association("Diarrhea", "Fever")
disease_symptom_graph.display_matrix()


print("\nAdding association between Cold and Fatigue:")
disease_symptom_graph.add_association("Cold", "Fatigue")
disease_symptom_graph.display_matrix()

print("\nRemoving association between Cold and Cough:")
disease_symptom_graph.remove_association("Cold", "Cough")
disease_symptom_graph.display_matrix()
