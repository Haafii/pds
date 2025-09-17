import random



customers = [
    ("C001", 500, 650),
    ("C002", 800, 1050),
    ("C003", 300, 450),
    ("C004", 1500, 2000),
    ("C005", 1200, 1600),
    ("C006", 700, 900),
    ("C007", 250, 400),
    ("C008", 1100, 1500),
    ("C009", 600, 850),
    ("C010", 950, 1300)
]

# Process each customer
for pid, cost_price, selling_price in customers:
    discount_percent = random.randint(5, 10)

    # Using formulas
    discount = (discount_percent / 100) * selling_price
    final_sp = selling_price - discount
    profit = final_sp - cost_price

    print(f"{pid} profit with discount is {profit:.2f}")
