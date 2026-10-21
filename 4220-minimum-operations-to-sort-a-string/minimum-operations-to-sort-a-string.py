class Solution:
    def minOperations(self, s: str) -> int:
        # Case 1: Already sorted
        if s == "".join(sorted(s)):
            return 0
        
        n = len(s)
        # Case 2: Length 2 cannot be fixed if unsorted
        if n == 2:
            return -1
        
        min_char = min(s)
        max_char = max(s)
        
        # Case 3: Min char at start or Max char at end
        if s[0] == min_char or s[-1] == max_char:
            return 1
            
        # Case 4: Special edge cases requiring 3 operations
        if s[0] == max_char and s.count(max_char) == 1 and s[-1] == min_char and s.count(min_char) == 1:
            return 3
            
        # Fallback: Can always be done in 2 operations otherwise
        return 2