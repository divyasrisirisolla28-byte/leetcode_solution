class Solution:
    def reverseDegree(self, s):
        total = 0

        for i, ch in enumerate(s):
            # Reverse alphabet position: a=26, b=25, ..., z=1
            reverse_pos = 26 - (ord(ch) - ord('a'))
            
            # String position is 1-indexed
            string_pos = i + 1
            
            total += reverse_pos * string_pos

        return total