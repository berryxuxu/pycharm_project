def ca(x):
	a = -5*x**5 + 69*x**2 -47
	return a
print ca(0),ca(1),ca(2),ca(3)

import math
def polygon(n, s):
    return 0.25 * n * s**2 / (math.tan(math.pi/n))

print polygon(7, 3)

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
    scale = distance / dist_to_origin
    return point_x * scale, point_y * scale

print project_to_distance(2, 7, 4)