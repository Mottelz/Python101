def fact(number):
    if not isinstance(number, int):
        raise TypeError(f"Expected a number got a {type(number)}")
    out = number
    for i in range(1, number):
        out *= i
    return out


try:
    print(fact("5"))
except TypeError:
    print("Wrong type")
