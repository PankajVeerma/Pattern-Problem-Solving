# Anagram Number or string
# s1 = "listen"
# s2 = "Silent"
# if len(s1) ==len(s2):
#   if sorted(s1.upper())==sorted(s2.upper()):
#     print(f"Given input  is Anagram") 
#   else:
#     print("Given inout is not Anagram")
# else:
#   print("Given inout is not Anagram")  
  
dic = {}

str  ="dsjhfrtfyuwfufjjgjrfy8wqetrf" 
for index in str:
    if index in  dic:
       dic[index] += 1
    else:
        dic[index] = 1   
max_char  = max(dic,key=dic.get)
print(max_char)
print(dic[max_char])
        
print(dic)       