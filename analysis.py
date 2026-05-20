import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Karan", "Sneha"],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("Student Data")
print(df)

average = df["Marks"].mean()

print("Average Marks:", average)

highest = df["Marks"].max()

print("Highest Marks:", highest)

print("Data Science Team Project")