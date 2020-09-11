"""
Codeland Username Validation

Have the function CodelandUsernameValidation(str) take the str parameter being
passed and determine if the string is a valid username according to the following
rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string 'true',
otherwise return the string 'false'.

Examples
Input: "aa_"
Output: false

Input: "u__hello_world123"
Output: true
"""
import re

def CodelandUsernameValidation(strParam):

    # 1. The username is between 4 and 25 characters.
    if len(strParam) < 4 or len(strParam) > 25:
        return 'false'
    
    # 2. It must start with a letter.
    letter = re.match('[A-Z,a-z]', strParam[0])
    if letter == None:
        return 'false'
    
    # 3. It can only contain letters, numbers, and the underscore character.
    chars = re.match('[A-Z,a-z,0-9,_]', strParam[len(strParam) - 1])
    if chars == None:
        return 'false'
    
    # 4. It cannot end with an underscore character.
    letter = re.match('_', strParam[len(strParam) - 1])
    if letter != None:
        return 'false'
    
    # 5. Return 'true' if pass all tests
    return 'true'

if __name__ == '__main__':
    
    input = "aa_"
    print(CodelandUsernameValidation(input))
    # Output: false
    
    input = "u__hello_world123"
    print(CodelandUsernameValidation(input))
    # Output: true
