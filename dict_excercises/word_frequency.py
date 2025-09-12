def count_word_frequency(words):
    freq = {}
    for word in words:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    return freq

print(count_word_frequency(['apple', 'orange', 'banana', 'apple', 'orange', 'apple']))