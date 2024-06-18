import random

def active_generator(num):
    array = [None] * num
    for i in range(num):
        array[i] = random.randint(0, num)
    return array