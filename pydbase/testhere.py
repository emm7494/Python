from itertools import chain
from functools import update_wrapper, wraps


class CountCalls(object):
    __instances = {}

    def __init__(self, f):
        self.__f = f
        self.__num_calls = 0
        # type(self).__instances[f] = self is an alternative
        self.__class__.__instances[f] = self
        update_wrapper(self, f)

    def __call__(self, *args, **kwargs):
        self.__num_calls += 1
        return self.__f(*args, **kwargs)

    def count(self):
        return self.__num_calls

    @classmethod
    def counts(cls):
        return dict(
            [
                (f.__name__, cls.__instances[f].__num_calls)
                for f in cls.__instances
            ]
        )


def parcheck(*types):
    def decorator(fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            for _type, _arg in zip(types, args):
                print(f'Parameter "{_arg}" is of type "{_type}".')
                assert isinstance(
                    _arg, _type
                ), f'Parameter type check failed for input value:"{_arg}" as "{_type.__name__}"; input value:"{_arg}" is of type "{type(_arg).__name__}"!'
            return fn(*args, **kwargs)
        return inner
    return decorator


@parcheck(int)
@CountCalls
def foo(num):
    print(num)


@CountCalls
def bar(word):
    print(word)


@CountCalls
def baz():
    pass


@parcheck(int, int, int)
def sum(x, y, z):
    return f'The sum of x, y and z is "{x + y + z}".'


def yield_factors_of(num_0):
    from math import sqrt
    return ((num_1, num_0//num_1) for num_1 in range(1, int(sqrt(num_0))+1) if num_0 % num_1 == 0)


def main():
    it = chain(*yield_factors_of(100))
    print(sorted(set(it), key=abs, reverse=True))
    # print(sum(1, 2, 3))
    # foo('cat')
    # for i in range(1):
    #     foo('foo 99'), bar('bar, hi')
    # for i in range(1):
    #     bar('bar, tEsT')
    # print(foo.count())
    # print(bar.count())
    # print(CountCalls.counts())
    # obj = CountCalls(foo)
    # print(obj.__name__)
    # obj(77)
    # print(type(obj))
    # obj2 = CountCalls(baz)
    # print(obj2.__name__)
    # obj2()
    # obj2()
    # obj2()
    # print(CountCalls.counts())


if __name__ == "__main__":
    main()
