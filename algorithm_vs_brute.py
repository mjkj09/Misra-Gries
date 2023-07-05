from pympler import asizeof
from implementation import misra_gries
import random


def brutecount(stream, k):
    n = len(stream)
    elements = []

    for h in range(n):
        if stream[h] not in elements:
            elements.append(stream[h])
    m = len(elements)

    counting = []
    for h in range(m):
        counting.append(0)

    for h in range(m):
        for j in range(n):
            if elements[h] == stream[j]:
                counting[h] += 1

    final_list = []
    for h in range(m):
        temp = []
        if counting[h] >= (n / k):
            temp.append(elements[h])
            temp.append(counting[h])
            final_list.append(temp)

    return final_list


if __name__ == '__main__':
    teststream5 = []
    for i in range(111111):
        teststream5.append(random.randint(1, 50))
    k5 = 200

    misra_result = misra_gries(teststream5, k5)
    misra_memoryusage = asizeof.asizeof(misra_result)

    brute_result = brutecount(teststream5, k5)
    brute_memoryusage = asizeof.asizeof(brute_result)

    # all you need to do is run the program and see that Misra-Gries algorithm actually works! :)

    print(f"MISRA GRIES - Numbers that occured n/k or more times are: {misra_result}")
    print(f"MISRA GRIES - Memory usage: {misra_memoryusage}")

    print(f"BRUTE - Numbers that occured n/k or more times are: {brute_result}")
    print(f"BRUTE - Memory usage: {brute_memoryusage}")
