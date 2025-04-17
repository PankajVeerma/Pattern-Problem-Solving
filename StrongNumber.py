def fact(n):
  if n == 0:
    return 1
  else:
    return n*fact(n-1)
    
number = int(input("Enter the number "))
sum = 0
temp = number
while temp>0:
  rem = temp%10
  sum += fact(rem)
  temp = temp//10
print(sum)
if sum == number:
  print("Given number is Strong number")

else:
  print("Given number is not Strong number")


