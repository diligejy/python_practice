# Generator
# Iterator는 클래스에 __iter__, __next__, 또는 __getitem__ 메서드를 구현해야 하지만
# 제너레이터는 yield키워드만 사용하면 끝


def number_generator():
    yield 0
    yield 1
    yield 2


for i in number_generator():
    print(i)
