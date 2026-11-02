bal=int(input())
limit=int(input())
n=int(input())
success=0
failed=0
for _ in range(n):
    t=input().split()
    typ=t[0]
    amt=int(t[1])
    if amt<=0:
        failed+=1
        continue
    if typ=="D":
        bal+=amt
        success+=1
    elif typ=="W":
        if amt>limit or amt>bal:
            failed+=1
        else:
            bal-=amt
            success+=1
print(bal)
print(success)
print(failed)
