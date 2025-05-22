class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        i = 0
        while len(tokens) > 1:
            if tokens[i] in "+-*/":
                if tokens[i] == "/":
                    new = int(int(tokens[i - 2]) / int(tokens[i - 1]))
                elif tokens[i] == "*":
                    new = int(tokens[i - 2]) * int(tokens[i - 1])
                elif tokens[i] == "+":
                    new = int(tokens[i - 2]) + int(tokens[i - 1])
                else:
                    new = int(tokens[i - 2]) - int(tokens[i - 1])
                tokens.pop(i)
                tokens.pop(i - 1)
                tokens.pop(i - 2)
                tokens.insert(i - 2, str(new))
                i = 0
            i += 1
        return int(tokens[0])

sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]))