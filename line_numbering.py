"""
Testing 1-2-3

Your team is writing a fancy new text editor and you've been tasked with implementing 
the line numbering.

Write a function which takes a list of strings and returns each line prepended by
 the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples:

number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]



"""
# NORMAL
def number(lines):
  full = []
  empty = []
  if len(lines) == 0:
    return (empty)
  else:
    for counter, element in enumerate(lines):
      result = (str(counter +1) + ': ' + str(element))
      full.append(result)
    return(full)
print(number(['a','b','c']))
print(number([]))

# SMART
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]

# SMART
def number(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]