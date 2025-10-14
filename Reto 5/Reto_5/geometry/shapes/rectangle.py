from geometry.shapes.shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__()
        self.width = width
        self.height = height
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.inner_angles = self.compute_inner_angles()

    def compute_area(self) -> float:
        return self.width * self.height

    def compute_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def compute_inner_angles(self) -> list[float]:
        return [90.0] * 4

    def __str__(self):
        return (
            f"Rectangle\n"
            f"Width: {self.width}, Height: {self.height}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Inner Angles: {self.inner_angles}"
        )
