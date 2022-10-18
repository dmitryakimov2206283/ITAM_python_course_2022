from binary import Binary

class Tenary(Binary):
    def __init__(self, num):
        self.binary_num = self.convert_to_tenary(num)

    def empty():
        ten_num = Tenary(0)
        ten_num.binary_num = []
        return ten_num

    def __add__(self, other):
        result = Tenary.empty()
        result.binary_num = self.add(other)
        return result

    def __sub__(self, other):
        result = Tenary.empty()
        result.binary_num = self.sub(other)
        return result

    def __mul__(self, other):
        result = Tenary.empty()
        result.binary_num = self.mul(other)[::-1]
        return result

    def __floordiv__(self, other):
        result = Tenary.empty()
        result.binary_num = self.floordiv(other)
        return result

    def __str__(self):
        return super().__str__()

    @classmethod
    def convert_to_tenary(cls, value:int):
        cls.base = 3

        # Keep in mind that it's inverted
        # Lowest bit is at 0 index in list
        return cls.convert_to_binary(value)
