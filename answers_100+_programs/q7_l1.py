'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program: 3,5
Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

'''
def method_1(X, Y):
    main_list = [[0 for col in range(Y)] for row in range(X)]
    for row in range(X):
        for col in range(Y):
            main_list[row][col] = row*col
    return main_list

def method_2(X, Y):
    final_list = []
    for i in range(X):
        final_list.append([i*j for j in range(Y)])
    return final_list

dimensions = [int(num) for num in input('Enter two numbers as comma separated:').split(',')]
X = dimensions[0]
Y = dimensions[1]

print(method_1(X, Y))
print(method_2(X, Y))
