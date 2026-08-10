class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        store, max_len = set(), 0

        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l += 1
            store.add(s[r])
            max_len = max(max_len, r-l+1)
        return max_len