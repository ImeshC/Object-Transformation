from turtle import *
import numpy as np
hideturtle()

def create_object(points, color='black'):
    # Create and draw an object based on a list of points.
    # Default color is black.
    pencolor(color)
    firstpoint = points[0][:2]
    speed(0)
    penup()
    goto(firstpoint)
    pendown()

    for point in points[1:]:
        goto(point[:2])

    goto(firstpoint)
    penup()

def axis():
    # Draw x and y axes.
    speed(0)
    penup()
    goto(0, -5)
    pendown()
    goto(0, 1000)
    penup()
    goto(-5, 0)
    pendown()
    goto(1000, 0)

def create_point(Point):
    # Create a point at the specified location.
    penup()
    goto(Point)
    dot(5, 'red')

def create_line(line):
    # Create and draw a line based on the line equation (y = mx + c).
    m = line[0]
    c = line[1]

    x0 = -1000
    x1 = 1000
    y0 = m * x0 + c
    y1 = m * x1 + c

    pencolor('red')
    width(3)
    penup()
    goto(x0, y0)
    pendown()
    goto(x1, y1)
    width(0)

def Rotation(Object, Angle, Print=1):
    # Rotate an object by the specified angle (in degrees).
    angle = np.radians(Angle)
    sinx = np.sin(angle)
    cosx = np.cos(angle)
    rotate_matrix = np.array([[cosx, -sinx, 0], [sinx, cosx, 0], [0, 0, 1]])
    Object = np.array(Object)
    rotate_object = []

    for obj in Object:
        rotate_object.append(rotate_matrix @ obj)

    if Print == 0:
        return rotate_object
    create_object(rotate_object, 'red')

def Translation(Object, Point, Print=1):
    # Translate an object by a specified point (x, y).
    x = Point[0]
    y = Point[1]
    trans_matrix = np.array([[1, 0, x], [0, 1, y], [0, 0, 1]])

    trans_object = []
    for obj in Object:
        obj[-1] = 1
        obj = np.array(obj)
        trans_object.append(trans_matrix @ obj)

    if Print == 0:
        return trans_object
    create_object(trans_object, 'blue')

def Scale(Object, Scale, Print=1):
    # Scale an object by the specified scaling factor.
    s = Scale
    scale_matrix = np.array([[s, 0, 0], [0, s, 0], [0, 0, 0]])
    Object = np.array(Object)

    scale_object = []
    for obj in Object:
        scale_object.append(scale_matrix @ obj)

    if Print == 0:
        return scale_object
    create_object(scale_object, 'yellow')

def Mirror(Object, axis=0, Print=1):
    # Mirror an object across the x-axis (axis=0) or y-axis (axis=1).
    mirror_matrix = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    if axis == 1:
        mirror_matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 0]])

    Object = np.array(Object)

    mirror_object = []
    for obj in Object:
        mirror_object.append(mirror_matrix @ obj)

    if Print == 0:
        return mirror_object
    create_object(mirror_object, 'orange')

def Shear(Object, x, y, Print=1):
    # Shear an object by the specified shear factors (x, y).
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]

    shear_matrix = np.array([[a, b, 0], [c, d, 0], [0, 0, 0]])
    Object = np.array(Object)

    shear_object = []
    for obj in Object:
        shear_object.append(shear_matrix @ obj)

    if Print == 0:
        return shear_object
    create_object(shear_object, 'purple')

def Arbitary_Rotate(Object, Point, Angle):
    create_point(Point)
    create_object(Object)
    point = [-x for x in Point]
    T0 = Translation(Object, point, 0)
    R = Rotation(T0, Angle, 0)
    Translation(R, Point)

def Line_Mirror(Object, line):
    c = [0, line[1]]
    angle = np.degrees(np.arctan(line[0]))
    c0 = [-x for x in c]
    create_line(line)

    T0 = Translation(Object, c0, 0)
    R0 = Rotation(T0, -angle, 0)
    M = Mirror(R0, 0, 0)
    R1 = Rotation(M, angle, 0)
    Translation(R1, c)

axis()
Points = [[50, 50, 0], [150, 50, 0], [175, 75, 0], [175, 125, 0], [145, 125, 0], [145, 155, 0], [80, 155, 0], [50, 125, 0]]
create_object(Points)

##Rotation(Points, 45)
##Translation(Points, [50, 10])
##Scale(Points, 1.5)
##Mirror(Points)
##Shear(Points, [.1,.2], [.8,1])

Arbitary_Rotate(Points, [120, 150], 78)
Line_Mirror(Points, [3, 2])

exitonclick()
