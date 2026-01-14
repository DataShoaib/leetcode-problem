class solution:
    def max_element_arr(self,arr:list[int]):
        if len(arr)==0:
            return None
        max_element=arr[0]
        for i in range(1,len(arr)):
            if arr[i]>max_element:
                max_element=arr[i]
        return max_element        
arr=[3,4,5,3,3,5,6,50,3,23,5,5]

sl=solution()
max_ele=sl.max_element_arr(arr)
print(max_ele)