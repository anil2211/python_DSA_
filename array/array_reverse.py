'''
Given an array arr[], the task is to reverse the array. Reversing an array means 
rearranging the elements such that the first element becomes the last, the second 
element becomes second last and so on.
Input: arr[] = {1, 4, 3, 2, 6, 5}  
Output: {5, 6, 2, 3, 4, 1}
'''
print("\n by temporary varibale")
# using temporary variable
def reverseArray(arr):
    n=len(arr)
    temp=[0]*n

    for i in range(n):
        temp[i]=arr[n-i-1] #copy element from original to temp in reverse order

    for i in range(n):
        arr[i]=temp[i]  #copy back element into array

    for i in range(len(arr)):
        print(arr[i], end=" ")

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]
    reverseArray(arr)

print("\nusing two pointers")
# using two pointers
def reverseArray(arr):
    left=0
    right=len(arr)-1

    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left=left + 1
        right=right -1
    for i in range(len(arr)):
        print(arr[i], end=" ")
if __name__ == "__main__":
    arr = [1,7,6,4,9,2]
    reverseArray(arr)

# by swapping
print("\nby swapping")
def reverseArray(arr):
    n = len(arr)
    for i in range(n // 2):
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]
    reverseArray(arr)

    for i in range(len(arr)):
        print(arr[i], end=" ")