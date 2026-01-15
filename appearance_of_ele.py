# Problem: Given an array nums, return the element that appears more than ⌊n/2⌋ times.
# Example:
# Input: nums = [3,3,3,1,2]
# Output: 3
# ________________________________________

# brute force

class Solution:
    def appearance_of_ele(self,arr:list[int],k:int)->list:
        result=[]
        for i in range(len(arr)):
            count=0
            for j in range(len(arr)):
                if arr[i]==arr[j]:
                    count+=1
            if count>len(arr)//k and arr[i] not in result:
                result.append(arr[i])       
        return result
    
arr=[3,3,3,2,2,2,2]
sl=Solution()
print(sl.appearance_of_ele(arr,3))

# hashmap

class Solution:
    def appearance_of_elemenet(self,arr:list[int],k:int)->list:
        result=[]
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1

        for key,value in freq.items():
            if value > len(arr)//k:
                result.append(key)
        return result        
arr=[3,3,3,2,2,2,2]
sl=Solution()
print(sl.appearance_of_elemenet(arr,3))

# vote's theorem

class Solution:
    def appear_vote(self,arr:list[int],k:int)->list:
        freq=[]
        candidate={}

        for num in arr:
            if num in candidate:
                candidate[num]+=1
            elif len(candidate)<k-1:
                candidate[num]=1
            else:
                remove_key=[]
                for key in candidate:
                    candidate[key] -= 1
                    if candidate[key]==0:
                        remove_key.append(candidate[key])

                for key in remove_key:
                    del candidate[key]   
        result=[]
        for key,Values in candidate.items():
            if Values > len(arr)//k:
                result.append(key)
        return result       


arr=[3,3,3,2,2,2,2]
sl=Solution()
print(sl.appear_vote(arr,3))
            
         