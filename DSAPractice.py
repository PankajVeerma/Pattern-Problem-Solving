
def selctionSort(nums):
    for i in range(len(nums)):
       min_index=i
       for j in range(i+1,len(nums)):
           if nums[j]<nums[min_index]:
               min_index=j
       nums[i],nums[min_index]=nums[min_index],nums[i]
    return nums
nums=[2,4,3,3,25,67,87,6554,3]    
# print(selctionSort(nums))     
  
  
    
def bubbleSort(nums):
    for i in range(len(nums)-1,-1,-1):
        for j in range(0,i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]= nums[j+1],nums[j]
    return nums            

nums=[2,4,3,3,25,67,87,6554,3]   
# print(bubbleSort(nums))
    
def InsertionSort(nums):
    for i in range(1,len(nums)):
        key=nums[i]
        j = i-1
        while key > 0 and nums[j] > key :
          nums[j+1]=nums[j]
          j-1
        nums[j+1]=key
    return nums      
nums=[2,4,3,3,25,67,87,6554,3]   
# print(InsertionSort(nums))    
# ----------------Merge Sort--------------------   

def merge_Arr(left,right):
  result=[]
  i=0
  j=0
  while i<len(left) and j< len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i +=1
    else:
      result.append(right[j])
      j +=1
  if i<len(left):
      while i< len(left):
        result.append(left[i])
        i +=1
  if j<len(right):
      while j<len(right):
        result.append(right[j])
        j +=1  
  return result             
def mergeSort(nums):
    if len(nums)<=1:
      return nums
    mid = len(nums)//2
    left_arr = nums[:mid]
    right_arr = nums[mid:]
    left = mergeSort(left_arr)
    right = mergeSort(right_arr)
    return merge_Arr(left, right)
    
              
# nums=[2,4,3,3,25,67,87,6554,3]   
# print(mergeSort(nums))   



# -------------Quick Sort ------------------


def Quick_Partition(nums, low, high):
  pivot = nums[low]
  i=low
  j=high
  while i<j:
    while i < j and nums[i]<=pivot:
      i += 1
    while nums[j]>pivot:
      j -=1
    if i <= j:
      nums[i],nums[j]=nums[j],nums[i]
    else:
      break
  nums[low],nums[j] = nums[j],nums[low]
  print("J=======",j)
  return j

def Quick_Sort(nums,low,high):
  if low< high:
    p_index = Quick_Partition(nums, low, high)    
    Quick_Sort(nums, low, p_index-1)
    Quick_Sort(nums, p_index+1, high)    

  
nums = [2, 4, 3, 3, 25, 67, 87, 6554, 3]
Quick_Sort(nums, 0, len(nums) - 1)
print(nums)