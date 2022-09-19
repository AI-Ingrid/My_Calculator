class Operator:
    def __init__(self, operation, strength):
        self.operation = operation
        self.strength = strength

    def execute(self, element_1, element_2, debug=True):

        result = self.operation(element_1, element_2)
        print(str(element_1) + str(self.operation) + str(element_2) + " = " + str(result))
        return result
