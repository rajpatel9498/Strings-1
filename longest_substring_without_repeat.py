class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        if len(s)==0:
            return 0
        
        s_dict={}
        
        maximum=0
        slow=0
        for i in range(len(s)):
            
            if s[i] in s_dict:
                slow = max(slow,s_dict[s[i]])
            
            s_dict[s[i]]=i+1
            
            maximum=max(maximum,i-slow+1)
            
        return maximum
