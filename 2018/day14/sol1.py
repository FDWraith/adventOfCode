inputValue = 157901
recipeScores = [3, 7]

elfIndexes = [0, 1]

while len(recipeScores) < inputValue + 11:
    elfScores = [recipeScores[i] for i in elfIndexes]
    s = sum(elfScores)
    
    if s >= 10:
        recipeScores.append(s / 10)
        recipeScores.append(s % 10)
    else:
        recipeScores.append(s)
    
    elfIndexes = [(score + 1 + elfIndexes[i]) % len(recipeScores) for i,score in enumerate(elfScores)]
    # print recipeScores


print "".join([str(i) for i in recipeScores[inputValue:inputValue+10]])
