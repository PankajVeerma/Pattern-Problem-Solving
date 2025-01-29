col = 5

for i in  range(col+1):
  for j in range(i):
    print("*", end="")
  print()  
for i in  range(col+1):  
  for k in range((col-i)-1):
    print("*", end="")
  print()
     