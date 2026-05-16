class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def signature(s: str):
            sig_anagram=Counter(s)
            return sig_anagram

        res = defaultdict(list)
        for i in range(0,len(strs)):
            sig_anagaram=tuple(sorted(signature(strs[i]).items()))
            res[sig_anagaram].append(strs[i])
        return list(res.values())