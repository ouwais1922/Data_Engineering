import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    "Chills": ["Y", "Y", "Y", "N", "N", "N", "N", "Y"],
    "Runny Nose": ["N", "Y", "N", "Y", "N", "Y", "Y", "Y"],
    "Headache": ["Mild", "No", "Strong", "Mild", "No", "Strong", "Strong", "Mild"],
    "Fever": ["Y", "N", "Y", "Y", "N", "Y", "N", "Y"],
    "Flu?": ["N", "Y", "Y", "Y", "N", "Y", "N", "Y"],
}

symptoms = list(data.keys())[:-1] 

flu_counts = [data[symptom].count("Y") for symptom in symptoms]
no_flu_counts = [data[symptom].count("N") for symptom in symptoms]

x = np.arange(len(symptoms))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width/2, flu_counts, width, label="Flu", color="blue")
ax.bar(x + width/2, no_flu_counts, width, label="No Flu", color="orange")

ax.set_xticks(x)
ax.set_xticklabels(symptoms, rotation=45, ha="right")

ax.set_ylabel("Count")

ax.set_title("Symptom Count for Flu and No Flu Cases")

ax.legend()

plt.tight_layout()
plt.show()
