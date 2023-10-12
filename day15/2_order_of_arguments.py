# The order of arguments in a python function must be as follows:
# 1. Positional Arguments
# 2. Keyword / Default Arguments
# 3. *args
# 4. **kwargs

def addition(a, b, c, d=2, e=3, *args, **kwargs):
    print(a)  # 1
    print(b)  # 2
    print(c)  # 3
    print(d)  # 4
    print(e)  # 5
    print(args)  # (6, 7, 8, 9)
    print(kwargs)  # {"x": 3, "y": 4, "z": 3}


addition(1, 2, 3, 4, 5, 6, 7, 8, 9, x=3, y=4, z=3)

