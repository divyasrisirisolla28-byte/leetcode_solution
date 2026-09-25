class Solution:
    def braceExpansionII(self, expression):
        self.s = expression
        self.i = 0

        result = self.parse()

        return sorted(result)

    def parse(self):
        # Result of the current expression
        result = set()

        # Current concatenation result
        current = {""}

        while self.i < len(self.s) and self.s[self.i] != '}':
            
            if self.s[self.i] == ',':
                # Union
                result |= current
                current = {""}
                self.i += 1

            elif self.s[self.i] == '{':
                # Parse inside braces
                self.i += 1
                part = self.parse()

                # Concatenate current with part
                new_current = set()

                for a in current:
                    for b in part:
                        new_current.add(a + b)

                current = new_current

                # Skip '}'
                self.i += 1

            else:
                # Single letter
                new_current = set()

                for word in current:
                    new_current.add(word + self.s[self.i])

                current = new_current
                self.i += 1

        # Add final concatenation
        result |= current

        return result