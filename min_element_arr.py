class solution:
    def min_elem(self,arr:list[int])->int:
        if len(arr)==0:
            return None
        min_element=arr[0]
        for i in range(1,len(arr)):
            if arr[i]<min_element:
                min_element=arr[i]
        return min_element
arr=[2,23,4,5,0,6,54,3,5,6,65,4,4]    
sl=solution()
min_ele=sl.min_elem(arr)   
print(min_ele)         