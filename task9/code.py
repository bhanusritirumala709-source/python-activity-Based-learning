c=int(input())
min_sub=int(input())
cutoff=int(input())
eligible=[]
for _ in range(c):
    name=input()
    m=int(input())
    p=int(input())
    ch=int(input())
    if m<min_sub or p<min_sub or ch<min_sub:
        continue
    agg=m+p+ch
    if agg>=cutoff:
        eligible.append((name,agg,m))
eligible.sort(key=lambda x: (-x[1],-x[2]))
for e in eligible:
    print(e[0],e[1])
