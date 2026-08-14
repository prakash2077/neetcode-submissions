class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        window = {}
        t_hash = {}
        for c in t:
            t_hash[c] = t_hash.get(c, 0) + 1
        need = len(t_hash)
        res = None
        l, have = 0, 0
        min_len = float('inf')
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in t_hash and window[s[r]] == t_hash[s[r]]:
                have += 1
            while need  == have:
                if (r-l+1) < min_len:
                    res = [l, r]
                    min_len = r-l+1
                if s[l] in t_hash:
                    if s[l] in t_hash and t_hash[s[l]] == window[s[l]]:
                        have -= 1
                window[s[l]] -= 1
                l += 1
        # print(res)
        if res:
            l, r = res
            return s[l:r+1]
        return ""
