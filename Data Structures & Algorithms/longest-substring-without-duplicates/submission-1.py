class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        store = {}
        for r in range(len(s)): #pwwkew
            while(store.get(s[r], 0) > 0):
                store[s[l]] -= 1
                l += 1
            store[s[r]] = store.get(s[r], 0) + 1
            temp_len = r - l + 1
            max_len = max(temp_len, max_len)
        return max_len