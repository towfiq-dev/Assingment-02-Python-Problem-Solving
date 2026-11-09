# Input:
customer_name = input("Enter your name: ")
product_1 = input("Enter your Product_1 name: ")
price_1 = int(input("Enter your Price_1: "))
product_2 = input("Enter your Product_2 name: ")
price_2 = int(input("Enter your Price_2: "))
product_3 = input("Enter your Product_3 name: ")
price_3 = int(input("Enter your Price_3: "))

# Subtotal:
subtotal = price_1 + price_2 + price_3

# Discount Conditions:
if subtotal >= 5000:
    discount_rate = 20 / 100
elif subtotal >= 3000 and subtotal < 5000:
    discount_rate = 10 / 100
elif subtotal >= 1000 and subtotal < 3000:
    discount_rate = 5 / 100
else:
    discount_rate = 0 / 100

discount = int(subtotal * discount_rate)
final_total = int(subtotal - discount)

# Output:
print(f"Customer Name: {customer_name}")
print(f"Product 1: {product_1}")
print(f"Price: {price_1}")
print(f"Product 2: {product_2}")
print(f"Price: {price_2}")
print(f"Product 3: {product_3}")
print(f"Price: {price_3}")
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"Final Total: {final_total}")