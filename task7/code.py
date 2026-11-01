dist=int(input())
price=int(input())
v=int(input())
min_cost=9999999
min_idx=-1
for i in range(v):
    mileage=float(input())
    tank=float(input())
    reserve=float(input())
    fuel=dist/mileage
    need=fuel+reserve
    cost=fuel*price
    feasible=need<=tank
    print(f"{fuel:.2f} {cost:.2f} {feasible}")
    if feasible and cost<min_cost:
        min_cost=cost
        min_idx=i
print(min_idx)
