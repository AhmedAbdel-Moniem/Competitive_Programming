from collections import Counter

# Number One
def count_vowels(a_string):
	count_ = Counter(a_string)
	print(sum([count_[x]for x in 'aeiou']))

count_vowels('ahmed abdel moniem mohamed abdel gawad')




# Number Two
def count_vowels2(a_string2):
	result = a_string2.count('a') + a_string2.count('e') + a_string2.count('i') + a_string2.count('o') + a_string2.count('u')
	print(result)

count_vowels2('ahmed abdel moniem mohamed abdel gawad')


# NUmber Four
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

# NUmber Five
def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels
# NUmber SIX
def count_vowels(my_string):
    count = 0
    for char in my_string:
        if char in 'aeiou':
            count += 1
    return count


print(count_vowels('ahmed abdel monem mohamed'))