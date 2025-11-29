import sys

# Check number of arguments (script name + 4 arguments = 5)
if len(sys.argv) != 5:
    print("Error: Missing arguments!")
    print("Usage: python Billing_receipt.py <item name> <quantity> <price per unit> <discount>")
    sys.exit(1)

item_name = sys.argv[1]
quantity = int(sys.argv[2])
price_per_unit = float(sys.argv[3])
discount = float(sys.argv[4])   # discount in percentage

# Calculate total
subtotal = quantity * price_per_unit

# Apply discount
discount_amount = subtotal * (discount / 100)
total = subtotal - discount_amount

# Print receipt
print("\n===== Billing Receipt =====")
print(f"Item Name     : {item_name}")
print(f"Quantity      : {quantity}")
print(f"Price/Unit    : {price_per_unit:.2f}")
print(f"Subtotal      : {subtotal:.2f}")
print(f"Discount      : {discount_amount:.2f}")
print(f"Total         : {total:.2f}")
