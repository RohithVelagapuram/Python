import calendar

yy = 2001
mm = 10
print(calendar.month(yy, mm))

l = [5, 6, 7, 8]
l[1:3] = [1, 2, 3]
print(l)


@lambda _: _()
def _():
    print("_")


def fun(num):
    if num > 10:
        return num - 10
    return fun(fun(num + 11))


print(fun(5))
