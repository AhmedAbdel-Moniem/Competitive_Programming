""" 
Find the stray number
Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
"""
# One
def stray(arr):
    for i in arr:
        if arr.count(i) ==1:
            return i
print(stray([1,3,1,1]))
# Two
def stray(arr):
    return min(arr, key=arr.count)
print(stray([1,7,1,1]))
# Three
def stray(arr):
    arr.sort()
    return arr[-1] if arr[0] == arr[1] else arr[0]
print(stray([1,5,1,1]))