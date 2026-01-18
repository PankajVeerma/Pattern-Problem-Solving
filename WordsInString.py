def wordCounting(string):     #    BruteForce Solution Time Complexity O(n)
    i=0
    count=0
    n=len(string)
    while i< n:
        while i< n and string[i]==" ":
            i+=1
        if i< n and string[i]!=" ":
           count+=1
        while i< n and string[i] != " ":
            i +=1       
    return count


    # count=0 
    # max_count=0         # optimal Solution Time Complexity O(n)
    # is_word=False
    # for ch in string:
    #     if ch !=" " and not is_word:
    #         count +=1
    #         is_word=True
           
    #     elif ch ==" " and is_word:
    #         is_word=False 
             
    # return count
st="India is Great Country"
print(wordCounting(st))



def findDuplicateChar(string):
    dictionary={}
    value=1
    for char in string:
        if char not in dictionary:
            dictionary[char]=value 
        else:
            dictionary[char] = value +1  

    li=[]
    for key,value in dictionary.items():
        if value >1:
            li.append(key)        
    return li
string="abcdefasd"
print(findDuplicateChar(string))


# All Substring
def AllAubstring(string):
    result=[]
    count=0
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            result.append(string[i:j])
            count +=1
    return result ,count      
string="abcdefasd"
print(AllAubstring(string))  



# Sub String of Length k
def K_LenthSubString(string,k):
    result=[]
    for char in range(len(string)-k+1): 
       result.append(string[char:char+k])
    return result
string = "abcdefgh"
k=3
print(K_LenthSubString(string,k))
   

def Max_length_word(string):
    max_length=0
    words=string.split(' ')
    print(words)
    for char in words:
       length=len(char)
       if max_length<length:
           max_length=length
    return max_length      

string="India Is My Country"
print(Max_length_word(string))


def reverseSentance(sentance):
    result=[]
    words = sentance.split(" ")
    for char in range(len(words)-1,-1,-1):
        result.append(words[char])
    return " ".join(result) 

string="India Is My Country"
print(reverseSentance(string))