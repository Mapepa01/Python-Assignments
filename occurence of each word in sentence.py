def word_count(x):
    counts = dict()
    words = x.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('Mr Shoniwa is the Python Expect.'))
