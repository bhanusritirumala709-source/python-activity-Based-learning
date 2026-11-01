**Problem:** Check subject min, aggregate cutoff, rank with tie-break maths.

**Algorithm:** 1.Read c min cutoff 2.Check each subject>=min 3.agg>=cutoff eligible 4.Sort desc agg, maths

**Flowchart:**
```mermaid
flowchart TD
    A[Start] --> B[Read total candidates and min and cutoff]
    B --> C[Initialize eligible list]
    C --> D{Is i less than c?}
    D -- Yes --> E[Read name m p ch]
    E --> F{Any subject less than min?}
    F -- Yes --> G[Increment i]
    F -- No --> H[Calculate agg = m + p + ch]
    H --> I{Is agg greater than cutoff?}
    I -- Yes --> J[Add to eligible list]
    I -- No --> G
    J --> G
    G --> D
    D -- No --> K[Sort by agg desc and maths desc]
    K --> L[Print ranked list]
    L --> M[End]
```
Sample Input 1:
3
40
180
Aman
80
70
60
Riya
90
85
80
Karan
50
40
30

Sample Output 1:
Riya 255
Aman 210
