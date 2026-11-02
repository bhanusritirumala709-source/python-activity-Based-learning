total = int(input())
attended = int(input())
threshold = float(input())
current = attended / total * 100
if current >= threshold:
    req = 0
else:
    req = math.ceil((threshold/100*total - attended) / (1 - threshold/100))
print(f"{current:.2f}")
print(req)
