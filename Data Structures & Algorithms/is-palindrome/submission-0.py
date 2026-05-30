class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=s.split()
        strs="".join(string)
        new_str=""
        for i in range(0,len(strs)):
            if strs[i].isalnum():
                new_str+=strs[i]
        new_str=new_str.lower()
        print(new_str)
        if new_str!=new_str[::-1]:
            return False
        return True

        
        