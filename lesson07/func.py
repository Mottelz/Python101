def greet():
    print('hi!')


def greet_by_name(name=None):
    if name:
        print(f'Hello, {name}')
    else:
        greet()


def fact(number):
    out = number
    for i in range(1, number):
        out *= i
    return out


print(fact(5))
print(fact(90))
print(fact(678))
print(fact(2))
print(fact(54))

