import gdspy
import numpy as np

pi = np.pi
deg = 180 / pi

def stringCoordinates(coordinateList):
    integratedList = np.array([])
    for i in range(len(coordinateList)):
        if i is 0:
            integratedList = np.append(integratedList, coordinateList[0])
        else:
            integratedList = np.vstack((integratedList, integratedList[i-1] + np.array(coordinateList[i])))

    return integratedList

def createCross(diameter, traceWidth, offset=np.array([0,0])):
    d = diameter
    w = traceWidth
    points = offset + np.array([-w/2, w/2]) + np.array([[0,0] , [0, (d - w)/2], [w, (d-w)/2], [w, 0],
        [(d+w)/2, 0], [(d + w)/2, -w], [w, -w],
        [w, -(d+w)/2], [0, -(d+w)/2], [0, -w],
        [-(d-w)/2, -w], [-(d-w)/2, 0], [0, 0]])
    cross = gdspy.Polygon(points)
    return cross

def createArrow(length, width, traceWidth, offset=np.array([0,0])):
    l = length
    w = width
    t = traceWidth
    coordinates = [[0,0], [0, l-t], [-(w-t)/2, -(w-t)/2], [0,t],
        [w/2, w/2], [w/2,-w/2], [0,-t], [-(w-t)/2, (w-t)/2], [0, -(l-t)], [-t, 0]]
    points = stringCoordinates(coordinates)
    print(coordinates)
    arrow = gdspy.Polygon(points)
    return arrow
