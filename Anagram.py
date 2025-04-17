str1 = input("Enter the first string ")
str2 = input("Enter the second string ")
if len(str1) == len(str2):
  if sorted(str1.upper())==sorted(str2.upper()):
    print(f"Given input  is Anagram") 
  else:
    print("Given input is not Anagram")
else:
  print("Given input is not Anagram")    