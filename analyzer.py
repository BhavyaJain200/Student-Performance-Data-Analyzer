# cd "C:\Users\aanit\OneDrive\Desktop\PYTHON\Project\Student Performace Analyzer"
# python analyzer.py
import pandas as pd

file_path = "Student_performance_data.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

print("\n📊 GPA Statistics")
print("Average GPA:", round(df["GPA"].mean(), 2))
print("Highest GPA:", df["GPA"].max())
print("Lowest GPA:", df["GPA"].min())

top_student = df.loc[df["GPA"].idxmax()]
low_student = df.loc[df["GPA"].idxmin()]

print("\n🏆 Top Performer")
print(top_student[["StudentID", "GPA"]])

print("\n⚠️ Lowest Performer")
print(low_student[["StudentID", "GPA"]])

print("\n📈 Average GPA by Weekly Study Time")
study_gpa = df.groupby("StudyTimeWeekly")["GPA"].mean()
print(study_gpa)

