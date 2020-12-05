''' 
Display string length.  (using character array & character pointers. Dont use Library functions)
'''

s = 'Hello World'
count = 0  

for c in s:
    count += 1

print('Length of string: ', count)

print('Length using library:', len(s))
