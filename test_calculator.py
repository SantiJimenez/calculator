#!/usr/bin/env python

__author__ = "Santiago Jimenez Bonilla"
__email__ = "santijimenezbonilla@gmail.com"

"""
   Calculator built using Python 3.x
   that allows to convert infix input strings into rpn expressions
   using operators dictionary in ordern to extend the operators support
"""

import unittest
from calculator import *


test_expressions = [
    ["1plus(3*4)#3", 19.0],
    ["-1 plus ( 3 into 4) # 3", 17.0],
    ["-1 pls ( 3 into 4) # 3", ValueError],
    ["7 into 7 into6 plus 7 plus 6 plus 8 over 2 into 1", 311.0],
    ["( 48 plus 36.2) plus( 8 over 4 ) * 2", 88.2],
    ["( ( 7 plus 4 ) minus 50 ) plus ( 3 into ( 5 minus 2 ) ) over 3", -36.0]
]


class TestCalculator(unittest.TestCase):
    def testExpressionsResults(self):
        for expression in test_expressions:
            self.assertEqual(evalAsPostfix(
                expression[0]), expression[1])


if __name__ == '__main__':
    unittest.main()
