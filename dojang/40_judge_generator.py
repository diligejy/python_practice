def prime_number_generator(start, stop):
    num_list = [i for i in range(start, stop)]
    for i in num_list:
        result = True
        for j in range(2, i):
            if i % j == 0:
                result = False
        if result:
            yield i


start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=" ")
