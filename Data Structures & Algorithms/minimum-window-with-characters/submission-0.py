class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need=Counter(t)
        l=0
        have=0
        need_count=len(need)
        window=defaultdict(int)
        result=[-1,-1]
        min_length=float("inf")
        for r in range(len(s)):
            char=s[r]
            window[char]+=1
            if char in need and window[char]==need[char]:
                have+=1
            while have==need_count:
                window_len=r-l+1
                if window_len<min_length:
                    min_length=window_len
                    result=[l,r]

                left_char=s[l]
                window[left_char]-=1

                if left_char in need and window[left_char]<need[left_char]:
                    have-=1
                
                l+=1
        left, right = result
        return "" if min_length == float("inf") else s[left:right + 1]



        
            
        