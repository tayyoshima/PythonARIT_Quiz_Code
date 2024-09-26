def increment_score(score, bonus, points):
    if bonus == True:
        points = points * 2
    score = score + points
    return score
points = 5
score = 10
new_score = increment_score(score, True, points)
print(new_score)