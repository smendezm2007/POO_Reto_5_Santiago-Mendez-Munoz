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
