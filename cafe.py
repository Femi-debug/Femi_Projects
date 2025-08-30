menu = ["Donut", "Coffee", "Bagel", "Tea"]
stock = {"Donut": 280,
         "Coffee": 330,
         "Bagel": 350,
         "Tea": 450,
         }
price = {"Donut": 2.10,
         "Coffee": 2.30,
         "Bagel":2.40,
         "Tea":2.50,
         }
total_stock = 0
for item in menu:
    total_stock += stock[item] * price[item]

print(f"Total stock worth in the cafe:{total_stock}")