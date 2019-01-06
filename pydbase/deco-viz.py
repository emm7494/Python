def func_1(fn):
    print('func_1 enter!!!')

    def func_1_inner():
        print('\t\t inner_1 enter!!!\n')
        gn = fn()
        print('\t\t inner_1 exit!!!\n\n')
        return gn
    print('func_1 exit!!!\n')
    return func_1_inner


def func_2(fn):
    print('func_2 enter!!!')

    def func_2_inner():
        print('\t inner_2 enter!!!\n\n')
        gn = fn()
        print('\t inner_2 exit!!!\n\n\n')
        return gn
    print('func_2 exit!!!\n')
    return func_2_inner


def func_3(fn):
    print('func_3 enter!!!')

    def func_3_inner():
        print('inner_3 enter!!!\n\n\n')
        gn = fn()
        print('inner_3 exit!!!\n')
        return gn
    print('func_3 exit!!!\n')
    return func_3_inner


@func_3
@func_2
@func_1
def func():
    print('\t\t\t func here!!!\n')


if __name__ == '__main__':
    func()
