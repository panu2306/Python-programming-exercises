'''
Check if given string is palindrome. 
'''

def palindrome(s):
    if(s == ''.join(reversed(s))):
        return True

s = input('Enter a string:')

if(palindrome(s) == True):
    print('String is palindrome')
else:
    print('string is not palindrome')
