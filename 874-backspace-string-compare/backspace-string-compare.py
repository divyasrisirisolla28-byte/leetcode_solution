class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for ch in s:
            if ch != "#" :
                s1.append(ch)
            elif s1:
                s1.pop()
        for ch in t:
            if ch != '#':
                s2.append(ch)
            elif s2:
                s2.pop()
        return s1 == s2
        