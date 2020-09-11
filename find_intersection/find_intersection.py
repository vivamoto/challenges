"""
Find Intersection

Have the function FindIntersection(strArr) read the array of strings stored in
strArr which will contain 2 elements: the first element will represent a list of
comma-separated numbers sorted in ascending order, the second element will
represent a second list of comma-separated numbers (also sorted).

Your goal is to return a comma-separated string containing the numbers that
occur in elements of strArr in sorted order. If there is no intersection, return
the string 'false'.

Examples
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13

Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Output: 1,9,10

"""
def FindIntersection(strArr):
    # code goes here
    a1 = strArr[0].split(', ')
    a2 = strArr[1].split(', ')
    result = []
    for element in a1:
        if element in a2:
            result.append(element)
    if len(result) == 0:
        return 'false'
    else:
        return ','.join(result)
    


if __name__ == '__main__':
    
    input = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    print(FindIntersection(input))
    # Output: 1, 4, 13
    
    input = ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
    print(FindIntersection(input))
    # Output: 1, 9, 10

