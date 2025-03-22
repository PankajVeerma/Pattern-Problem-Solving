# Anagram Number or string
s1 = "listen"
s2 = "Silent"
if len(s1) ==len(s2):
  if sorted(s1.upper())==sorted(s2.upper()):
    print(f"Given input  is Anagram") 
  else:
    print("Given inout is not Anagram")
else:
  print("Given inout is not Anagram")   