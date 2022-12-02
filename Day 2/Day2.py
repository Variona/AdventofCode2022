
wins = {"A": "Z", "B": "X", "C": "Y"}
draws = {"A": "X", "B": "Y", "C": "Z"}
pointTable = {"X": 1, "Y": 2, "Z": 3}
def draw(opponent, you):
	if draws[opponent] == you:
		return True
	return False
	

def win(opponent, you):
	if you == wins[opponent]:
		return 0
		
	return 6

def calculate(input): #could prob merge this function with win()
	opponent = input[0]
	you = input[1]
	points = pointTable[you]
	
	if not draw(opponent, you):
		points += win(opponent, you)
	else:
		points += 3
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
