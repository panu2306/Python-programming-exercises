'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8
Then, the output should be: 40320
'''

def factorial_for_loop(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i
    return fact

def factorial_recursion(num):
    if(num == 1 or num == 0):
        return 1
    else: 
        return num*factorial_recursion(num-1)

print(factorial_for_loop(8))
print(factorial_recursion(8))
