def summation(*args:int):
    sum = 0
    args = [-x * 2 if x < 0 else x for x in args]
    max_arg = max(args)
    for x in args:
        sum += x / max_arg
    print(sum)
summation(-10, 2, 3, 15, -4)