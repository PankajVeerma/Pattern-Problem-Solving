# A  
# B C  
# D E F  
# G H I J  
# K L M N O

# n = int(input("Enter the nuber of row "))
# count = 1
# for i in range(n):
#   for j in range(i+1):
#     print(chr(count+64),end=" ")
#     count += 1  
#   print(" ")  
  
  
  
  
  
  
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# n = int(input("Enter the nuber of row "))
# count = 1
# for i in range(n):
#   for j in range(i+1):
#     print(count,end=" ")
#     count += 1
#   print(" ")
  
  
  
# 1 
# 3 2
# 4 5 6
# 10 9 8 7 
# 11 12 13 14 15

# n = int(input("Enter the nuber of row "))
# count = 1
# for i in range(n):
#   if i%2==2:
#     for j in range(i+1):
#       print(count+j,end=" ")
#       count += 1
#   else:  
#       for j in range(i+1):
#          print(count-j,end=" ")
#          count += 1
#       print(" ")
  
  
  
n = int(input("Enter the nuber of row ")) 
for i in range(1,n//2+1):
   for j in range(2,n+1):
     if i**j == n:
       print(f"Base is {i} and Power is {j}")
       break
   
     