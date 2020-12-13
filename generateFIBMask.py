import gdspy
from myGDSFunctions import *

lib = gdspy.GdsLibrary()
import numpy as np
from gdspy import CellReference


rect = gdspy.Rectangle((0,0),(2,1))
mm = 1e3
um = 1
cell = lib.new_cell('CROSSES')
centerCrossDiameter = 10*mm
centerCrossWidth = 250*um
outerCrossDiameter = 250*um
outerCrossWidth = 5*um
crossSpacing = centerCrossWidth/2 + 10*um

centerCross = createCross(centerCrossDiameter, centerCrossWidth)
outerCrossShape = createCross(outerCrossDiameter, outerCrossWidth)
outerCross = gdspy.Cell("OUTER CROSS", outerCrossShape)
crossCoordinates = outerCrossDiameter /2 + crossSpacing * np.array([1,1])
triangle = createArrow(20*um, 10*um, 3*um)

crossTopRight = createCross(outerCrossDiameter, outerCrossWidth, crossCoordinates * np.array([1,1]))
crossTopLeft = createCross(outerCrossDiameter, outerCrossWidth, crossCoordinates * np.array([-1,1]))
crossBottomRight = createCross(outerCrossDiameter, outerCrossWidth, crossCoordinates * np.array([1,-1]))
crossBottomLeft = createCross(outerCrossDiameter, outerCrossWidth, crossCoordinates * np.array([-1,-1]))

textCrossOffset = np.array([outerCrossWidth, outerCrossWidth])
topRightText = gdspy.Text("TR", 3, np.array([1,1])*crossCoordinates + textCrossOffset)
topLeftText = gdspy.Text("TL", 3, np.array([-1,1])*crossCoordinates + textCrossOffset)
bottomRightText = gdspy.Text("BR", 3, np.array([1,-1])*crossCoordinates + textCrossOffset)
bottomLeftText = gdspy.Text("BL", 3, np.array([-1,-1])*crossCoordinates + textCrossOffset)

cell.add(topRightText)
cell.add(topLeftText)
cell.add(bottomRightText)
cell.add(bottomLeftText)
cell.add(centerCross)
cell.add([crossTopRight, crossTopLeft, crossBottomRight, crossBottomLeft])

# For some god-forsaken reason references never display on the viewers that I am using,
# neither in KLayout or any other software, so I am abandoning them for now
#ref1 = gdspy.CellReference(triangleCell, rotation=45)
#cell.add(ref1)


lib.write_gds('first.gds')
#gdspy.LayoutViewer()
