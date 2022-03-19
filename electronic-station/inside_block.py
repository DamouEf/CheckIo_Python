"""
When it comes to city planning it's important to understand the borders of various city structures.
Parks, lakes or living blocks can be represented as closed polygon and can be described using cartesian coordinates on a map.
We need a functionality to determine if a point (a building or a tree) lies inside the structure.
For the purpose of this mission, a city structure may be considered a polygon represented as a sequence of vertex coordinates on a plane or map.
The vertices are connected sequentially with the last vertex in the list connecting to the first.
We are given the coordinates of the point which we need to check.
If the point of impact lies on the edge of the polygon then it should be considered inside of it.
For this mission, you need to determine whether the given point lies inside the polygon.

Input: Two arguments. Polygon coordinates as a tuple of tuples with two integers each. A checking point coordinates as a tuple of two integers.
Output: Whatever the point inside the polygon or not as a boolean.
"""

from typing import Tuple
from sympy import Polygon
def is_inside(polygon: Tuple[Tuple[int, int], ...], point: Tuple[int, int]) -> bool:
    poly = Polygon(*polygon)
    return any(point in side for side in poly.sides) or poly.encloses_point(point)

if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) is True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) is False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) is True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) is False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) is True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) is False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) is True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) is False, "Eighth"
    print("All done! Let's check now")      