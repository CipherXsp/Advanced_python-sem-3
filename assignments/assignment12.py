import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "CustomerID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Age": [25, 35, 45, np.nan, 29, 52, 41, 33, np.nan, 60],
    "Tenure": [2, 5, 8, 1, 3, 10, 7, np.nan, 4, 12],
    "MonthlyCharges": [50, 75, 90, 45, np.nan, 100, 85, 65, 70, 110],
    "Contract": [
        "Month-to-month", "One year", "Two year", "Month-to-month",
        "One year", "Two year", "Month-to-month", "One year",
        "Month-to-month", "Two year"
    ],
    "Churn": [
        "Yes", "No", "No", "Yes", "No",
        "No", "Yes", "No", "Yes", "No"
    ]
}

df = pd.DataFrame(data)

# Display dataset
print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing numerical values with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Tenure"] = df["Tenure"].fillna(df["Tenure"].mean())
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
    df["MonthlyCharges"].mean()
)

print("\nDataset After Handling Missing Values:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

average_charges = np.mean(df["MonthlyCharges"])
maximum_charges = np.max(df["MonthlyCharges"])
minimum_charges = np.min(df["MonthlyCharges"])

print("\nNumPy Analysis:")
print("Average Monthly Charges:", average_charges)
print("Maximum Monthly Charges:", maximum_charges)
print("Minimum Monthly Charges:", minimum_charges)

churn_count = df["Churn"].value_counts()

print("\nCustomer Churn Count:")
print(churn_count)

plt.figure(figsize=(6, 4))

df["Churn"].value_counts().plot(
    kind="bar"
)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.show()

plt.figure(figsize=(6, 4))

plt.hist(
    df["MonthlyCharges"],
    bins=5,
    edgecolor="black"
)

plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.show()

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"]
)

contract_churn.plot(
    kind="bar",
    figsize=(7, 4)
)

plt.title("Contract Type vs Customer Churn")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=20)
plt.show()

churn_percentage = (
    df["Churn"].value_counts(normalize=True) * 100
)

print("\nChurn Percentage:")
print(churn_percentage)

print("\nEDA Completed Successfully!")
