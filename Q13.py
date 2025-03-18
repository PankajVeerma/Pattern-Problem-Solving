# 1 
# 2 3
# 3 4 5
# 4 5 6 7
# 5 6 7 8 9
n = int(input("Enter the nuber of row "))
count = 1
for i in range(n):
  for j in range(i+1):
    print(chr(count+64),end=" ")
    count += 1  
  print(" ")  