def theLoveLetter(s):
    """
    This function returns the integer representing the minimum number
    of operations needed to make the string a palindrome.
    """

    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    l = len(s) # length of input string

    # Sub divide the input string into two equal parts
    str1 = s[:l//2]

    # handle odd input string length
    str2 = s[l//2 if l % 2 == 0 else l//2 + 1:]

    # handle first edge case
    # if input string is already a palindrome return
    if s == s[::-1]: 
        return 0
    
    # initialize variables to hold totals of 
    # string manipulations
    part1 = 0
    part2 = 0

    # traverse through first part of the string 
    # from the string's beginning
    # while comparing current char with char from
    # second part of the string from the end

    

    for i in range(1,len(str1)+1):
        if str1[i-1] != str2[len(str2)-i]:
            # check the positions of the chars in alphabets
            if alphabets.find(str1[i-1]) < alphabets.find(str2[len(str2)-i]):
                part1 += (alphabets.find(str2[len(str2)-i]) - alphabets.find(str1[i-1]) )
            else:
                part2 += (alphabets.find(str1[i-1]) - alphabets.find(str2[len(str2)-i]))
    return part1+part2
# Driver code
print(theLoveLetter('bafhaef'))

