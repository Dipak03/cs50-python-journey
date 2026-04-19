# exercise2.py - Practice: input(), int(), float(), str operations

def main():
    # Get product details from user
    print("=== SHOPPING CART CALCULATOR ===\n")
    
    product_name = input("Product name: ")
    quantity = int(input("Quantity: "))
    unit_price = float(input("Unit price (₹): "))
    
    # Calculate subtotal
    subtotal = quantity * unit_price
    
    # Ask about shipping
    shipping_method = input("Shipping (standard/express): ").lower()
    
    # Calculate shipping cost based on method
    if shipping_method == "express":
        shipping = 200
        display_method = "express"
    elif shipping_method == "standard":
        shipping = 100
        display_method = "standard"
    else:
        # Default to standard but inform user
        shipping = 100
        display_method = "standard"
        print(f"Invalid shipping method. Defaulting to standard.")
    
    # Calculate total
    total = subtotal + shipping
    
    # Display receipt
    print("\n" + "="*40)
    print("RECEIPT")
    print("="*40)
    print(f"Product: {product_name}")
    print(f"Quantity: {quantity}")
    print(f"Unit Price: ₹{unit_price:.2f}")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Shipping ({display_method}): ₹{shipping:.2f}")
    print("-"*40)
    print(f"TOTAL: ₹{total:.2f}")
    print("="*40)


main()
