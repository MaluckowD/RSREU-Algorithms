# Тестировщик
from os import popen
from random import randint

i = 1
while True:
    test_ = [str(randint(1,200)) for _ in range(randint(1, 200))]
    test = " ".join(test_)
    slow = popen("echo {} | python slow.py".format(test)).read()
    candidate = popen("echo {} | python candidate.py".format(test)).read()

    if slow != candidate:
        print(f"{i}) !!!WA: slow: {slow}, candidate: {candidate}")
        break
    else:
        print(f"{i}) Ok")
    i += 1

