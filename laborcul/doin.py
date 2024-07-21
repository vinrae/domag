class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_width(self):
        return self.width

# Usage:
rect = Rectangle(10, 5)
print(rect.get_width())  # Output: 10
