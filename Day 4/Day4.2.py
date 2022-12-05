def intifier(input):
	inputList = []
	for i in input.split("-"):
		inputList.append(int(i))
	return inputList

def rangeAnalyzer(input1, input2):
	if input1[0] <= input2[0] and input1[1] >= input2[0]:#parenthesis are a hell of a drug
		return True
	elif input2[0] <= input1[0] and input2[1] >= input1[0]:
		return True
	
def pairChecker(input):
	pair1, pair2 = intifier(input[0]), intifier(input[1])
	if rangeAnalyzer(pair1, pair2):
		return True

pairs = []
f = open("assignments.txt", "r")
for i in f.readlines():
	pairs.append(i.strip())
f.close()

partedPairs = []
for i in pairs:
	partedPairs.append(i.split(","))
	
counter = 0
for i in partedPairs:
	if pairChecker(i):
		counter += 1
print(counter)
