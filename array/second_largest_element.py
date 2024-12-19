# import array as arr
# Given an array  arr,return the second largest distinct element from an array.If the second largest
#  element doesn't exixt then return -1 
"""
"""
# def second_largest_element(self,arr):
def second_largest_element(arr):
    n=len(arr)
    
    if n<2:
        return -1
    
    first=second= float('-inf')
    for num in arr:
        if num>first:
            second=first                    # Update second largest to the previous largest
            first=num                       # Update largest to the current number
        elif num>second and num != first:   # If current number is less than largest but greater than second largest
            second=num                      # Update second largest to current number

    if second==float("-inf"):
        return -1
    else:
        return second

arr=[10,20,5,3,2]
print(second_largest_element(arr))             
