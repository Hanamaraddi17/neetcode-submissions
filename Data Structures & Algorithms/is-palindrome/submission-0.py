class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for c in s.lower():
            if c.isalnum():
                st += c
        l = 0
        r = len(st) - 1
        # print(st)
        while l<r:
            if st[l] != st[r]:
                return False
            l+=1
            r-=1
        return True

        