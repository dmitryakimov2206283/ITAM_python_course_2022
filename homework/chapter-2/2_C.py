import string


def convert_to_notation(value:int, base:int):
    result = ""
    remains = value

    while value >= base:
        remains = value % base
        if remains > 9:
            result += chr(ord('A') + remains - 10)
        else:
            result += str(remains)
        value //= base

    if value > 9:
        result += chr(ord('A') + value - 10)
    else:
        result += str(value)

    return result[::-1]

print(convert_to_notation(74, 16))
print(convert_to_notation(35, 36))
print(convert_to_notation(13, 2))
    