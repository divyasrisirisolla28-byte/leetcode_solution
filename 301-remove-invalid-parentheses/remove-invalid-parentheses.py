class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(x):
            count = 0

            for ch in x:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        result = []
        queue = [s]
        visited = {s}
        found = False

        while queue:
            current = queue.pop(0)

            if isValid(current):
                result.append(current)
                found = True

            # Once we find valid strings, don't remove more characters
            if found:
                continue

            for i in range(len(current)):
                if current[i] not in '()':
                    continue

                new_string = current[:i] + current[i + 1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return result