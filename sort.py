def bubble_sort(li):
    for i in range(len(li)):
      for j in range(i+1,len(li)):
        if li[i]>li[j]:
          li[i],li[j] = li[j],li[i]
    return li 
    
arr_data = [2,4,6,8,90,12,14,20,16,23,18]    
data = bubble_sort(arr_data)  
print(data)
    
    
    
       
def selection_sort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]< arr[min_index]:
                min_index=j
        arr[i],arr[min_index] = arr[min_index], arr[i]        
    return arr
  
a=[1,4,6,9,3,2,0]
print(selection_sort(a))         




# for i in range(5):
#   if i%2==0:
#     print(i)
#   else: 
#     break
  
# for i in range(5):
#   if i%2==0:
#     print(i)
#   else: 
#     continue 