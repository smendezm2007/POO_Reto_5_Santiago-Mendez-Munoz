from math import sqrt, acos, atan, degrees

# -------------------- CLASE POINT -------------------- #
class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y


    def get_x(self) -> float:
        return self._x

    def set_x(self, x: float):
        self._x = x

    def get_y(self) -> float:
        return self._y

    def set_y(self, y: float):
        self._y = y

    def compute_distance(self) -> float:
        return sqrt(self._x**2 + self._y**2)

# -------------------- CLASE LINE -------------------- #
class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.start_point = start_point
        self.end_point = end_point
        self.length = self._calculate_length()

    def _calculate_length(self) -> float:
        dx = self.end_point.x - self.start_point.x
        dy = self.end_point.y - self.start_point.y
        return sqrt(dx**2 + dy**2)

# -------------------- CLASE BASE: SHAPE -------------------- #
class Shape:
    def __init__(self, vertices: list[Point] = None, edges: list[Line] = None):
        self.vertices = vertices if vertices is not None else []
        self.edges = edges if edges is not None else []
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

# -------------------- RECTANGLE -------------------- #
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


# -------------------- SQUARE -------------------- #
class Square(Rectangle):
    def __init__(self, side: float):
        self.side = side
        super().__init__(side, side)
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.inner_angles = self.compute_inner_angles()

    def compute_area(self) -> float:
        return self.side ** 2

    def compute_perimeter(self) -> float:
        return 4 * self.side

    def __str__(self):
        return (
            f"Square\n"
            f"Side: {self.side}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Inner Angles: {self.inner_angles}"
        )


# -------------------- TRIANGLE -------------------- #
class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.inner_angles = self.compute_inner_angles()

    def compute_area(self) -> float:
        return (self.a * self.b) / 2

    def compute_perimeter(self) -> float:
        return self.a + self.b + self.c

    def compute_inner_angles(self) -> list[float]:
        return [60.0, 60.0, 60.0]

    def __str__(self):
        return (
            f"Triangle\n"
            f"Sides: a={self.a}, b={self.b}, c={self.c}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Angles: {self.inner_angles}"
        )

# -------------------- ISOSCELES -------------------- #
class Isosceles(Triangle):
    def __init__(self, equal_side: float, base: float):
        self.equal_side = equal_side
        self.base = base
        super().__init__(equal_side, equal_side, base)
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.inner_angles = self.compute_inner_angles()

    def compute_area(self) -> float:
        height = sqrt(self.equal_side**2 - (self.base / 2)**2)
        return (self.base * height) / 2

    def compute_perimeter(self) -> float:
        return 2 * self.equal_side + self.base

    def compute_inner_angles(self) -> list[float]:
        height = sqrt(self.equal_side**2 - (self.base / 2)**2)
        vertex_angle = degrees(2 * acos(height / self.equal_side))
        base_angle = (180 - vertex_angle) / 2
        return [base_angle, base_angle, vertex_angle]

    def __str__(self):
        return (
            f"Isosceles Triangle\n"
            f"Equal Side: {self.equal_side}, Base: {self.base}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Inner Angles: {self.inner_angles}"
        )


# -------------------- EQUILATERAL -------------------- #
class Equilateral(Triangle):
    def __init__(self, side: float):
        self.side = side
        super().__init__(side, side, side)
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.inner_angles = self.compute_inner_angles()

    def compute_area(self) -> float:
        return (sqrt(3) / 4) * (self.side ** 2)

    def compute_perimeter(self) -> float:
        return 3 * self.side

    def compute_inner_angles(self) -> list[float]:
        return [60, 60, 60]

    def __str__(self):
        return (
            f"Equilateral Triangle\n"
            f"Side: {self.side}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Inner Angles: {self.inner_angles}"
        )


# -------------------- SCALENE -------------------- #
class Scalene(Triangle):
    def __init__(self, a: float, b: float, c: float):
        super().__init__(a, b, c)
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.inner_angles = self.compute_inner_angles()

    def compute_area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def compute_inner_angles(self) -> list[float]:
        A = degrees(acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)))
        B = degrees(acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)))
        C = 180 - A - B
        return [A, B, C]

    def __str__(self):
        return (
            f"Scalene Triangle\n"
            f"Sides: a={self.a}, b={self.b}, c={self.c}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Angles: {self.inner_angles}"
        )


# -------------------- TRIRECTANGLE -------------------- #
class Trirectangle(Triangle):
    def __init__(self, a: float, b: float):
        c = sqrt(a**2 + b**2)
        super().__init__(a, b, c)
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.inner_angles = self.compute_inner_angles()

    def compute_area(self) -> float:
        return (self.a * self.b) / 2

    def compute_inner_angles(self) -> list[float]:
        return [
            90.0,
            degrees(atan(self.b / self.a)),
            degrees(atan(self.a / self.b)),
        ]

    def __str__(self):
        return (
            f"Trirectangle\n"
            f"Sides: a={self.a}, b={self.b}, c={self.c}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Angles: {self.inner_angles}"
        )

# -------------------- TRYOUT -------------------- #
if __name__ == "__main__":
    figures = [
        Rectangle(5, 15),
        Square(6),
        Isosceles(15, 7),
        Equilateral(9),
        Scalene(6, 7, 8),
        Trirectangle(7, 9)
    ]

    for i in figures:
        print(i)
        print("---------------------------------------------")