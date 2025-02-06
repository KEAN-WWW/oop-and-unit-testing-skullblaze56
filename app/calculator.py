class Calculator:
    @staticmethod
    def add(val1: int, val2: int) -> float:
        return float(val1 + val2)

    @staticmethod
    def subtract(val1: int, val2: int) -> float:
        return float(val1 - val2)

    @staticmethod
    def multiply(val1: int, val2: int) -> float:
        return float(val1 * val2)

    @staticmethod
    def divide(val1: int, val2: int) -> float:
        if val2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return float(val1 / val2)
