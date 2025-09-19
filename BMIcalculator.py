# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Function to classify BMI
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# List to store patient data
patients = []

# Ask how many patients
num = int(input("How many patients? "))

# Get data from user
for i in range(num):
    print(f"\nEnter details for Patient #{i+1}")
    name = input("Name: ")
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))
    
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    patients.append({
        "name": name,
        "weight": weight,
        "height": height,
        "bmi": bmi,
        "category": category
    })

# Display all results
print("\n--- Patient BMI Report ---")
for p in patients:
    print(f"{p['name']}: BMI = {p['bmi']} ({p['category']})")
