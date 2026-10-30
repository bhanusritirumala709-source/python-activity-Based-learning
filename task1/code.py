classrooms = [
    [1,0,2,0,1],  #Room1: 0=vacant, 1=student, 2=reserved
    [2,1,1,0,0],  #Room2
    [1,1,0,2,0]   #Room3
]

print("CLASSROOM REPORT")
for i in range(len(classrooms)):
    vacant=reserved=students=0
    seen=[]
    for seat in classrooms[i]:
        if seat==0: vacant+=1
        elif seat==2: reserved+=1
        elif seat==1: 
            if 1 in seen: print(f"Room{i+1}: Duplicate found")
            seen.append(1)
            students+=1
    
    total=len(classrooms[i])
    print(f"Room{i+1}: Vacant={vacant} Reserved={reserved} Students={students}")
   
