f = open("calories.txt", "r")

elves = []
curCal = 0
for i in f.readlines():
	if i == "\n":
		elves.append(curCal)
		curCal = 0
		continue
	curCal += (int(i.strip("\n")))
f.close()

curCal = 0
for i in range(3):
	maxIndex = elves.index(max(elves))
	curCal += elves.pop(maxIndex)
print(curCal)