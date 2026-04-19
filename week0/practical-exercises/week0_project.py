# week0_project.py
# Build a complete order processing system with these features:

def main():
    """
    Your system should:
    1. Take customer name
    2. Accept multiple products (name, price, quantity)
    3. Calculate subtotal for each product
    4. Apply discount based on order value:
       - Orders > ₹10,000: 10% discount
       - Orders > ₹5,000: 5% discount
       - Orders < ₹5,000: No discount
    5. Calculate shipping:
       - Free shipping for orders > ₹5,000
       - ₹100 for orders < ₹5,000
    6. Calculate 18% GST on final amount
    7. Display beautiful receipt
    
    Use separate functions for each calculation!
    """
    print("="*60)
    print("         WELCOME TO ORDER PROCESSING SYSTEM")
    print("="*60)
    print()
    
    # Ask for customer name
    customer_name = input("Enter customer name: ").strip()
    print()
    
    # Collect products
    products = []
    print("Enter product details (type 'done' when finished):")
    while True:
        product_name = input("\nEnter product name (or 'done' to finish): ").strip()
        if product_name.lower() == 'done':
            break
        price = float(input(f"Enter price for {product_name} (₹): "))
        
        # Get quantity
        while True:
            try:
                quantity_input = input(f"Enter quantity for {product_name}: ").strip()
                if quantity_input:
                    quantity = int(quantity_input)
                    if quantity > 0:
                        break
                    else:
                        print("Quantity must be greater than 0. Please try again.")
                else:
                    print("Quantity cannot be empty. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Calculate item subtotal
        item_subtotal = price * quantity
        products.append({
            "name": product_name,
            "price": price,
            "quantity": quantity,
            "subtotal": item_subtotal
        })
    
    # Calculate totals
    subtotal = calculate_order_subtotal(products)
    discount = calculate_discount(subtotal)
    shipping = calculate_shipping(subtotal)
    
    # Calculate amount after discount and shipping
    amount_after_discount = subtotal - discount + shipping
    
    # Calculate GST on final amount
    tax = calculate_tax(amount_after_discount)
    
    # Calculate grand total
    total = amount_after_discount + tax
    
    # Print receipt
    print_receipt(customer_name, products, subtotal, discount, shipping, tax, total)


# Write helper functions here:
def calculate_order_subtotal(products):
    """Calculate total before discounts"""
    total = 0
    for product in products:
        total += product["subtotal"]
    return total


def calculate_discount(subtotal):
    """Return discount amount based on order value"""
    if subtotal > 10000:
        discount_rate = 0.10
    elif subtotal > 5000:
        discount_rate = 0.05
    else:
        discount_rate = 0.00
    
    return subtotal * discount_rate


def calculate_shipping(subtotal):
    """Return shipping cost"""
    if subtotal > 5000:
        return 0  # Free shipping
    else:
        return 100


def calculate_tax(amount):
    """Calculate 18% GST"""
    return amount * 0.18


def print_receipt(customer, products, subtotal, discount, shipping, tax, total):
    """Print formatted receipt"""
    print("\n" + "="*60)
    print("                     INVOICE")
    print("="*60)
    print(f"Customer: {customer}")
    print("-"*60)
    print(f"{'ITEM':<25} {'PRICE':>10} {'QTY':>5} {'SUBTOTAL':>15}")
    print("-"*60)
    
    # Print each product
    for product in products:
        print(f"{product['name']:<25} ₹{product['price']:>9,.2f} {product['quantity']:>5} ₹{product['subtotal']:>14,.2f}")
    
    print("-"*60)
    print(f"{'Subtotal:':<45} ₹{subtotal:>14,.2f}")
    
    if discount > 0:
        discount_percent = (discount / subtotal) * 100
        print(f"{'Discount (' + str(int(discount_percent)) + '%):':<45} -₹{discount:>13,.2f}")
    
    if shipping > 0:
        print(f"{'Shipping:':<45} ₹{shipping:>14,.2f}")
    else:
        print(f"{'Shipping:':<45} {'FREE':>15}")
    
    amount_before_tax = subtotal - discount + shipping
    print(f"{'Amount before tax:':<45} ₹{amount_before_tax:>14,.2f}")
    print(f"{'GST (18%):':<45} ₹{tax:>14,.2f}")
    print("="*60)
    print(f"{'TOTAL AMOUNT:':<45} ₹{total:>14,.2f}")
    print("="*60)
    print("\n           Thank you for your business!")
    print("="*60)


main()