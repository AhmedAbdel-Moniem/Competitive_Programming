""" Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so: """
def find_needle(haystack):
    # your code here
    for word in haystack:
        if word == 'needle':
            result = "found the needle at position "+ str(haystack.index('needle'))
            print('"'+result+'"')

find_needle(['a', 'b','needle','gunk'])
