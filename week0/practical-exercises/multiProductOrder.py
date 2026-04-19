# exercise3.py - Practice: Multiple parameters, scope, return values

def calculate_product_total(name, price, quantity, discount=0):
    """
    Calculate total for a single product line
    
    Args:
        name: Product name
        price: Unit price
        quantity: Number of items
        discount: Discount percentage (default 0)
    
    Returns:
        Dictionary with product details and total
    """
    subtotal = price * quantity
    discount_amount = subtotal * (discount / 100)
    total = subtotal - discount_amount
    
    return {
        "name": name,
        "price": price,
        "quantity": quantity,
        "subtotal": subtotal,
        "discount_percent": discount,
        "discount_amount": discount_amount,
        "total": total
    }


def print_line_item(item):
    """Print a formatted line item"""
    print(f"{item['name']:<20} {item['quantity']:>3} x ₹{item['price']:>8,.2f} = ₹{item['subtotal']:>10,.2f}")
    if item['discount_percent'] > 0:
        print(f"{'':>20} Discount ({item['discount_percent']}%): -₹{item['discount_amount']:>10,.2f}")
    print(f"{'':>20} {'Line Total:':>20} ₹{item['total']:>10,.2f}")


def main():
    print("=== E-COMMERCE ORDER CALCULATOR ===\n")
    
    # Create order with multiple products
    product1 = calculate_product_total("Laptop", 55000, 1, 10)
    product2 = calculate_product_total("Mouse", 500, 2, 5)
    product3 = calculate_product_total("Keyboard", 1500, 1, 0)
    
    # Display order
    print("ORDER DETAILS")
    print("-" * 60)
    
    print_line_item(product1)
    print_line_item(product2)
    print_line_item(product3)
    
    # Calculate order total
    order_total = product1['total'] + product2['total'] + product3['total']
    
    print("-" * 60)
    print(f"{'ORDER TOTAL:':>48} ₹{order_total:>10,.2f}")
    print("=" * 60)


main()