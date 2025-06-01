import pandas as pd

# Load data
df = pd.read_csv("../data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Basic check
print(df.shape)
print(df.columns)

# Drop unnecessary columns
drop_cols = ['EmployeeNumber', 'EmployeeCount', 'Over18', 'StandardHours']
df.drop(columns=drop_cols, inplace=True)

# Convert target to binary
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# Save cleaned data
df.to_csv("../data/cleaned_employee_data.csv", index=False)

print("Cleaned data saved.")