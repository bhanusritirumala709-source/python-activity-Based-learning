n=int(input())
m=int(input())
scores=[]
for _ in range(n):
    row=list(map(int,input().split()))
    scores.append(row)
for i in range(n):
    imp=scores[i][-1]-scores[i][0]
    print(imp)
    weak=True
    for s in scores[i]:
        if s>=40:
            weak=False
    if weak:
        print(f"Sub{i} Weak")
avg=sum([sum(r)/m for r in scores])/n
if avg>=75:
    print("Distinction")
elif avg>=60:
    print("First")
elif avg>=40:
    print("Pass")
else:
    print("Fail")
