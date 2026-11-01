**Problem:** Calculate hours from entry exit, rate by vehicle, overnight charge, cap.

**Algorithm:** 1.Validate time 2.If exit<entry hours=24-entry+exit else exit-entry 3.fee=hours*rate+overnight 4.cap 500

**Flowchart:**
```mermaid
flowchart TD
    A[Start]-->B[Read entry exit vtype]
    B-->C{invalid}
    C--Yes-->D[Invalid]
    D-->Z[End]
    C--No-->E{exit<entry}
    E--Yes-->F[hours=24-entry+exit overnight=100]
    E--No-->G[hours=exit-entry overnight=0]
    F-->H[rate]
    G-->H
    H-->I[fee=hours*rate+overnight]
    I-->J{fee>500}
    J--Yes-->K[fee=500]
    J--No-->L[Print]
    K-->L
    L-->Z
```
Sample Input 1:
9
15
4W

Sample Output 1:
6
240

Sample Input 2 (Overnight):
20
5
2W

Sample Output 2:
9
280
