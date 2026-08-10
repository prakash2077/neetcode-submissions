class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            n = len(s)
            res += str(n) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        if s: 
            n = 0
            temp = ""
            word = ""
            i = 0
            while i < len(s):
                c = s[i]
                if c == "#":
                    n = int(temp)
                    while(n > 0 and i+1 < len(s)):
                        i += 1
                        c = s[i]
                        word += c
                        n -= 1
                    res.append(word)
                    word = ""
                    temp = ""
                else:
                    temp += c
                i += 1
            return res
        else:
            return []