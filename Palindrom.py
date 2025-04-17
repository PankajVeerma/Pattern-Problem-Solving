string = input("Enter the string ")
if string.lower() == string[::-1].lower():
  print("Given string is Palindrom")
else:
  print("Given string is not Palindrom")  