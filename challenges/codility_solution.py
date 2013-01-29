def is_reverse(left_str, right_str):
    """returns true if left_str is reverse of right_str"""
    if (not left_str) and (not right_str):
        return True
    else:
        len_substr = len(left_str)
        for index in xrange(len_substr):
            if left_str[index] != right_str[len_substr-1-index]:
                return False
        return True

def symmetryPoint ( S ):
    """returns the symmetry point in string S about whichthe substring before the point is the reverse of that after the point; returns -1 if there is no such point"""
    if not S:               
        return ''
    if len(S)%2 != 0:
        pivot = len(S)/2
        if is_reverse(S[0:pivot], S[pivot+1:]):
            return pivot
    return -1

