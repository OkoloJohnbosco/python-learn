from functools import reduce


temp = [0, 40, 100]


def change_temp(T):
    print((9.0/5)*T + 32)
    return (9.0/5)*T + 32


boy = map(lambda T: (9.0/5)*T + 32, temp)
map(change_temp, temp)

girl = reduce(lambda x, y: x+y, temp)
max_num = reduce(lambda a, b: a if(a > b) else b, temp)

print("my_tuple")
print(list(boy))
print(girl)
print(max_num)
