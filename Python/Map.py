CostCo = [10.00, 11.00, 12.34, 2.34]
Sams = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, CostCo, Sams)

for item in cheapest:
    print(item)
    
