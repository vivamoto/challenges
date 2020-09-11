"""
Questions Marks

Have the function QuestionsMarks(str) take the str string parameter, which will
contain single digit numbers, letters, and question marks, and check if there
are exactly 3 question marks between every pair of two numbers that add up to 10.

If so, then your program should return the string true, otherwise it should
return the string false. If there aren't any two numbers that add up to 10 in
the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return
'true' because there are exactly 3 question marks between 6 and 4, and 3
question marks between 5 and 5 at the end of the string.

Examples

Input: "aa6?9"
Output: false

Input: "acc?7??sss?3rr1??????5"
Output: true
"""
import re
def QuestionsMarks(strParam):
    n = 0
    count = 0
    flag = 'false'
    for i in strParam:
        if i in '0123456789':
            n += int(i)
            if count == 3 and n == 10:
                flag = 'true'
            count = 0
        elif i == '?':
            count += 1
    
    return flag

if __name__ == '__main__':
    input = "aa6?9"
    print(QuestionsMarks(input))
    # Output: false

    input = "acc?7??sss?3rr1??????5"
    print(QuestionsMarks(input))
    # Output: true
