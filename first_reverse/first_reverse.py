"""
First Reverse

Have the function FirstReverse(str) take the str parameter being passed and
return the string in reversed order. For example: if the input string is
"Hello World and Coders" then your program should return the string "sredoC dna
dlroW olleH".

Examples
Input: "Hello World and Coders"
Output: etybredoc

Input: "I Love Code"
Output: edoC evoL I
"""
def FirstReverse(strParam):

  res = ''
  for i in range(len(strParam)-1, -1, -1):
    res += strParam[i]

  return res

if __name__ == '__main__':
    input = "Hello World and Coders"
    print(FirstReverse(input))
    # Output: sredoC dna dlroW olleH
    
    input = "I Love Code"
    print(FirstReverse(input))
    #Output: edoC evoL I
    

