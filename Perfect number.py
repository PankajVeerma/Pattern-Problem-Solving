number  =int(input("Enter the number "))
sum = 0
for i in range(1,(number//2)+1):
  if number%i==0:
    sum += i
if sum == number:
  print("Given number is perfect number")
else:
  print("Given number is not perfect number")  