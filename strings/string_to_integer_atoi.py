class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign =  1
        r = 0

        I_MAX = 2**31 -1
        I_MIN = -2**31
        while i < n and s[i] == ' ':
            i += 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        while i < n and s[i].isdigit():
            r = r*10 +(ord(s[i]) - ord('0'))
            if sign *r <= I_MIN:
                return I_MIN
            if sign *r >=I_MAX:
                return I_MAX
            i += 1
        return sign*r 
