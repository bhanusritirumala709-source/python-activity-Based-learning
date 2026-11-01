marks = [
    [80,70,90],
    [60,50,40],
    [90,95,85]
]
row_avg = []
for r in marks:
    row_avg.append(sum(r)/len(r))
col_avg = []
for c in zip(*marks):
    col_avg.append(sum(c)/len(marks))
top_student = row_avg.index(max(row_avg))
low_subject = col_avg.index(min(col_avg))
print("Row-wise Avg:", row_avg)
print("Col-wise Avg:", col_avg)
print("Top Performer Row:", top_student)
print("Low Avg Subject Col:", low_subject)
