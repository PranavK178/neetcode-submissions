class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += s
            output += "`"
        return output
    def decode(self, s: str) -> List[str]:
        output = []
        l = 0
        r = 0
        empty = s.count("`")
        print(empty)
        while l < len(s):
            while s[r] != "`" and r < len(s):
                r += 1
            output.append(s[l: r])
            l = r + 1
            r = l

        if len(output) == 0:
            return [""] * (empty)
        return output

        
