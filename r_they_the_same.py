
""" Are They The Same ,
check if the array b is the same as a but multiplied in itself's values
"""

# One
def comp(arr_a,arr_b):
	return sorted([i**2 for i in arr_a]) == sorted(arr_b)


print(comp([1,2,3,4,5], [1,4,9,16,25]))
print(comp([1,2,3,4,5], [1,4,9,16]))

# Two
def comp(array1, array2):
    if array1 and array2:
        return sorted([x*x for x in array1]) == sorted(array2)
    return array1 == array2 == []