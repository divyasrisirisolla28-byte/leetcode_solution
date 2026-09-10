class Solution:
    def elevatorRequests(self, n: int, requests: List[int]) -> int:
        current = 0
        total_time = 0

        for floor in requests:
            total_time += abs(current - floor)
            current = floor

        return total_time