# string = input("Enter the string ")
# if string.lower() == string[::-1].lower():
#   print("Given string is Palindrom")
# else:
#   print("Given string is not Palindrom") 

def palindrom(string):
  result=True
  for char in range(len(string)//2):
    if string[char]!=string[len(string)-1-char]:
       result=False
  return result
string = input("Enter the string ")    
res=palindrom(string)

if res:
  print("Palindrom")
else:
  print("Not Palindrom")  