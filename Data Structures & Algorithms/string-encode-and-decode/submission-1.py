class Solution:

    def encode(self, strs: List[str]) -> str:
        op = " "
        for i in strs:
            op += str(len(i)) + "#" + i
        return op


    def decode(self, s: str) -> List[str]:
        op = []
        while s:
            index = s.find("#")
            num = int(s[:index])
            op_str = s[index + 1 : num + index + 1]
            op.append(op_str)
            s = s[num + index + 1:]
            return op