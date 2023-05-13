import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Create a dataframe from the provided dataset
data = {'chills': ['Y', 'Y', 'Y', 'N', 'N', 'N', 'N', 'Y'],
        'runny_nose': ['N', 'Y+', 'N', 'Y', 'N', 'Y', 'Y', 'Y'],
        'headache': ['Mild', 'No', 'Strong', 'Mild', 'No', 'Strong', 'Strong', 'mild'],
        'fever': ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y'],
        'flu': ['N', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'Y']}

df = pd.DataFrame(data)

# Convert the runny nose values to a consistent format
df['runny_nose'] = df['runny_nose'].apply(lambda x: 'Y' if x == 'Y+' else x)

# Convert the headache values to a consistent format
df['headache'] = df['headache'].apply(lambda x: x.capitalize())

# Use LabelEncoder to convert categorical variables into numerical values
encoder = LabelEncoder()
for col in df.columns:
    df[col] = encoder.fit_transform(df[col])

# Compute the correlation matrix
corr = df.corr()

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", cbar=True, xticklabels=corr.columns, yticklabels=corr.columns)
plt.title("Correlation Matrix")
plt.show()
