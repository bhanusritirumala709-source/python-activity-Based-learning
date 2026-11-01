capacity=int(input())
level=int(input())
threshold=int(input())
days=int(input())
first=-1
for d in range(1,days+1):
    inflow=int(input())
    outflow=int(input())
    level=level+inflow-outflow
    if level>capacity:
        print(f"Day {d} Overflow")
        level=capacity
    if level<0:
        print(f"Day {d} Shortage")
        level=0
    if level>=threshold and first==-1:
        first=d
print(level)
print(first)
