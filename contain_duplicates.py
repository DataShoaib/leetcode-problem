# Problem: Given an integer array nums, return true if any value appears at least twice, otherwise return false.
# Example:
# Input: nums = [1,2,3,4,1]
# Output: true
# ________________________________________


# using brute force
# class solution:
#     def contains_duplicate(self,arr:list[int])->bool:
#         if len(arr)==0:
#             return False
#         elif len(arr)==1:
#             return False
#         for i in range(len(arr)):
#             for j in range(i+1,len(arr)):
#                 if arr[i]==arr[j]:
#                    return True
#         return False

# arr = [1,1,3,5,3,5]     
# sl=solution()
# is_contains=sl.contains_duplicate(arr)  

# print(is_contains)

# optimized one o(n) time

class solution:
    def contains_duplicate(self,arr:list[int])->bool:
        if len(arr)==0:
            return False
        elif len(arr)==1:
            return False
        seen=set()
        for i in arr: 
              if i in seen:
                  return True
              seen.add(i)
        return False

arr = [1,2,4,1]     
sl=solution()
is_contains=sl.contains_duplicate(arr)  
print(is_contains)

    