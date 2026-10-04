class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            prefix = len(s)
            res += str(prefix) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        length = ""
        while(i < len(s)):
            if s[i] != "#":
                length += s[i]
                i += 1
            else:
                length = int(length)
                res.append(s[i+1: i+length+1])
                i = i+length+1
                length = ""
        return res
            