class Binary:
    base = 2

    def __init__(self, num):
        self.binary_num = Binary.convert_to_binary(num)

    def empty():
        bin = Binary(0)
        bin.binary_num = []
        return bin

    def __add__(self, other):
        result = Binary.empty()
        result.binary_num = self.add(other)
        return result

    def add(self, other):
        remains = 0
        result = []
        bin_num = self.binary_num
        other_bin_num = other.binary_num

        self_len = len(self.binary_num)
        other_len = len(other.binary_num)

        offset = abs(self_len - other_len)

        i = 0
        remainder_index = -1
        if self_len >= other_len:
            while i < self_len - offset:
                sum = bin_num[i] + other_bin_num[i] + remains
                if (sum > self.base):
                    result.append(0)
                    remains += sum - 1
                else:
                    result.append(sum)
                if remains > 0:
                    remains -= 1
                i += 1
            
            remainder_index = i - 1
            while i < self_len:
                result.append(bin_num[i])
                i += 1
        else:
            while i < other_len - offset:
                sum = bin_num[i] + other_bin_num[i] + remains
                if (sum > self.base):
                    result.append(0)
                    remains = sum - 1
                else:
                    result.append(sum)
                if remains > 0:
                    remains -= 1
                i += 1
            
            remainder_index = i - 1
            while i < other_len:
                result.append(other_bin_num[i])
                i += 1

        while remains > 0:
            sum = bin_num[remainder_index] + remains
            if (sum > self.base):
                result.append(0)
                remains += sum - 1

                if (remainder_index == self_len - 1):
                    result.append(1)
            else:
                result.append(sum)
            if remains > 0:
                remains -= 1
            remainder_index += 1

        return result

    def __sub__(self, other):
        result = Binary.empty()
        result.binary_num = self.sub(other)
        return result

    def sub(self, other):
        result = []
        bin_num = self.binary_num
        other_bin_num = other.binary_num

        self_len = len(self.binary_num)
        other_len = len(other.binary_num)
        sub_offset = abs(self_len - other_len)

        # 1000 - 0100 = 0100
        i = 0
        remains = 0
        while i < self_len - sub_offset:
            diff = bin_num[i] - other_bin_num[i] - remains
            if diff < 0 and i < self_len - 1:
                result.append(1)
                remains += 1
            else:
                result.append(diff)
            i += 1

        # while remains > 0:
        #     result.append(remains)
        #     remains -= 1
        
        # while i < self_len:
        #     result.append(bin_num[i] - remains)
        #     i += 1

        return result

    def __mul__(self, other):
        result = Binary.empty()
        result.binary_num = self.mul(other)
        return result

    def mul(self, other):
        result_bin = Binary.empty()
        bin_num = self.binary_num
        other_bin_num = other.binary_num

        self_len = len(self.binary_num)
        other_len = len(other.binary_num)
        
        # First multiplication
        for x in bin_num:
            mult = x * other_bin_num[0]
            result_bin.binary_num.append(mult)

        # Multiplication with addition
        if other_len > 1:
            for i in range(1, other_len):
                result_bin.binary_num.insert(0, 0)
                mult_bin = Binary.empty()
                for x in bin_num:
                    mult = x * other_bin_num[i]
                    mult_bin.binary_num.append(mult)
                result_bin = result_bin + mult_bin

        result_bin.binary_num = result_bin.binary_num[::-1]
        return result_bin.binary_num

    def __floordiv__(self, other):
        result = Binary.empty()
        result.binary_num = self.floordiv(other)
        return result

    def floordiv(self, other):
        bin_num = self.binary_num
        other_bin_num = other.binary_num

        self_len = len(self.binary_num)
        other_len = len(other.binary_num)

        substract_count = 0
        minuend = Binary.empty()
        for x in bin_num:
            minuend.binary_num.append(x)
        while not minuend < other:
            minuend = minuend - other
            substract_count += 1
        return Binary(substract_count).binary_num

    def __lt__(self, other):
        if len(self.binary_num) > len(other.binary_num):
            return False
        elif len(self.binary_num) < len(other.binary_num):
            return True

        for i in range(len(self.binary_num) - 1, -1, -1):
            if self.binary_num[i] > other.binary_num[i]:
                return False
            elif self.binary_num[i] < other.binary_num[i]:
                return True
        return False

    def __gt__(self, other):
        if len(self.binary_num) < len(other.binary_num):
            return False
        elif len(self.binary_num) > len(other.binary_num):
            return True

        for i in range(len(self.binary_num) - 1, -1, -1):
            if self.binary_num[i] < other.binary_num[i]:
                return False
            elif self.binary_num[i] > other.binary_num[i]:
                return True
        return False

    def __str__(self):
        result = ""
        for x in self.binary_num[::-1]:
            result += str(x)
        return result

    @classmethod
    def convert_to_binary(cls, value:int):
        result = []
        remains = value

        while value >= cls.base:
            remains = value % cls.base
            result.append(remains)
            value //= cls.base

        result.append(value)

        # Keep in mind that it's inverted
        # Lowest bit is at 0 index in list
        return result