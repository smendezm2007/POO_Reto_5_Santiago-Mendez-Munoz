from geometry.shapes.rectangle import Rectangle
from geometry.shapes.square import Square
from geometry.shapes.isosceles import Isosceles
from geometry.shapes.equilateral import Equilateral
from geometry.shapes.scalene import Scalene
from geometry.shapes.trirectangle import Trirectangle

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
