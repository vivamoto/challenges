"""
Permutation Step
Difficulty: Medium
Maximum Score: 10

Description: For this challenge you will determine the next greatest number
using the same numbers of a given argument.

Have the function PermutationStep(num) take the num parameter being passed and
return the next number greater than num using the same digits.

For example: if num is 123 return 132, if it's 12453 return 12534. If a number
has no greater permutations, return -1 (ie. 999).

Examples
Input: 11121
Output: 11211

Input: 41352
Output: 41523


"""
import copy as cp
import itertools as it

def PermutationStep(num):
    # 1. create a list with all digits
    snum = []
    for i in str(num):
        snum.append(i)
    
    next_num = []  # store next number
    # 2. Sort all digits (smallest value)
    n = ''
    for i in range(len(snum)):
        for j in range(len(snum)):
            if snum[i] < snum[j]:
                n = n + snum[i]
                temp = cp.copy(snum)
                snum[i] = temp[j]
                snum[j] = temp[i]
    # print ('Smallest number:', snum)
    # 3. Permutation: Pick next largest number
    for i in range(len(snum)):
        n = snum[:i]
        for j in range(len(snum)):
            if i != j :
                temp = cp.copy(snum)
                temp[i] = snum[j]
                temp[j] = snum[i]
                # print('i:', i, 'j:',j, 'temp:', temp)
                # Convert list of strings to number
                n = ''
                for k in temp:
                    n = n + k
                # print (n)
                # Create a list of possible numbers
                if int(n) > num:
                    next_num.append(int(n))
    
    num = min(next_num)
    return num

# Use of itertools library
def PermutationItertools(num):
    # 1. Create list of all possible permutations
    lnum = it.permutations(str(num), r=None)
    lnum = cp.copy(list(lnum))
    # Convert list to number and save if larger than num
    next_num = []
    for i in lnum:
        # 2. Convert list of tupples to number
        n = ''
        for j in i:
            n = n + j
        # 3. Save number larger than num
        if int(n) > num:
            next_num.append(int(n))

    # 4. Return smallest number
    if len(next_num) == 0:
        return -1
    else:
        return min(next_num)

# Demo
if __name__ == '__main__':

    # My solution
#    print(PermutationStep(11121))
#    print(PermutationStep(41352))
#    print(PermutationStep(12345))
#    print(PermutationStep(53241))

    print()
    # With itertools library
    print(PermutationItertools(11121))
    print(PermutationItertools(41352))
    print(PermutationItertools(12345))
    print(PermutationItertools(53241))
    print(PermutationItertools(999))

