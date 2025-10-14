from geometry.core.point import Point
from geometry.core.line import Line

class Shape:
    def __init__(self, vertices: list[Point] = None, edges: list[Line] = None):
        self.vertices = vertices if vertices else []
        self.edges = edges if edges else []
        self.inner_angles = []
        self.is_regular = False
        self.area = 0.0
        self.perimeter = 0.0

    def compute_area(self) -> float:
        return self.area

    def compute_perimeter(self) -> float:
        return self.perimeter

    def compute_inner_angles(self) -> list[float]:
        return self.inner_angles
