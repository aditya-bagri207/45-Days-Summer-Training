import pandas as pd

data = {
    "Name": ["Aditya", "Rahul", "Aman", "Riya"],
    "Marks": [85, None, 90, None],
    "Age": [21, 20, None, 22]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nMissing Values:")
print(df.isnull())


print("\nAfter fillna(0):")
filled = df.fillna(0)
print(filled)


print("\nAfter dropna():")
dropped_df = df.dropna()
print(dropped_df)