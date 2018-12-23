# -*- coding: utf-8 -*-

from multiprocessing import Pool
import random


def prime_factor(value):
    factors = []
    for divisor in range(2, value - 1):
        quotient, remainder = divmod(value, divisor)
        if not remainder:  # remainder is not zero
            factors.extend(prime_factor(divisor))
            factors.extend((prime_factor(quotient)))
            break
    else:
        factors = [value]
    return factors


if __name__ == "__main__":
    pool = Pool()
    to_factor = [random.randint(100000, 5000000) for i in range(100)]
    results = pool.map(prime_factor, to_factor)
    for value, factor in zip(to_factor, results):
        print("The factors of {} are {}".format(value, factor))
