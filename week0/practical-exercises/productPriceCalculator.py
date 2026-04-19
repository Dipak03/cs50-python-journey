# exercise1.py - Practice: def, parameters, return, float

def calculate_final_price(original_price, discount_percent, tax_percent):
    """
    Calculate final price after discount and tax
    
    Args:
        original_price: Product's original price
        discount_percent: Discount percentage (e.g., 10 for 10%)
        tax_percent: Tax percentage (e.g., 18 for 18%)
    
    Returns:
        Final price after discount and tax
    """
    # Apply discount first
    price_after_discount = original_price * (1 - discount_percent / 100)
    
    # Then apply tax
    final_price = price_after_discount * (1 + tax_percent / 100) # Calculate final price after applying tax 
    
    return final_price


# Test your function
def main():
    # Product details
    product = "iPhone 15"
    price = 79900  # ₹79,900
    discount = 16  # 16% off
    tax = 18  # 18% GST
    
    final = calculate_final_price(price, discount, tax)
    
    discount_savings = price * discount / 100
    tax_added = final - (price - discount_savings)

    print(f"Product: {product}")
    print(f"Original Price: ₹{price:,.2f}")
    print(f"Discount: {discount}%")
    print(f"Tax: {tax}%")
    print(f"Final Price: ₹{final:,.2f}")
    print(f"You Save (discount): ₹{discount_savings:,.2f}")
    print(f"Tax Added: ₹{tax_added:,.2f}")
    print(f"Net Difference: ₹{final - price:,.2f}")


main()