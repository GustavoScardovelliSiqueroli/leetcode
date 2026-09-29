"""
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        last = "("
        open = 0
        close = 0
        max_depth = 0
        for i in s:
            if i in ("(", ")"):
                if i == "(":
                    open += 1
                else:
                    close += 1

                if last == "(" and i == ")":
                    saldo = open - close + 1
                    if saldo > max_depth:
                        max_depth = saldo

                last = i
        return max_depth


print(Solution().maxDepth("(1+(2*3)+((8)/4))+1"))

print(Solution().maxDepth("(1)+((2))+(((3)))"))

print(Solution().maxDepth("()(())((()()))"))

print(Solution().maxDepth(""))
