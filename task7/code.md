**Problem:** fuel=dist/mileage, cost=fuel*price, feasible check with reserve.

**Algorithm:** 1.Read dist price v 2.fuel calc 3.need=fuel+reserve 4.feasible=need<=tank 5.Track min cost

**Flowchart:**
```mermaid
flowchart TD
    A[Start]-->B[Read dist price v]
    B-->C[min_cost=INF min_idx=-1 i=0]
    C-->D{i<v}
    D--Yes-->E[Read mileage tank reserve]
    E-->F[fuel=dist/mileage]
    F-->G[need=fuel+reserve cost=fuel*price]
    G-->H{need<=tank}
    H--Yes-->I[feasible True]
    H--No-->J[feasible False]
    I-->K{cost<min_cost}
    J-->K
    K--Yes-->L[Update min]
    K--No-->M[i++]
    L-->M
    M-->D
    D--No-->N[Print min_idx]
    N-->O[End]
```
Sample Input 1:
100
100
2
10
15
2
20
10
1

Sample Output 1:
10.00 1000.00 True
5.00 500.00 True
1
