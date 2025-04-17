string  =input("Enter the string ")
list1 = []
for i in range(len(string)-1,-1,-1):
  list1.append(string[i])
print("".join(list1))