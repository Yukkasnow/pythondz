from functools import wraps

def value_chek(l_func):
    def _value_check(func):
        @wraps(func)
        def wrapper(num):
            if l_func(num):
                result=func(num)
            else:
                raise ValueError(f'wrong value {num}')
            return result
        return wrapper
    return _value_check

@value_chek(lambda x: x>0)
def calc_cube(x):
    return x**3
a=calc_cube(-5)
print(a)