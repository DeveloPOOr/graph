import matplotlib.pyplot as plt
import random


def quicksort(nodes, degree):
    if len(nodes) <= 1:
        return nodes
    else:
        q = random.choice(nodes)

    left, middle, right = (list() for _ in range(3))
    for n in nodes:
        if degree[n] > degree[q]:
            left.append(n)
        if degree[n] < degree[q]:
            right.append(n)
        if degree[n] == degree[q]:
            middle.append(n)

    return quicksort(left, degree) + middle + quicksort(right, degree)
