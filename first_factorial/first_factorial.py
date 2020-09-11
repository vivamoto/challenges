"""
First Factorial

Have the function FirstFactorial(num) take the num parameter being passed and
return the factorial of it. For example: if num = 4, then your program should
return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and
18 and the input will always be an integer.

Examples
Input: 4
Output: 24

Input: 8
Output: 40320
"""
# Iterative solution
def FirstFactorial(num):
    n = 1
    for i in range(1, num + 1):
        n *= i
    return n

# Recursive solution
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

if __name__ == '__main__':
    input = 4
    print(FirstFactorial(input))
    print(factorial(input))
    # Output: 24
    
    input = 8
    print(FirstFactorial(input))
    print(factorial(input))
    # Output: 40320
    

