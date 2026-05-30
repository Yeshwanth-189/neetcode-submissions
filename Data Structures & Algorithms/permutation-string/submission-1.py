class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        if k>len(s2):
            return False
        s1_count=Counter(s1)
        window_count=Counter(s2[:k])
        if window_count==s1_count:
            return True
        for r in range(k,len(s2)):
            window_count[s2[r]]+=1
            left_char=s2[r-k]
            window_count[left_char]-=1
            if window_count[left_char] == 0:
                del window_count[left_char]

            if window_count == s1_count:
                return True
        return False
        
        