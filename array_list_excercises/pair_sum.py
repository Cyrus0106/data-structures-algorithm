def pair_sum(myList, sum):
    output = []
    seen = set()
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == sum:
                pair = tuple(sorted((myList[i], myList[j])))
                if pair not in seen:
                    output.append(f"{pair[0]}+{pair[1]}")
                    seen.add(pair)
    return output

print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))

