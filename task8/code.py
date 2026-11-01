budget=int(input())
n=int(input())
total=0
for _ in range(n):
    price=int(input())
    qty=int(input())
    total+=price*qty
thresh=int(input())
disc_per=int(input())
if total>=thresh:
    total=total-total*disc_per/100
print(int(total))
if total<=budget:
    print("Within Budget")
else:
    print("Over Budget")
    print(int(total-budget))
