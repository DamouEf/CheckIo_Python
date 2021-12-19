"""
This is a mission to check the similarity of two triangles.
You are given two lists as coordinates of vertices of each triangle.
You have to return a bool. (The triangles are similar or not)

Input:

Two lists as coordinates of vertices of each triangle.
Coordinates is three tuples of two integers.
Output: True or False.

Precondition:
-10 ≤ x(, y) coordinate ≤ 10
"""


from math import sqrt
from typing import List, Tuple
Coords = List[Tuple[int, int]]

def calculate_distance(a: tuple, b: tuple) -> float:
    '''
    this function takes 2 coords of 2 points and calculate the distance between them

    params : 
        * a : tuple (x,y) 
        * b : tuple (x,y) 
    '''
    x1,y1 = a
    x2,y2 = b

    distance: float = sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return distance
    

def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:

    # your code here
    A,B,C = coords_1
    A1,B1,C1 = coords_2

    distance_1 = [
        calculate_distance(A,B),
        calculate_distance(A,C),
        calculate_distance(B,C),
    ]
    distance_2 = [
        calculate_distance(A1,B1),
        calculate_distance(A1,C1),
        calculate_distance(B1,C1),
    ]
 
    return (len(set(sorted(distance_1)[i] / sorted(distance_2)[i] for i in range(3))) == 1)

if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    assert similar_triangles([[3,1],[2,1],[4,2]],[[2,0],[9,0],[-5,7]]) is False , 'last one' 
    print("Coding complete? Click 'Check' to earn cool rewards!")