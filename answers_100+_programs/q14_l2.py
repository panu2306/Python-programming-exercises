'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
    Hello world!
Then, the output should be:
    UPPER CASE 1
    LOWER CASE 9
'''

string_input = input('Enter a sentence with upper-case & lower-case letters: ')
count_dict = {'lower':0, 'upper':0}
for c in string_input:
    if(c.islower()):
        count_dict['lower'] += 1
    elif(c.isupper()):
        count_dict['upper'] += 1
    else:
        pass

print('UPPER CASE', count_dict['upper'])
print('LOWER CASE', count_dict['lower'])

