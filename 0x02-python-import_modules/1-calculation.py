#!/user/bin/python3
from audioop import add


if __name__ == "__main__":
    from calculator_1 import mul, div, add
    a = 10
    b = 5
    print(f"{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print(f"{:d} * {:d} = {:d}".format(a, b, sub(a, b)))
    print(f"{:d} - {:d} = {:d}".format(a, b, mul(a, b)))
    print(f"{:d} / {:d} = {:d}".format(a, b, div(a, b)))
