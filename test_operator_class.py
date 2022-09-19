import unittest
import numpy as np
from operator_class import Operator


class TestOperator(unittest.TestCase):

    def test_execute(self):
        add_op = Operator(np.add, 0)
        multiply_op = Operator(np.multiply, 1)

        print("Calculating: 1 + ( 2 * 3 )")

        result = add_op.execute(1, multiply_op.execute(2, 3))

        self.assertEqual(result, 7, " should be 7 ")


