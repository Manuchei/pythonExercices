# -*- coding: utf-8 -*-
# La siguiente función trata de añadir un nuevo elemento a la tupla.
# ¿Por qué no funciona?
"""No funcionaba porque estaba entre parentesis y las listas van entre llaves"""
# ¿Cómo se puede arreglar?
"""Cambiando los corchetes por llaves"""
from random import randint
list = [1,2,3,4,5]

def add_new_random_value(list):
    list.append(randint(0,10))


def test():
    assert len(list) == 5, "Should be 5 elements"
    add_new_random_value(list)
    assert len(list) == 6, "Should be 6 elements"


if __name__ == "__main__":
    test()
    print("Everything passed")