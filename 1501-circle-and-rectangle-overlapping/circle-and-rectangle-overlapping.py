class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Find the closest x-coordinate in the rectangle
        closestX = max(x1, min(xCenter, x2))

        # Find the closest y-coordinate in the rectangle
        closestY = max(y1, min(yCenter, y2))

        # Calculate squared distance
        dx = xCenter - closestX
        dy = yCenter - closestY

        # Compare squared distance with squared radius
        return dx * dx + dy * dy <= radius * radius