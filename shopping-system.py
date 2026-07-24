store_password = "9821"

while True:
    login = input("Enter admin password: ")

    if login == store_password:
        print("\nLogin Successful!")
        break

    print("Incorrect password. Try again.")

print("\n===== Welcome to Imtiaz Store =====")
print("Sale on Every Item!")

customer_name = input("\nEnter Customer Name: ")

products = {
    "iphone17": 1500,
    "samsung s26 ultra": 1800,
    "reno4": 1200,
    "vivo v4 plus": 1000
}

print("\nAvailable Products:")
for product, price in products.items():
    print(f"- {product.title()} : Rs {price}")

selected_product = input("\nEnter product name: ").lower()

while selected_product not in products:
    print("Product not found.")
    selected_product = input("Enter product name again: ").lower()

quantity = int(input("Enter quantity: "))

while quantity <= 0:
    print("Quantity must be greater than 0.")
    quantity = int(input("Enter quantity: "))

price = products[selected_product]
subtotal = price * quantity

discount = subtotal * 0.10
total = subtotal - discount

print("\n===== ORDER SUMMARY =====")
print(f"Customer: {customer_name}")
print(f"Product: {selected_product.title()}")
print(f"Unit Price: Rs {price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: Rs {subtotal}")
print(f"Discount (10%): Rs {discount}")
print(f"Total Bill: Rs {total}")

confirm = input("\nConfirm Order? (yes/no): ").lower()

if confirm == "yes":
    print("\nOrder Confirmed Successfully!")
    print("Thank you for shopping at Imtiaz Store.")
else:
    print("\nOrder Cancelled.")