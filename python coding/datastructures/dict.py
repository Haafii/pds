#Dictionary practise
#1. Average Temperature (Last 3 Days)
temps = {
"Day1": [30, 32, 31, 29, 33],
"Day2": [28, 27, 29, 30, 28],
"Day3": [31, 30, 32, 33, 31]
}
for day in temps:
    avg = sum(temps[day]) / len(temps[day])
    print(day, "Average:", avg)
#2. Best Rating & Lowest Price (Amazon Products)
products = {
"P001": {"rating": 4.5, "price": 1200},
"P002": {"rating": 4.8, "price": 1500},
"P003": {"rating": 4.2, "price": 900},
"P004": {"rating": 4.9, "price": 2000}
}
best = max(products, key=lambda x: products[x]["rating"])
cheap = min(products, key=lambda x: products[x]["price"])
print("Best Rated:", best, products[best])
print("Lowest Price:", cheap, products[cheap])
#Do you want me to also make the tuple questions in the same short-and-simple style? That way
#they’ll all be consistent.