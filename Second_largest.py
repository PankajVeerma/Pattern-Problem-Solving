# #User function Template for python3
# class Solution:
#     def getSecondLargest(self, arr):
#         # Code Here
#         first_max = second_max = float('-inf')
#         if len(arr) < 2:
#             return -1
#         for num in arr :
            
#             if num > first_max:
#                 second_max= first_max
#                 first_max = num
                
#             elif num > second_max and num != first_max :
#                 second_max = num
                
                
#         if second_max == float('-inf'):
#             return -1
#         else:
#             return second_max

# if __name__ == '__main__':
#     ob = Solution()
#     arr = [60, 50, 80, 90, 100, 70,10, 20, 30, 40]
#     print(ob.getSecondLargest(arr))

