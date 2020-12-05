'''
Check given number is prime number or not.

'''

def check_prime(num):
    flag = 0
    if(num > 1): 
        for i in range(2, num):
            if((num % i) == 0):
                flag = 1
                break
            else:
                pass
    else:
        print('Number is neither prime nor composite.')
    
    if(flag==0):
        print('Prime')
    else:
        print('Not Prime')

n = int(input('Enter a num:'))
check_prime(n)
            
