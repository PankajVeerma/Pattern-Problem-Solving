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