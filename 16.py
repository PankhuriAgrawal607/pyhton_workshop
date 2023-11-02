score=0 #global score
def increase_score(points):
    global score
    score+=points
increase_score(10)
print("score:", score)