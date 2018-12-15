inputValue = "157901"
recipeScores = "37"

elfIndexes = [0, 1]

print str(inputValue)

# width = 1
while str(inputValue) not in recipeScores[-20:]:
    # print recipeScores
    
    elfScores = [int(recipeScores[i]) for i in elfIndexes]
    s = sum(elfScores)
    
    if s >= 10:
        recipeScores += str(s / 10)
        recipeScores += str(s % 10)
        # width += 2
    else:
        recipeScores += str(s)
        # width += 1
    
    elfIndexes = [(score + 1 + elfIndexes[i]) % len(recipeScores) for i,score in enumerate(elfScores)]
    # print recipeScores
    


print recipeScores.index(str(inputValue))
