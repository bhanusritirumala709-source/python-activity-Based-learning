**Problem:** Process deposits and withdrawals with limit and balance check.

**Algorithm:**
1. Read bal, limit, n
2. Loop n times read type amt
3. If amt<=0 failed++
4. D->bal+=amt W->check limit & bal

**Flowchart:**
```mermaid
flowchart TD
    A[Start]-->B[Read bal limit n]
    B-->C[i=0 success=0 failed=0]
    C-->D{i<n}
    D--Yes-->E[Read type amt]
    E-->F{amt<=0}
    F--Yes-->G[failed++]
    F--No-->H{type==D}
    H--Yes-->I[bal+=amt success++]
    H--No-->J{amt>limit or amt>bal}
    J--Yes-->G
    J--No-->K[bal-=amt success++]
    G-->L[i++]
    I-->L
    K-->L
    L-->D
    D--No-->M[Print]
    M-->N[End]

```



Sample Input 1:
5000
2000
4
D 1000
W 3000
W 1500
W 500

Sample Output 1:
4000
3
1
