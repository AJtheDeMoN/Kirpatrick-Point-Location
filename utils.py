from math import atan2, degrees, sqrt
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

def point_on_line_segment(p, q, r):
    return q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and \
           q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])

def line_length(p, q):
    if not isinstance(p, tuple) or not isinstance(q, tuple):
        return 0
    return sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)


def in_help(p, a, b, c):
    v0 = np.array(c) - np.array(a)
    v1 = np.array(b) - np.array(a)
    v2 = np.array(p) - np.array(a)
    det = np.linalg.det([v0, v1])
    if det == 0:
        return False
    u = np.linalg.det([v2, v1]) / det
    v = np.linalg.det([v0, v2]) / det
    
    return u >= 0 and v >= 0 and u + v <= 1

@dataclass
class Point:
    x: float
    y: float
    def __add__(self, other):
        if not isinstance(other, Point):
            raise ValueError("Unsupported operand type for +")
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise ValueError("Unsupported operand type for -")
        return Point(self.x - other.x, self.y - other.y)

    def __truediv__(self, scalar: int):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Scalar must be a number")
        return Point(self.x / scalar, self.y / scalar)
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

class Polygon:
    def __init__(self, *vertices):
        if len(vertices) < 3:
            raise ValueError("Polygon must have at least 3 sides")

        self.V = [pt if isinstance(pt, Point) else Point(pt[0], pt[1]) for pt in vertices]
        self.n = len(self.V)
        self.E = [(self.V[i], self.V[(i + 1) % self.n]) for i in range(self.n)]

    def __repr__(self) -> str:
        return f"Polygon({self.V})"

    def __str__(self) -> str:
        return f"{self.V}"
    
    def __eq__(self, other: object) -> bool:
        return self.V == other.V

    def __hash__(self) -> int:
        return hash(self.__repr__())
    
def inside_polygon(A: Point, P: Polygon) -> bool:
    [vertex_a, vertex_b, vertex_c] = [edge[0] for edge in P.E]
    vector_a = Point(vertex_a.x - A.x, vertex_a.y - A.y)
    vector_b = Point(vertex_b.x - A.x, vertex_b.y - A.y)
    vector_c = Point(vertex_c.x - A.x, vertex_c.y - A.y)

    determinant = (
        (vector_a.x * vector_a.x + vector_a.y * vector_a.y) * (vector_b.x * vector_c.y - vector_c.x * vector_b.y) -
        (vector_b.x * vector_b.x + vector_b.y * vector_b.y) * (vector_a.x * vector_c.y - vector_c.x * vector_a.y) +
        (vector_c.x * vector_c.x + vector_c.y * vector_c.y) * (vector_a.x * vector_b.y - vector_b.x * vector_a.y)
    )

    return determinant > 0


def getcommon(pts: list[Point], interior=None) -> list[Point]:
    def custom_sort(point, center):
        angle = degrees(atan2(point.x - center.x, point.y - center.y)) + 360 % 360
        return angle
    cent = sum(pts, Point(0, 0)) / len(pts)
    if interior is not None:
        cent = interior
    
    pts.sort(key=lambda a: custom_sort(a, cent), reverse=True)
    return pts          

def point_in_triangle(pt: Point, poly: Polygon) -> bool:
    def check(p1, p2, p3):
        return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

    v1 = poly.V[0]
    v2 = poly.V[1]
    v3 = poly.V[2]
    
    is_neg = (check(pt, v1, v2) < 0) or (check(pt, v2, v3) < 0) or (check(pt, v3, v1) < 0)
    is_pos = (check(pt, v1, v2) > 0) or (check(pt, v2, v3) > 0) or (check(pt, v3, v1) > 0)

    return not(is_neg and is_pos)
