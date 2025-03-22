
# Frequency of the input
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