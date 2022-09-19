import numpy as np
from function import Function


def main():
    exponential_function = Function(np.exp)
    sinus_function = Function(np.sin)
    print(exponential_function.execute(sinus_function.execute(0)))


main()
