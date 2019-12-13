class Disk:
    """A disk class"""

    def __init__(self, color, x, y, diameter):
        self.color = color
        self.x = x
        self.y = y
        self.diameter = diameter

    def __repr__(self):
        """Repr method for debugging"""
        return "color:{0}, x:{1}, y:{2} \n".format(self.color, self.x, self.y)

    def __eq__(self, other):
        """Equals method to compare disks"""
        if type(other) == int:
            return False
        elif self.color == other.color and self.x == other.x and \
                self.y == other.y and self.diameter == other.diameter:
            return True
        else:
            return False

    def display(self):
        """Draws the disk on a tile"""
        if self.color != "None":
            fill(self.color)
            ellipse(self.x, self.y, self.diameter, self.diameter)
