'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

string_input = input('Enter a string containing letters and digits:')
letter_count = 0 
digit_count = 0
for c in string_input:
    if(c.isalpha()):
        letter_count += 1
    elif(c.isdigit()):
        digit_count+= 1
    else:
        pass

print('LETTERS', letter_count)
print('DIGITS', digit_count)
