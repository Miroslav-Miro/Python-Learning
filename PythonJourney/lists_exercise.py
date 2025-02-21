sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales_w2.append(int(input("Enter the sales for the 7th day of week 2: ")))
sales = sales_w1 + sales_w2


most_lemonade_sold_day = float(max(sales))
print(f"The most profit in a day was {most_lemonade_sold_day * 1.50}$")

least_lemonade_sold_day = float(min(sales))
print(f"The least profit in a day was {least_lemonade_sold_day * 1.50}$")

sales_w1_total = float(sum(sales_w1))
sales_w2_total = float(sum(sales_w2))

print(f"The total profit for week 1 was {sales_w1_total * 1.50}$ for the week 2 was {sales_w2_total * 1.50}$, in total {(sales_w1_total * 1.50) + ( sales_w2_total*1.50)}$")