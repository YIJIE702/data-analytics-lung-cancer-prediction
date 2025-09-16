import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import numpy as np

# Read the Excel file
df = pd.read_csv('C:/Users/User/OneDrive/Desktop/Data Analytic Group Assignment/cancer_patient_datasets.csv')

# Define the columns to check
columns_to_check = ['Gender', 'Air Pollution', 'Alcohol use', 'Dust Allergy', 'OccuPational Hazards', 'Genetic Risk', 'chronic Lung Disease',
                    'Balanced Diet', 'Obesity', 'Smoking', 'Passive Smoker', 'Chest Pain', 'Coughing of Blood', 'Fatigue', 'Wheezing', 
                    'Swallowing Difficulty', 'Dry Cough', 'Snoring']

# Loop over the columns and print the count of values that are not in the range of 1 to 9
for col in columns_to_check:
    count = len(df[~df[col].between(1,9)])
    print(f"value(s) of column {col} that not in the range of 1 to 9 : {count}")
print("\n")
       
# Count the number of missing values in each column
missing_values = df.isnull().sum()
missing_values = missing_values.transpose().reset_index()
missing_values.rename(columns={'index': 'Parameter'}, inplace=True)
print(missing_values)

# Check for missing values
if df.isnull().values.any():
    print("The dataset contains missing values")
else:
    print("The dataset does not contain missing values")
print("\n")

# Update the values in the "Level" column
df['Level'] = df['Level'].replace({'Low': 1, 'Medium': 2, 'High': 3})

# Perform data profiling
df_stats = df.describe().apply(lambda x: round(x, 2))
df_stats = df_stats.transpose().reset_index()
df_stats.rename(columns={'index': 'Parameter'}, inplace=True)
print(df_stats)
print("\n")

# Handle missing data
df.dropna(inplace=True)

# Save the statistical analysis to a new Excel file
df_stats.to_csv('analysis.csv', index=False)
# Save the updated DataFrame to a new Excel file
df.to_csv('updated_dataset.csv', index=False)
