'''
Reverse given string. (using character array & character pointers. Dont use Library functions)
'''

# using revursion-method: 
def reverse(s):
    if(len(s)==0):
        return s
    else: 
        return reverse(s[1:]) + s[0]


s = 'Hello World'

print('Reverse using recursion:', reverse(s))
# simple method: 
reverse = ''
for ele in s: 
	reverse= ele + reverse

print('Reverse using for loop:', reverse)

# using string slicing: 
print('Reverse using string slicing:', s[::-1])

# using reversed method:
print('Reverse using reversed method:', ''.join(reversed(s)))
