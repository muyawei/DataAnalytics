# -*- coding:utf-8 -*-


def do_something():
    a = {"one": 1}
    b = {"two": 2}
    return a, b

if __name__ == "__main__":
    one, two = do_something()
    print one
    print two
