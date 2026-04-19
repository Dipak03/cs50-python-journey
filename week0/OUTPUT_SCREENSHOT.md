# Week 0 Project - Output Screenshot

## Program Execution: Order Processing System

### Input Provided:
- **Customer Name**: John Doe
- **Product 1**: Laptop - ₹45,000 × 2 units
- **Product 2**: Mouse - ₹500 × 3 units

---

### Complete Terminal Output:

```
PS D:\Study\Python\cs50-python-journey> cd week0/practical-exercises; python week0_project.py
============================================================
         WELCOME TO ORDER PROCESSING SYSTEM
============================================================

Enter customer name: John Doe

Enter product details (type 'done' when finished):

Enter product name (or 'done' to finish): Laptop
Enter price for Laptop (₹): 45000
Enter quantity for Laptop: 2

Enter product name (or 'done' to finish): Mouse
Enter price for Mouse (₹): 500
Enter quantity for Mouse: 3

Enter product name (or 'done' to finish): done

============================================================
                     INVOICE
============================================================
Customer: John Doe
------------------------------------------------------------
ITEM                           PRICE   QTY        SUBTOTAL
------------------------------------------------------------
Laptop                    ₹45,000.00     2 ₹     90,000.00
Mouse                     ₹   500.00     3 ₹      1,500.00
------------------------------------------------------------
Subtotal:                                     ₹     91,500.00
Discount (10%):                               -₹     9,150.00
Shipping:                                                FREE
Amount before tax:                            ₹     82,350.00
GST (18%):                                    ₹     14,823.00
============================================================
TOTAL AMOUNT:                                 ₹     97,173.00
============================================================

           Thank you for your business!
============================================================
```

---

## Calculations Breakdown:

### 1. Subtotal Calculation
- Laptop: ₹45,000 × 2 = ₹90,000.00
- Mouse: ₹500 × 3 = ₹1,500.00
- **Subtotal**: ₹91,500.00

### 2. Discount Applied
- Order value > ₹10,000 → **10% discount**
- Discount amount: ₹91,500 × 0.10 = ₹9,150.00
- Amount after discount: ₹91,500 - ₹9,150 = ₹82,350.00

### 3. Shipping Calculation
- Order value > ₹5,000 → **FREE shipping**
- Shipping cost: ₹0

### 4. Tax Calculation (GST)
- Amount before tax: ₹82,350.00
- GST (18%): ₹82,350 × 0.18 = ₹14,823.00

### 5. Final Total
- **Grand Total**: ₹82,350 + ₹14,823 = ₹97,173.00

---

## Features Demonstrated:

✅ **Multi-product support** - Handled 2 different products  
✅ **Dynamic pricing** - Applied 10% discount for order > ₹10,000  
✅ **Free shipping** - Automatically applied for order > ₹5,000  
✅ **Tax calculation** - Calculated 18% GST on final amount  
✅ **Professional formatting** - Clean, aligned receipt display  
✅ **Input validation** - Accepted 'done' to finish product entry  
✅ **Modular functions** - Separate functions for each calculation  

---

## Technical Highlights:

- **String Formatting**: Used f-strings with alignment (`:>`, `:<`) and number formatting (`:,.2f`)
- **Data Structures**: Stored products in a list of dictionaries
- **Control Flow**: While loop for multiple product entry, conditional logic for discounts/shipping
- **Type Conversion**: Converted user input from strings to int/float
- **Function Design**: Single responsibility - each function handles one calculation
- **Edge Cases**: Handles orders at different price thresholds (₹5K, ₹10K)

---

**Program File**: [week0_project.py](week0/practical-exercises/week0_project.py)  
**Date**: April 20, 2026  
**Status**: ✅ Successfully Completed
