def flerttern(li):
    result=[]
    for i in range(len(li)):
        if len(li)<=0:
            return li
        if isinstance(li[i] ,list):

            result.extend(flerttern(li[i]))
        else:        
            result.append(li[i])    
    return result   
l = [2, 3, 4, 5, [20, 6, 7,[32,[0,89,76,59],35,40], 56, 343]]

print(flerttern(l))