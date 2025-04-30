
def commulativesum(list): 
    sum = 0
    li1=[]
    for i in list:
        sum+=i
        li1.append(sum)
    return li1    
a=[1,2,3,4,5]    
print(commulativesum(a))