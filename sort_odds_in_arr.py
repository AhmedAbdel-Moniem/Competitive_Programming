# SORT ODD NUMBERS IN AN ARRAY.

def sort_odd1(source_array):
    # Return a sorted REVERSED array odd array.
    odd_array = sorted([x for x in source_array if x%2 > 0],
    	reverse=True)
    index = 0
    # new list to inject all numbers.
    new_array = []
    # loop on the main arr.
    for x in source_array:
        # if even
        if x%2 == 0:
        	# Append in the new array.
            new_array.append(x)
        # if Odd:
        else:
        	# Append REVERSED SORTED array
            new_array.append(odd_array.pop())
            # Increment the index after the odd number.
            index += 1
    return new_array


# the best practice
def sort_odd2(source_array):
    odd_array = sorted([y for y in source_array if y%2 >0], reverse=True)
    return [x if x%2 == 0 else odd_array.pop() for x in source_array]

print(sort_odd1([7,2,5,6,8,3,44,4]))
print(sort_odd2([7,2,5,6,8,3,44,4]))