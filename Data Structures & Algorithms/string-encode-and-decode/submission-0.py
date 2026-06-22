class Solution:

    def encode(self, strs: List[str]) -> str:
        op = " "
        for i in strs:
            op += str(len(i)) + "#" + i
        return op


    def decode(self, s: str) -> List[str]:
        op = []
        while i:
            index = i.find("#")
            num = int(i[:index])
            op_str = i[index + 1 : num + index + 1]
            op.append(op_str)
            i = i[num + index + 1:]
            return op