class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        freq=defaultdict(int)
        max_length=0
        max_freq=0
        while r < len(s):
            freq[s[r]]+=1
            max_freq=max(max_freq,freq[s[r]])
            while (r-l+1)-max_freq>k:
                freq[s[l]]-=1
                l+=1
            max_length=max(max_length,r-l+1)
            r+=1
        return max_length