# Check if Array is Sorted
# Problem: Given an integer array nums, return true if the array is sorted in non-decreasing order, else return false.
# Example:
# Input: nums = [1,2,3,4,5]
# Output: true
# ________________________________________

class solution:
    def is_sorted(self,arr:list[int])->bool:
        if len(arr)<=1:
            return True
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return False
        return True
        
arr=[1,2,3,4,5]        
sl=solution()
is_sort=sl.is_sorted(arr)     
print(is_sort)   

# time complexity=o(n) because this traverse once 
# space complexity = o(1)