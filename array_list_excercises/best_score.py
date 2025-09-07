lis = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
def first_second(my_list):
    # TODO
    score1, score2 = 0,0
    for score in my_list:
        if score > score1:
            score2 = score1
            score1 = score
        elif score > score2 and score != score1:
            score2 = score
    return score1,score2

print(first_second(lis))