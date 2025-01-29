col = 5
row = 2*col-1
for i in range(col+1):
    for j in range(col-i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")  
    print()    
for i in range(col-1):
    for j in range(i+1):
        print(" ", end="")    
    for k in range(col-i-1):
        print("*", end="")
    print()    
