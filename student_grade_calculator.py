student_name = input("Enter your name: ")

bangla = int(input("Bangla Marks: "))
english = int(input("English Marks: "))
math = int(input("Math Marks: "))

# Calculation
total_marks = (bangla + english + math)
average_marks = total_marks/3
# Validation: Check if marks are between 0 and 100
if (bangla < 0 or bangla > 100) or (english < 0 or english > 100) or (math < 0 or math > 100):
    print("Invalid marks! Marks must be between 0 and 100.")
else:
  # Grade Conditions:
  if average_marks <=100 and average_marks >= 80:
    Grade = "A+"
  elif average_marks >=70 and average_marks < 80:
    Grade = "A"
  elif average_marks >=60 and average_marks < 70:
    Grade = "B"
  elif average_marks >=50 and average_marks < 60:
    Grade = "C"
  else:
    Grade = "F"
  
  # Display Output
  print(f"Student Name: {student_name}")
  print(f"Total Marks: {total_marks}")
  print(f"Average: {average_marks:.2f}")
  print(f"Grade: {Grade}")