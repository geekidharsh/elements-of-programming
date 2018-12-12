# Note : It may be assumed that the rectangles are parallel to the coordinate axis.

import collections

#creates a rectangle class
Rectangle = collections.namedtuple('Rectangle', ('x','y', 'width', 'height'))


def is_intersection(r1, r2):
	return (r1.x + r1.width >= r2.x and r1.x <= r2.x + r2.width 
		and r1.y + r1.height >= r2.y and r1.y <= r2.y + r2.height)


def intersecting_rectangle(r1, r2):
	# return the intersecting rectangle if there is an intersection between r1, r2

	if is_intersection(r1,r2):
		x_new = max(r1.x, r2.x)
		y_new = max(r1.y, r2.y)
		w_new = min(r1.x + r1.width, r2.x + r2.width) - x_new
		h_new = min(r1.y + r1.height, r2.x + r2.height) - y_new

		return Rectangle(x_new, y_new, w_new, h_new)



# test is_intersection

# pair of non intersections
r1 = Rectangle(1,1,1,4)
r2 = Rectangle(3,5,1,4)
print(is_intersection(r1, r2))

# pair of intersecting rectangles
r3 = Rectangle(1,1,4,4)
r4 = Rectangle(3,5,1,4)
print(is_intersection(r3, r4))


# test intersecting_rectangle
print(intersecting_rectangle(r3,r4))