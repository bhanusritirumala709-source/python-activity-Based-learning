**Problem:** Update level, detect overflow shortage, first day reaching threshold.

**Algorithm:** 1.Read capacity level threshold days 2.Loop update level 3.Check overflow shortage 4.Track first threshold

**Flowchart:**
```mermaid
flowchart TD
    A[Start]-->B[Read capacity level threshold days]
    B-->C[first=-1 d=1]
    C-->D{d<=days}
    D--Yes-->E[Read inflow outflow]
    E-->F[level=level+inflow-outflow]
    F-->G{level>capacity}
    G--Yes-->H[Overflow level=capacity]
    G--No-->I{level<0}
    H-->I
    I--Yes-->J[Shortage level=0]
    I--No-->K{level>=threshold and first==-1}
    J-->K
    K--Yes-->L[first=d]
    K--No-->M[d++]
    L-->M
    M-->D
    D--No-->N[Print level first]
    N-->O[End]
```
Sample Input 1:
1000
200
600
3
500
100
300
200
100
300

Sample Output 1:
Day 1 Overflow
400
1

Sample Input 2:
1000
200
600
2
500
100
300
200

Sample Output 2:
600
2
