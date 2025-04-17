# def flatelist(li):
#   li1=[]
#   for item in li:
#     if isinstance(item,list):
#       li1.extend(flatelist(item))
#     else:
#       li1.append(item)
#   return li1

# result = flatelist([
#     ["Apple", "Banana", "Cherry"],  # List of fruits
#     [10, 20, 30, 40],  # List of numbers
#     ["Python", "Java", "C++"],  # List of programming languages
#     [[1, 2], [3, 4], [5, 6]]  # List of lists (Matrix-like structure)
# ]
# )
# print(result)    


# str1 = "Python734362Java"
# li = []
# for element in str1:
#     if element.isdigit():
#         li.append(element)
#     else:
#         result = ''.join(li)
      
# # sum = 0        
# # for i in li:
# #     sum += int(i)
# # print(sum)    


# # Manually accumulating sum without using sum() or reduce()
# total = 0
# [total := total + num for num in [int(i) for i in li]]  # Using the walrus operator (Python 3.8+)

# print(total) 

def maxvalue(arr):
    max = arr[0]
    second_max =max
    for i in range(1,len(arr)):
        if arr[i]>max:
            max = arr[i-1]
    return max        

arr = [60, 50, 80, 90, 100, 70,10, 20, 30, 40]
max = maxvalue(arr)
print(max)