import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Updated dataset
data = {
    'disease': ['Flu', 'COVID-19', 'Malaria', 'Common Cold', 'Pneumonia', 'Diabetes', 'Hypertension', 'Allergies', 'Arthritis', 'Asthma'],
    'symptom_fever': [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    'symptom_cough': [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    'symptom_fatigue': [1, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    'symptom_headache': [1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    'symptom_loss_of_taste': [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    'symptom_shortness_of_breath': [0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    'symptom_diarrhea': [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    'symptom_nausea': [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    'symptom_sore_throat': [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    'symptom_vomiting': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

X = df.drop('disease', axis=1)
y = df['disease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Updated classification report format
report = classification_report(y_test, predictions, zero_division=1, output_dict=True)
for disease, metrics in report.items():
    print(f"Disease: {disease}")
    for metric, value in metrics.items():
        print(f"{metric.capitalize()}: {value}")
    print("------------------------")
