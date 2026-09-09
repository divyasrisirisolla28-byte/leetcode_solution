class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            valid = True
            for digit in str(num):
                d = int(digit)
                if d == 0 or num % d != 0:
                    valid = False
                    break
            if valid:
                ans.append(num)
        return ans
        