import streamlit as st
import pandas as pd

# Page title
st.title("🩺 BMI Calculator for Patients")

# Input number of patients
num = st.number_input("How many patients?", min_value=1, max_value=20, step=1)

# Collect patient data
data = []

for i in range(num):
    st.subheader(f"Patient #{i+1}")
    name = st.text_input(f"Name #{i+1}", key=f"name_{i}")
    weight = st.number_input(f"Weight (kg) #{i+1}", key=f"weight_{i}")
    height = st.number_input(f"Height (m) #{i+1}", key=f"height_{i}")

    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        data.append({
            "Name": name,
            "Weight": weight,
            "Height": height,
            "BMI": round(bmi, 2),
            "Category": category
        })

# Display table
if data:
    df = pd.DataFrame(data)
    st.subheader("📋 Patient BMI Report")
    st.dataframe(df)

    # Plot BMI chart
    st.subheader("📊 BMI Chart")
    st.bar_chart(df.set_index("Name")["BMI"])

    # 🔽 Save CSV and provide download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download CSV", data=csv, file_name='bmi_report.csv', mime='text/csv')
