s = "If comrade Napoleon says it, it must be right."
a = [100, 200, 300]
print('a =', a)

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

if (__name__ == '__main__'):
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)
