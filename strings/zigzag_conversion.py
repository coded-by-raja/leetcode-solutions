class Solution(object):
    def convert(self, s, r):
        if r == 1 or r >=len(s):
            return s
        rows = [""] * r
        curr = 0
        d = 1
        for ch in s:
            rows[curr] +=ch
            if curr == 0:
                d = 1
            elif curr ==r -1:
                d = -1
            curr +=d
        return "".join(rows)
