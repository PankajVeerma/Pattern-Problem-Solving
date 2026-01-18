def wordCounting(string):
        #    BruteForce Solution Time Complexity O(n)
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


