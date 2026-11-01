**Problem:** Compare scores, improvement, weak subjects, classify.

**Algorithm:** 1.Read n m 2.Read matrix 3.imp=last-first 4.all<40 weak 5.avg classify

**Flowchart:**
```mermaid
flowchart TD
    A[Start]-->B[Read n m scores]
    B-->C[i=0]
    C-->D{i<n}
    D--Yes-->E[imp=last-first]
    E-->F[Print imp]
    F-->G{all<40}
    G--Yes-->H[Weak]
    G--No-->I[i++]
    H-->I
    I-->D
    D--No-->J[avg]
    J-->K[Classify]
    K-->L[End]
```
Sample Input 1:
2
3
30 35 30
60 70 80

Sample Output 1:
0
Sub0 Weak
10
60.0
First
