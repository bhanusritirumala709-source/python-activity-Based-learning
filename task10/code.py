v=int(input())
total=0
disq=False
for _ in range(v):
    cat=input()
    off=input()
    rep=input()
    if off=="speed":
        fine=1000
    elif off=="signal":
        fine=1500
    elif off=="drunk":
        fine=5000
        disq=True
    else:
        fine=500
    if rep=="Y":
        fine=fine*2
    total+=fine
if v>=3:
    disq=True
print(total)
print(disq)
