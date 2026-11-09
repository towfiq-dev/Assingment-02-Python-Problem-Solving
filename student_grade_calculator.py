student_name = input("Enter your name ")

bangla = int(input("Bangla Marks: "))
english = int(input("English Marks: "))
math = int(input("Math Marks: "))

# Calculation
total_marks = (bangla + english + math)
average_marks = total_marks/3

# Grade Conditions:
if average_marks <=100 and average_marks >= 80:
  GPA = "A+"
elif average_marks >=70 and average_marks < 80:
  GPA = "A"
elif average_marks >=60 and average_marks < 70:
  GPA = "B"
elif average_marks >=50 and average_marks < 60:
  GPA = "C"
else:
  GPA = "F"
  
# Display Output
print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Average: {average_marks:.2f}")
print(f"GPA: {GPA}")