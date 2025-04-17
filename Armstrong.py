number =int(input("Enter the number "))

count = 0
temp = number
while number>0:
  rem = number%10
  number = number//10
  count += 1

sum = 0 
while number>0:
  rem = number%10
  sum += rem**count
  number = number//10
temp  =number  
if sum == temp:
  print("Given number is Armstrong number")
else:
  print("Given number is not Armstrong number")
    
  