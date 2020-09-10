"""
Tree Constructor
Difficulty: Medium
Maximum Score: 10

Description: For this challenge you will determine if an array of integer pairs
can form a binary tree properly.

Have the function TreeConstructor(strArr) take the array of strings stored in
strArr, which will contain pairs of integers in the following format: (i1,i2),
where i1 represents a child node in a tree and the second integer i2 signifies
that it is the parent of i1.

For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the
following tree:

         4
        /
       2
     / \
    1  7

which you can see forms a proper binary tree. Your program should, in this case,
return the string true because a valid binary tree can be formed. If a proper
binary tree cannot be formed with the integer pairs, then return the string false.
All of the integers within the tree will be unique, which means there can only
be one node in the tree with the given integer value.

Examples
Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
Output: true

Input: ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
Output: false

More examples in the end of this file.

"""
import re

def TreeConstructor(strArr):
    
    # 0. Create son and father lists
    son = []
    father = []
    for p in strArr:
        _, n1, n2, _ = re.split(r'\(|,|\)', p)
        son.append(n1)
        father.append(n2)
    
    # 1. Father can have 1 or 2 sons
    for i in father:
        count = 0
        for j in father:
            if i == j:
                count += 1
                if count > 2:
                    return 'Father has more than 2 sons'

    # 2. Son can have only 1 father
    for i in son:
        count = 0
        for j in son:
            if i == j:
                count += 1
                if count > 1:
                    return 'Son has more than 1 father'

    # 3. Root has no father
    root = []  # save roots
    for i in father:
        # Father is son of another node
        count = 0
        for j in son:
            if i == j:
                count += 1
        # Father is root
        if count == 0:
            root.append(i)
    
    # 4. Only one root
    if len(root) > 1:
        if len(root) == 2:
            if root[0] != root[1]:
                return('More than 1 root')
        elif len(root) > 2:
            return ('More than 1 root')

    # If passed all tests, the input list is a tree and return 'true'
    
    return 'This is a single tree'

# Demo
if __name__ == '__main__':
    
    input = ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
    print(TreeConstructor(input))
    
    input = ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
    print(TreeConstructor(input))
    
    input = ["(2,7)", "(5,6)", "(11,6)", "(6,7)", "(4,9)", "(9,5)", "(5,2)", "(7,0)"]
    print(TreeConstructor(input))
    
    input = ["(1,2)", "(2,3)", "(4,3)", "(3,5)", "(6,7)", "(8,7)", "(7,5)"]
    print(TreeConstructor(input))
    
    input = ["(1,2)", "(2,3)", "(4,3)", "(0,5)", "(6,7)", "(8,7)", "(7,5)"]
    print(TreeConstructor(input))
   
    
