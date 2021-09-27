items = [1, True, '3']


def Test():
    for x in items:
        print(f'{x} is a {type(x)}')

def Test2(a, b):
    show = a * b
    return show

Test()
print(Test2(3, 'true'))