class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new=""
        for i in range(len(s)):
            if s[i].isalnum():
                s_new=s_new+s[i].lower()
        s_rev=s_new[-1::-1]
        return s_rev==s_new        