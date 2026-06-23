import pandas as pd

df1 = pd.DataFrame({
    "StudentID": [101, 102, 103, 104],
    "Name": ["Aditya", "Rahul", "Aman", "Riya"],
    "Department": ["CSE", "IT", "DS", "ECE"]
})
print("First data frame: ")
print(df1)

df2 = pd.DataFrame({
    "StudentID": [101, 102, 103, 104],
    "Marks": [92, 75, 88, 65],
    "Grade": ["A", "B", "A", "C"]
})
print("Second data frame: ")
print(df2)

merged_df = pd.merge(df1, df2, on="StudentID")

print("Merged DataFrame:")
print(merged_df)

print("\nStudents with Grade A:")
print(merged_df[merged_df["Grade"] == "A"])