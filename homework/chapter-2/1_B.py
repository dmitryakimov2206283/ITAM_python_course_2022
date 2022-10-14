def summation(start:int, end:int):
    sum = 0
    if end < start:
        for x in range(end, start + 1):
            sum += x
    else:
        for x in range(start, end + 1):
            sum += x
    print(sum)

summation(2, 12)
summation(-4, 4)
summation(3, 2)