"""
Longest Word

Have the function LongestWord(sen) take the sen parameter being passed and
return the largest word in the string. If there are two or more words that are
the same length, return the first word from the string with that length.

Ignore punctuation and assume sen will not be empty.

Examples
Input: "fun&!! time"
Output: time

Input: "I love dogs"
Output: love
"""
import re
def LongestWord(sen):

  res = ''
  for i in re.split('[^a-z|^A-Z|^0-9]', sen):
    if len(i) > len(res):
      res = i

  return res

if __name__ == '__main__':
    input = "fun&!! time"
    print(LongestWord(input))
    #Output: time
    
    input = "I love dogs"
    print(LongestWord(input))
    #Output: love
    
    input = "0123456789 123456"
    print(LongestWord(input))
    #Output: 0123456789

