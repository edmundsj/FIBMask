import unittest
import sys
from myGDSFunctions import stringCoordinates
import numpy as np

sys.path.append('test')

class TestStuff(unittest.TestCase):
    def testStringCoordinates(self):
        inputCoordinates = np.array([[0,0],[1,1],[2,2]])
        outputActual = np.array([[0,0], [1, 1], [3, 3]])
        outputCalculated = stringCoordinates(inputCoordinates)
        np.testing.assert_array_equal(outputActual, outputCalculated)

