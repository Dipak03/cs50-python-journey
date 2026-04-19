# Week 0 - Functions, Variables

## 📚 Overview
Week 0 introduces the fundamentals of Python programming, covering basic syntax, functions, variables, and user input/output operations. This week focuses on building a strong foundation in Python programming concepts.

## 🎯 Topics Covered
- **Functions**: Understanding built-in functions like `print()` and `input()`
- **Variables**: Creating and using variables to store data
- **Data Types**: Working with integers (`int`), floating-point numbers (`float`), and strings (`str`)
- **Type Conversion**: Converting between different data types
- **String Operations**: String manipulation, concatenation, and formatting
- **Conditional Logic**: Making decisions with `if-elif-else` statements
- **User Input**: Getting and processing user input
- **Comments**: Writing clear code documentation

## 📝 Examples

### Basic Programs
Located in `examples/` directory:

1. **Hello World** (`hello.py`, `hello1.py`)
   - First Python program
   - Using the `print()` function

2. **Data Types**
   - `intExample.py` - Working with integers
   - `floatExample.py` - Handling floating-point numbers
   - `stringExample.py` - String manipulation and operations
   - `float1.py`, `float2.py`, `float3.py` - Advanced float operations

3. **Functions** (`def1.py` through `def4.py`)
   - Creating custom functions
   - Function parameters and return values
   - Code organization and reusability

## 💻 Practical Exercises

### 1. Cart Calculator (`cartCalculator.py`)
A shopping cart calculator that:
- Takes product details (name, quantity, unit price)
- Calculates subtotal
- Adds shipping cost (standard/express)
- Displays a formatted receipt

**Key Concepts**: Input handling, arithmetic operations, conditionals, string formatting

### 2. Commission Calculator (`commissionCalculator.py`)
Calculates sales commission based on sales amount with tiered commission rates.

### 3. Multi-Product Order (`multiProductOrder.py`)
Handles multiple products in a single order with totals calculation.

### 4. Product Price Calculator (`productPriceCalculator.py`)
Advanced price calculation with various pricing rules.

## 🎓 Problem Set 0

### 1. Indoor Voice (`indoor/indoor.py`)
Converts user input to lowercase, simulating an "indoor voice."

### 2. Playback Speed (`playback/playback.py`)
Replaces spaces with "..." to simulate slow speech playback.

### 3. Making Faces (`faces/faces.py`)
- Converts emoticons to emoji
- `:)` → 🙂 (slightly smiling face)
- `:(` → 🙁 (slightly frowning face)

**Functions**: `main()`, `convert()`

### 4. Einstein (`einstein/einstein.py`)
Implements Einstein's mass-energy equivalence formula: **E = mc²**
- Takes mass (kg) as input
- Calculates equivalent energy in Joules
- Uses c = 300,000,000 m/s

**Example**: 
- Input: 1 kg → Output: 90,000,000,000,000,000 Joules

### 5. Tip Calculator (`tip/tip.py`)
Calculates restaurant tip based on meal cost and tip percentage.

**Functions**:
- `dollars_to_float(d)` - Converts "$##.##" to float
- `percent_to_float(p)` - Converts "##%" to float (0.0-1.0)
- `main()` - Main program logic

**Example**:
- Meal: $50.00, Tip: 15% → Leave $7.50

## 🚀 Main Project: Order Processing System

### `week0_project.py`

A comprehensive order management system that demonstrates all Week 0 concepts.

#### Features:
1. **Customer Management**
   - Collect customer name

2. **Multi-Product Support**
   - Add multiple products (name, price, quantity)
   - Calculate individual item subtotals

3. **Dynamic Pricing**
   - **Discount System**:
     - Orders > ₹10,000: 10% discount
     - Orders > ₹5,000: 5% discount
     - Orders < ₹5,000: No discount
   
   - **Shipping Calculation**:
     - Free shipping for orders > ₹5,000
     - ₹100 flat rate for orders < ₹5,000

4. **Tax Calculation**
   - 18% GST on final amount (after discount and shipping)

5. **Professional Receipt**
   - Formatted invoice display
   - Itemized product list
   - Clear breakdown of charges

#### Functions Implemented:
```python
def calculate_order_subtotal(products)  # Calculate total before discounts
def calculate_discount(subtotal)         # Apply tiered discount
def calculate_shipping(subtotal)         # Calculate shipping cost
def calculate_tax(amount)                # Calculate 18% GST
def print_receipt(...)                   # Display formatted invoice
```

#### Sample Output:
```
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
ITEM                          PRICE   QTY       SUBTOTAL
------------------------------------------------------------
Laptop                   ₹45,000.00     2    ₹90,000.00
Mouse                       ₹500.00     3     ₹1,500.00
------------------------------------------------------------
Subtotal:                                     ₹91,500.00
Discount (10%):                               -₹9,150.00
Shipping:                                            FREE
Amount before tax:                            ₹82,350.00
GST (18%):                                    ₹14,823.00
============================================================
TOTAL AMOUNT:                                 ₹97,173.00
============================================================

           Thank you for your business!
============================================================
```

## 🎨 Skills Demonstrated

### Input/Output
- Getting user input with `input()`
- Formatted output with f-strings
- String formatting for currency display

### Data Handling
- Type conversion (`int()`, `float()`, `str()`)
- Working with dictionaries and lists
- Data validation and error handling

### Control Flow
- Conditional statements (if-elif-else)
- While loops for repeated input
- Input validation loops

### Functions
- Creating modular, reusable functions
- Function parameters and return values
- Single responsibility principle

### String Formatting
- F-strings for variable interpolation
- Alignment and padding (`:>`, `:<`)
- Number formatting (`,` for thousands, `.2f` for decimals)

## 📂 Directory Structure
```
week0/
├── README.md                          # This file
├── week0.md                          # Lecture notes
├── examples/                         # Basic examples
│   ├── hello.py, hello1.py
│   ├── intExample.py
│   ├── floatExample.py
│   ├── stringExample.py
│   └── def1.py through def4.py
├── practical-exercises/              # Practice programs
│   ├── cartCalculator.py
│   ├── commissionCalculator.py
│   ├── multiProductOrder.py
│   ├── productPriceCalculator.py
│   └── week0_project.py             # Main project ⭐
└── problemSet0/                      # CS50 problem sets
    ├── einstein/
    ├── faces/
    ├── indoor/
    ├── playback/
    └── tip/
```

## 🏆 Key Achievements
- ✅ Completed 5 CS50 problem sets
- ✅ Built 4 practical exercises
- ✅ Created a full-featured order processing system
- ✅ Mastered basic Python syntax and functions
- ✅ Implemented real-world business logic (discounts, tax, shipping)

## 🔑 Key Takeaways
1. Functions make code reusable and organized
2. Variables store and manage data throughout a program
3. Type conversion is essential for handling user input
4. String formatting creates professional-looking output
5. Breaking problems into smaller functions improves code quality

---

**Next Steps**: Week 1 - Conditionals and Loops (Advanced)
