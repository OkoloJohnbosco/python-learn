bic = ["bosco", "uche", "dad", "boy"];
# print(bic)

bic.reverse()
# print(bic)

# bic.sort()
sorted(bic)
# print(bic)

for bi in bic:
    print("i like  " + bi)

boy = list(range(1, 10))

for value in boy:
    print(value)

print(max(boy))
print(min(boy))

first_squares = []

for value in range(1,11):
    first_squares.append(value ** 2)
print(first_squares)

bossu = list(range(1, 11))
second_sqaures = [value ** 2 for value in bossu[-3:]]
print(second_sqaures)

threes = list(range(3, 31, 3))
print(threes)

names = ["chidera", "amaka", "uche", "obioma", "emeka"]
print(names[0:3])
print(names)
