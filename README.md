# Python Fundamentals Assignment

This repository contains Python solutions for two fundamental programming problems focused on conditional logic, user input handling, arithmetic operations, and string formatting (f-strings).

---

## Project Structure

```text
├── student_grade_calculator.py
├── shopping_cart.py
└── README.md
```

---

## 1. Student Grade Calculator (`student_grade_calculator.py`)

A Python program that calculates a student's total marks, average score, and corresponding grade across three subjects.

### Features
- Takes student name and scores for 3 subjects.
- Computes total marks and average marks.
- Formats average marks to 2 decimal places.
- Assigns grades based on predefined thresholds:
  - **80 – 100:** `A+`
  - **70 – 79:** `A`
  - **60 – 69:** `B`
  - **50 – 59:** `C`
  - **Below 50:** `F`

### Sample Output
```text
Student Name: Rahim
Total Marks: 245
Average: 81.67
Grade: A+
```

---

## 2. Simple Shopping Cart (`shopping_cart.py`)

A Python program that simulates a retail checkout process by calculating item subtotals, applying tiered discount logic, and generating an itemized receipt.

### Features
- Takes customer name along with names and prices of 3 products.
- Computes the subtotal of purchased items.
- Determines the discount rate based on tiered spending tiers:
  - **5000 Tk or above:** 20% discount
  - **3000 – 4999 Tk:** 10% discount
  - **1000 – 2999 Tk:** 5% discount
  - **Below 1000 Tk:** No discount
- Computes final payable amount using:
  - Discount = Subtotal * Discount Rate
  - Final Total = Subtotal - Discount

### Sample Output
```text
Customer Name: Rahim
Product 1: Keyboard
Price: 1500
Product 2: Mouse
Price: 800
Product 3: Headphone
Price: 2000
Subtotal: 4300
Discount: 430
Final Total: 3870
```

---

## How to Run

Clone the repository and run the scripts using Python 3:

```bash
# Clone the repository
git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git

# Navigate into the project folder
cd <your-repo-name>

# Run Problem 1
python student_grade_calculator.py

# Run Problem 2
python shopping_cart.py
```