entry=int(input())
exit_=int(input())
vtype=input()
if entry<0 or entry>23 or exit_<0 or exit_>23:
    print("Invalid")
else:
    if vtype=="2W":
        rate=20
    elif vtype=="4W":
        rate=40
    else:
        rate=60
    if exit_<entry:
        hours=(24-entry)+exit_
        overnight=100
    else:
        hours=exit_-entry
        overnight=0
    fee=hours*rate+overnight
    if fee>500:
        fee=500
    print(hours)
    print(fee)
