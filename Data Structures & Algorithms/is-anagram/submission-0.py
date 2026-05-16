class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_freq=Counter(s)
        t_freq=Counter(t)
        for char in s_freq:
            if s_freq[char]!=t_freq[char]:
                return False
        
        return True



        