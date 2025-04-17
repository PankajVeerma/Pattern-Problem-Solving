def printNatural(n):
  return [i for i in range(n+1)]

def reverseNatural(n):
  return [i for i in range(n,0,-1)]

def AlphabateUpper(n):
  return [chr(64+i) for i in range(1,n+1)]  
def AlphabateLower(n):
  return [chr(96+i) for i in range(1,n+1)]  
def evenNumber(n):
  return [i for i in range(n+1) if i%2==0 ]  
def oddNumber(n):
  return [i for i in range(n+1) if i%2!=0 ]  
def printNaturalSum(n):
  sum = 0
  i=1
  while i <= n:
    sum +=i
    i +=1
  return [sum]
def printEvenSum(n):
  sum = 0
  i=1
  while i <= n:
    if i% 2 == 0:
      sum +=i
    i +=1
  return [sum]
def printOddSum(n):
  sum = 0
  i=1
  while i <= n:
    if i%2 != 0:
      sum +=i
    i +=1
  return [sum]
def multiplication(number, ran):
  return [number*i for i in range(1,ran+1)]  
def countNumber(num : int):
  count = 0
  while num > 0:
    count+=1
    num //= 10
  return count
def FastLast(num):
    return int(str(num)[0]), int(str(num)[-1])
def SumFastLast(num):
    return int(str(num)[0])+int(str(num)[-1])
  
  
def SwapFastLast(number):
   digit_list = [i for i in str(number)]
   digit_list[0], digit_list[-1] = digit_list[-1], digit_list[0]
   return int(''.join(digit_list))
def sumOfDigit(number):
  sum =0
  while(number>0):
    digit  =number%10
    sum+=digit
    number//=10
  return sum


def productOfDigit(number):
  sum =1
  if number == 0:
    return 0
  while(number>0):
    digit  =number%10
    sum*=digit
    number//=10
  return sum

def reverse(number):
  reverse =0
  while(number>0):
    digit  =number%10
    reverse = reverse*10 +digit
    number//=10
  return reverse
def Palindrom(number):
  if number == reverse(number):
    return True
  return False

def frequencyOfInteger(number):
  frequency= {}
  while number>0:
    digit=number%10
    if digit in frequency:
      frequency[digit]+=1
    else:
      frequency[digit]=1
    number//=10
  return frequency  
       
       
def numberToword(number):
  number = str(number)
  word = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
  }
  return [word[digit] for digit in number] 

def numberToword2(number):
  pass
def printASCII():
  for i in range(1, 127):
    print(f"ASCII value of {chr(i)} is {i}")
  
    


# print(printNatural(10)) 
# print(reverseNatural(10)) 
# print(AlphabateUpper(26))
# print(AlphabateLower(26))
# print(evenNumber(26))
# print(oddNumber(26))
# print(printNaturalSum(5))
# print(printEvenSum(5))
# print(printOddSum(5))
# print(multiplication(2,10))
# print(countNumber(1234))
# print(FastLast(1213142))
# print(SumFastLast(1213142))
# print(SwapFastLast(1213142))
# print(sumOfDigit(1234))
# print(productOfDigit(11110))
# print(reverse(11110))
# print(Palindrom(12321)) # True
# print(frequencyOfInteger(123321))
print(numberToword(1234))
print(printASCII())