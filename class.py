class DevTest1:
    def __init__(self, odd, even, zero):
        self.odd = odd
        self.even = even
        self.zero = zero


show = DevTest1('123', '234', '0')

print(show.odd)
print(show.even)
print(show.zero)