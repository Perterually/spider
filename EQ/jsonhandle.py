# -*- coding:utf-8 -*-
def myMap(func, iterable):
    for arg in iterable:
        yield func(arg)


names = ["ana", "bob", "dogge"]
