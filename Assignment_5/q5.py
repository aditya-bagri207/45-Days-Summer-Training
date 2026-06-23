import pandas as pd

data = {
    "Name": ["Aditya", "Rahul", "Aman", "Riya", "Kriti",
             "Neha", "Rohit", "Priya", "Vikas", "Simran"],

    "Age": [21, 20, 22, 21, 20,
            19, 22, 21, 20, 19],

    "Marks": [85, 72, 91, 67, 88,
              79, 95, 70, 82, 76],

    "City": ["Pilani", "Jaipur", "Delhi", "Mumbai", "Pune",
             "Ajmer", "Kota", "Delhi", "Jaipur", "Udaipur"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nFirst 5 Rows:")
print(df.head())     #default it print only 5 rows

print("\nStatistics:")
print(df.describe())

print("\nStudents Scoring More Than 75:")
print(df[df["Marks"] > 75])

print("\nSorted by Marks (Descending):")
print(df.sort_values(by="Marks", ascending=False))