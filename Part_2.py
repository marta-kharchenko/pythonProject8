import math


class Vector:
    def __init__(self, components):
        self.components = components

    def magnitude(self):
        return math.sqrt(self.components[0] ** 2 + self.components[1] ** 2 + self.components[2] ** 2)

    def add(self, vector):
        sum = [self.components[j]+vector.components[j] for j in range(len(self.components))]
        return Vector(sum)

    def dot_product(self, vector):
        return sum(self.components[j]*vector.components[j] for j in range(len(vector.components)))


Vector_1 = Vector([1, 2, 3])
Vector_2 = Vector([4, 5, 6])
Vector_Sum = Vector_1.add(Vector_2)
print('Sum vector:', Vector_Sum.components)
print('Length of the first vector:', Vector_1.magnitude())
print('Length of the second vector:', Vector_2.magnitude())
print('The dot product of the vectors is:', Vector_1.dot_product(Vector_2))