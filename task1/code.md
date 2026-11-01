**Problem:** Fine by offence type, double if repeat, disqualify if >=3 or drunk.

**Algorithm:** 1.Read v 2.Get base fine 3.If rep Y double 4.Sum 5.Check disq

**Flowchart:**
```mermaid
flowchart TD
    A[Start]-->B[Read v total=0 disq=False i=0]
    B-->C{i<v}
    C--Yes-->D[Read cat off rep]
    D-->E[Get base fine]
    E-->F{rep==Y}
    F--Yes-->G[fine=fine*2]
    F--No-->H[total+=fine]
    G-->H
    H-->I[Check disq]
    I-->J[i++]
    J-->C
    C--No-->K[Print total disq]
    K-->L[End]
```
Sample Input 1:
2
4W
speed
N
2W
signal
Y

Sample Output 1:
4000
False

Sample Input 2 (Disqualify):
3
4W
drunk
N
2W
speed
Y
4W
signal
N

Sample Output 2:
8500
True
