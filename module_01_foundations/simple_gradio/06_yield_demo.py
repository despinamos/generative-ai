def my_gen():
    yield 1
    yield 2
    yield 3

if __name__ == "__main__":
    a = my_gen()
    print(next(a))
    print(next(a))