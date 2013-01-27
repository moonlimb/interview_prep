"return the longest palindrome in the string"
def longest_palindrome(str):
   pass 

"iterative solution to whether a string contains palindrome"
def has_palindrome(str):
    for i in xrange(len(str)/2):
        if str[i] != str[len(str)-1-i]:
            return False
    return True

"recursive solution to whether a string is a palindrome"
def is_palindrome(str):
    if len(str) < 2:
        return True
    else:
        if str[0] != str[-1]:
            return False
    return True   
