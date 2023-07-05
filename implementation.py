def misra_gries(stream, k):
    """
    This function finds the elements that occur in the stream more than n/k times.

    Parameters:
    stream (list): our input stream
    k (int): factor responsible for the number of entries that will be stored in the associative array

    Returns:
    dictionary: sorted by frequency of the values which are keys here

    """
    n = len(stream)
    d1 = {}
    d2 = {}

    for j in range(n):
        m = len(d1)  # number of individual values in the stream

        if m < k:
            if stream[j] in d1:
                d1[stream[j]] += 1
            else:
                d1[stream[j]] = 1

        else:
            if stream[j] in d1:
                d1[stream[j]] += 1
            else:
                for key in list(d1.keys()):
                    d1[key] -= 1
                    if d1[key] == 0:
                        del d1[key]

    for key in list(d1.keys()):
        d2[key] = 0

    for j in range(n):
        if stream[j] in d2:
            d2[stream[j]] += 1

    for key in list(d2.keys()):
        if d2[key] < (n / k):
            del d2[key]

    sorted_dict = {j: v for j, v in sorted(d2.items(), key=lambda x: x[1], reverse=True)}
    return sorted_dict


if __name__ == '__main__':
    teststream1 = [1, 4, 5, 4, 4, 5, 4, 4]
    k1 = 2
    print(f"TEST 1: Numbers that occured n/k or more times are: {misra_gries(teststream1, k1)}")
    # result is: {4: 5}

    teststream2 = [1, 2, 3, 3, 3, 4, 5, 6]
    k2 = 2
    # n/k equals 4, and the most common element is 3 (that occured 3 times)...
    print(f"TEST 2: Numbers that occured n/k or more times are: {misra_gries(teststream2, k2)}")
    # ... that's why result is: {}

    teststream3 = [1, 11, 1, 11, 1, 11, 11]
    k3 = 3
    print(f"TEST 3: Numbers that occured n/k or more times are: {misra_gries(teststream3, k3)}")
    # result is: {11: 4, 1: 3}

    with open("lyrics.txt", "rt", encoding="utf8") as file:
        lyrics = []
        for line in file:
            listoflyrics = line.split()
            lyrics.append(listoflyrics)

    teststream4 = []
    for i in lyrics:
        teststream4 += i
    k4 = 50

    print(f"TEST 4: Words that occured n/k or more times are: {misra_gries(teststream4, k4)}")
