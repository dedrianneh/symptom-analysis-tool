# import json
from datetime import datetime

# A dictionary of symptoms set that indicate potential conditions
condition_rules = {
"Flu": {"fever", "cough", "fatigue"},
"Migraine": {"headache", "nausea", "light sensitivity"},
"Asthma": {"cough", "shortness of breath", "wheezing", "tight feeling in chest"},
"Fever": {"headache", "fatigue","sweating", "chills", "high temperature"},
"COVID-19": {"fever", "cough", "loss of taste"}
}
# entry = { "date": "2025-06-01", "symptoms": {"headache", "fatigue", "fever" }

# Step 1 Log symptoms
def log_symptoms():
    symptoms = input("Enter your symptoms (comma-separated): ").lower().split(",")
    symptoms = [s.strip() for s in symptoms]

    today = datetime.today().strftime("%d-%m-%y") # this format prints current date

    symptom_entry = {
        "date": today,
        "symptoms": symptoms
    }
    return symptom_entry

# my_entry = log_symptoms()
# print(my_entry) # just print the entry dictionary

def check_conditions(symptom_entry):
    symptoms_set = set(symptom_entry["symptoms"])
    matched_conditions = []

    for condition, condition_symptoms in condition_rules.items():
        # count how many symptoms match
        common = symptoms_set.intersection(condition_symptoms)
        if len(common) >= 2:
            matched_conditions.append(condition)

    if matched_conditions:
        print("\nThese symptoms can be asscoiated with:")
        for matched_condition in matched_conditions:
            print(f"-{matched_condition}") # print the name of the condition
        print("Please visit your GP for more understanding and a professional opinion.")

    else:
# if no conditions had 3 or more symptoms in common, inform the user accordingly
        print("\nNo condition matched. Please continue to monitor your health and consult a doctor if needed")

# call the log_symptoms function and store its returned dictionary in 'my_entry'
user_entry = log_symptoms()

# print the symptom entry dictionary to show what the user entered along the way
print("\nYour entry:", user_entry)

# call the check_conditions function, passing the symptom entry to evaluate and print possible conditions
check_conditions(user_entry)

# loops, indents, repeating code

# App

import tkinter as tk
from tkinter import messagebox

# app condition rules

conditions_rules = {
    "Flu": {"fever", "cough", "fatigue"},
    "Migraine": {"headache", "nausea", "light sensitivity"},
    "Asthma": {"cough", "shortness of breath", "wheezing", "tight feeling in chest"},
    "Fever": {"headache", "fatigue","sweating", "chills", "high temperature"},
    "COVID-19": {"fever", "cough", "loss of taste"}
}

# GUI functions
def check_conditions(symptoms_input):
    symptoms = [s.strip() for s in symptoms_input.split(",")]
    symptoms_set = set(symptoms)
    matched_conditions = []

    for condition, condition_symptoms in conditions_rules.items():
        if len(symptoms_set.intersection(condition_symptoms)) >= 2:
            matched_conditions.append(condition)

    if matched_conditions:
        message = "Based on your symptoms, you might have:\n" + "\n".join(f"-{c}" for c in matched_conditions)
        message += "\n\nPlease consider visiting your GP for a professional diagnosis."
    else:
        message = "No condition matched. Please continue to monitor your health and consult a doctor if needed"

    messagebox.showinfo("Results", message)

# GUI layout

def launch_app():
    window = tk.Tk()
    window.title("Symptom Checker")
    window.geometry("300x300")

    label = tk.Label(window, text="Enter your symptoms (comma-separated):")
    label.pack(pady=10)

    entry = tk.Entry(window, width=50)
    entry.pack(pady=5)

    def on_submit():
        user_input = entry.get()
        check_conditions(user_input)

    button = tk.Button(window, text="Check Conditions", command=on_submit)
    button.pack(pady=10)

    window.mainloop()

#run app
launch_app()




