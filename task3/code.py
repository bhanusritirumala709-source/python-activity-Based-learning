p=int(input())
for _ in range(p):
    name=input()
    opening=int(input())
    incoming=int(input())
    dispatched=int(input())
    closing=int(input())
    min_stock=int(input())
    expected=opening+incoming-dispatched
    disc=closing-expected
    rep=0
    if closing<min_stock:
        rep=min_stock-closing
    print(name,expected,disc,rep)
