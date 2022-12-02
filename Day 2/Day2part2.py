wins = {"A": "C", "B": "A", "C": "B"}
pointTable = {"A": 1, "B": 2, "C": 3}
def win(opponent, choice):
	for k, v in wins.items():
		if v == opponent:
			return k
	
def calculate(input):
	opponent = input[0]
	choice = input[1]
	if choice == "X":
		decision = wins[opponent]
		points = 0
	elif choice == "Y":
		decision = opponent
		points = 3
	else:
		decision = win(opponent, choice)
		points = 6
	points += pointTable[decision]
	return points 
	
		
#creating a list of lists to iterate over		
f = open("guide.txt", "r")
tempList = []
guideList = []
for i in f.readlines():
	for i2 in i.strip():
		tempList.append(i2.strip())
	tempList.pop(1)
	guideList.append(tempList)
	tempList = []
f.close()

#summing every match
totalPoints = 0
for i in guideList:
	totalPoints += calculate(i)
	
print(totalPoints)
