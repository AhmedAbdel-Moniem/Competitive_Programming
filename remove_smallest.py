""" Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left. 
Examples
remove_smallest([1,2,3,4,5]) = [2,3,4,5]
remove_smallest([5,3,2,1,4]) = [5,3,2,4]
remove_smallest([2,2,1,2,1]) = [2,2,2,1]"""

# First 
def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    else:
        numbers_s = numbers[:]
        numbers_s.remove(min(numbers_s))
        clean_list = []
        
        for x in numbers_s:
#             if x not in clean_list:
                clean_list.append(x)
        
        return clean_list
print(remove_smallest([1,2,3,1,1]))

# Second
def remove_smallest(numbers):
	if len(numbers) == 0: return []
	a = numbers[:]
	a.remove(min(a))
	return a
print(remove_smallest([1,2,3,1,1]))	