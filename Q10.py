col = 5
row = int(input("Enter the number of number of row "))
#          *
#          * * 
#          * * *
#          * * * *
#          * * * * *
#          * * * * * *
#          * * * * * 
#          * * * *
#          * * *
#          * *
#          *


for i in range(1,row+1):
  for j in range(1,i+1):
    print("*",end=" ")
  print(" ")
for j in range(row-1,0,-1):
  for i in range(1,j+1):
    print("*",end=" ")
  print(" ")
  
  
  
  # OR

for i in  range(col+1):
  for j in range(i):
    print("*", end=" ")
  print()  
for i in  range(col+1):  
  for k in range((col-i)-1):
    print("*", end=" ")
  print()
     