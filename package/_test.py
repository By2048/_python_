import pickle

p = float('nan')
print(p)
print(type(p))

print(1 > float('nan'))
print(1 < float('nan'))


class A(object):
    def __init__(self):
        self.name = '123'
        self.age = 123


a = A()

print(a)

b = pickle.dumps(a)
print(b)

data = b'\x80\x03c__main__\nA\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00123q\x04X\x03\x00\x00\x00ageq\x05K{ub.'
print(data)
print(type(data))

c = pickle.loads(data)
print(c)

print(12378794)
