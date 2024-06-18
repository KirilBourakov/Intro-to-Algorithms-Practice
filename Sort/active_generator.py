import random

def active_generator(num):
    length = [None] * num
    for i in range(num):
        length[i] = random.randint(0, num)
    return num