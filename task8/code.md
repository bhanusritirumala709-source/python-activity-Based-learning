## Problem Statement
Given budget, number of items n, for each item price and quantity.
Calculate total = sum(price * qty).
Read threshold and discount percentage.
If total >= threshold, apply discount: total = total - total*disc_per/100.
Print total, then check budget:
- If total <= budget -> Within Budget
- Else Over Budget and print extra amount needed.

## Algorithm
1. START
2. Read budget, n
3. Set total = 0
4. Loop n times
5.   Read price, qty
6.   total = total + price * qty
7. End Loop
8. Read thresh, disc_per
9. IF total >= thresh THEN total = total - total*disc_per/100
10. Print total as int
11. IF total <= budget THEN Print Within Budget
12. ELSE Print Over Budget and Print total-budget
13. END

## Flowchart
```mermaid
flowchart TD
    A[Start] --> B[Read budget n set total 0]
    B --> C[Loop n items]
    C --> D[Read price qty]
    D --> E[total equal total plus price times qty]
    E --> F{More items}
    F -- Yes --> C
    F -- No --> G[Read thresh disc_per]
    G --> H{Is total greater than or equal to thresh}
    H -- Yes --> I[Apply discount]
    H -- No --> J[Print total]
    I --> J
    J --> K{Is total less than or equal to budget}
    K -- Yes --> L[Print Within Budget]
    K -- No --> M[Print Over Budget and extra]
    L --> N[End]
    M --> N
```

## Sample Input and Output

**Input 1:**
```
1000
2
100
2
200
3
500
10
```

**Output 1:**
```
720
Within Budget
```

**Input 2:**
```
500
1
300
2
400
20
```

**Output 2:**
```
480
Within Budget
```

**Input 3:**
```
400
1
300
2
400
20
```

**Output 3:**
```
480
Over Budget
80
```

