# exercise4.py - Practice: Nested functions, return values, operators

def calculate_commission(sales_amount):
    """
    Calculate sales commission using progressive tiers
    
    Progressive Tiers (applied to each bracket):
    - First ₹50,000: 5%
    - Next ₹50,000 (₹50,001-₹100,000): 7%
    - Above ₹100,000: 10%
    """
    if sales_amount <= 50000:
        commission = sales_amount * 0.05
        rate = 5
    elif sales_amount <= 100000:
        # First 50k at 5%, remainder at 7%
        commission = (50000 * 0.05) + ((sales_amount - 50000) * 0.07)
        rate = 7
    else:
        # First 50k at 5%, next 50k at 7%, remainder at 10%
        commission = (50000 * 0.05) + (50000 * 0.07) + ((sales_amount - 100000) * 0.10)
        rate = 10
    
    return commission, rate  # Return commission amount and highest tier rate


def calculate_net_earnings(sales, base_salary=15000):
    """Calculate total earnings"""
    commission, commission_rate = calculate_commission(sales)
    total = base_salary + commission
    
    return {
        "base_salary": base_salary,
        "sales": sales,
        "commission_rate": commission_rate,
        "commission": commission,
        "total_earnings": total
    }


def main():
    print("=== SALES PERFORMANCE CALCULATOR ===\n")
    
    # Get sales data
    monthly_sales = float(input("Enter monthly sales (₹): "))
    
    # Calculate earnings
    earnings = calculate_net_earnings(monthly_sales)
    
    # Display results
    print("\n" + "="*50)
    print("MONTHLY EARNINGS BREAKDOWN")
    print("="*50)
    print(f"Base Salary:        ₹{earnings['base_salary']:>15,.2f}")
    print(f"Total Sales:        ₹{earnings['sales']:>15,.2f}")
    print(f"Commission Rate:     {earnings['commission_rate']:>14.0f}%")
    print(f"Commission:         ₹{earnings['commission']:>15,.2f}")
    print("-"*50)
    print(f"TOTAL EARNINGS:     ₹{earnings['total_earnings']:>15,.2f}")
    print("="*50)
    
    # Performance feedback
    if earnings['sales'] >= 100000:
        print("\n🎉 Excellent! Top performer!")
    elif earnings['sales'] >= 50000:
        print("\n👍 Good job! Keep it up!")
    else:
        print("\n💪 Push harder next month!")


main()