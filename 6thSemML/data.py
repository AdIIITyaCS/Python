import csv 
data = [
    ["Sky", "Temp", "Humidity", "Wind", "Water", "Forecast", "EnjoySport"],
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
]

# Create and write to the CSV file
with open("file.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created: file.csv")
