import random

def active_generator(num):
    array = [None] * num
    for i in range(num):
        array[i] = random.randint(1, num)
    return array

def limited_generator(num):
    array = [None] * num
    for i in range(num):
        array[i] = 1 - random.random()
    return array
    