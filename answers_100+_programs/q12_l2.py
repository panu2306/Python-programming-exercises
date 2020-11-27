'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
even_digit_num_list = []

for num in range(1000, 3001):
    current = num
    while(num>0):
        digit = num%10
        if(digit%2!=0):
            break
        num = num//10
    if(num==0):
        even_digit_num_list.append(str(current))

print('o/p using long method:')
print(','.join(even_digit_num_list))


# Easy Method:
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)

print("o/p using easy method:")
print(",".join(values))
