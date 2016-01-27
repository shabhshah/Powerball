#Rishabh Shah feat Ankur Gupta
#2016
#Analyzing Powerball Data

#imports
from prettytable import PrettyTable

#welcome
fileToOpen = raw_input("File name to open?: ") + ".txt"

allWhiteBalls = []
allPowerBalls = []
whiteBallPercentages = []
powerBallPercentages = []

for line in open(fileToOpen):
	line = line.strip()

	if(len(line) >= 11 and len(line) <= 17):	
		parts = line.split(":")
		whiteBalls = parts[0]
		powerBall = parts[1]
		whiteBall = whiteBalls.split(",")
		one = whiteBall[0]
		two = whiteBall[1]
		three = whiteBall[2]
		four = whiteBall[3]
		five = whiteBall[4]
		allWhiteBalls.append(one)
		allWhiteBalls.append(two)
		allWhiteBalls.append(three)
		allWhiteBalls.append(four)
		allWhiteBalls.append(five)
		allPowerBalls.append(powerBall)

table = PrettyTable(["White ball number", "Occurance"])

x = 1
#print "White Balls:"
#print ""
for i in xrange(1,70):
	y = allWhiteBalls.count(str(x))
#	print "Number of times " + str(x) + " appears is " + str(y)
	percentage = str(float(((float(y)/float(len(allWhiteBalls)))*100)))
#	print "The percentage is " + percentage + "%"
	table.add_row([x, percentage + "%"])
	whiteBallPercentages.append(str(percentage))
	x += 1
#print ""

table2 = PrettyTable(["Power ball number", "Occurance"])
#print "Powerballs:"
a = 1
for i in xrange(1,27):
	z = allPowerBalls.count(str(a))
#	print "Number of times " + str(a) + " appears is " + str(z)
	percentage = str(float(((float(z)/float(len(allPowerBalls)))*100)))
#	print "The percentage is " + percentage + "%"
	table2.add_row([a, percentage +"%"])
	powerBallPercentages.append(str(percentage))
	a += 1
print ""

table.align["Occurance"] = "l"
table2.align["Occurance"] = "l"
print table.get_string(sortby="Occurance", reversesort=True)
print ""
print table2.get_string(sortby="Occurance", reversesort=True)
print ""

maxWhiteBallPercentage = max(whiteBallPercentages)
location = whiteBallPercentages.index(maxWhiteBallPercentage)
whiteBallPercentages.remove(maxWhiteBallPercentage)

maxWhiteBallPercentage = max(whiteBallPercentages)
location3 = whiteBallPercentages.index(maxWhiteBallPercentage)
whiteBallPercentages.remove(maxWhiteBallPercentage)

maxWhiteBallPercentage = max(whiteBallPercentages)
location4 = whiteBallPercentages.index(maxWhiteBallPercentage)
whiteBallPercentages.remove(maxWhiteBallPercentage)

maxWhiteBallPercentage = max(whiteBallPercentages)
location5 = whiteBallPercentages.index(maxWhiteBallPercentage)
whiteBallPercentages.remove(maxWhiteBallPercentage)

maxWhiteBallPercentage = max(whiteBallPercentages)
location6 = whiteBallPercentages.index(maxWhiteBallPercentage)
whiteBallPercentages.remove(maxWhiteBallPercentage)

maxPowerBallPercentage = max(powerBallPercentages)
location2 = powerBallPercentages.index(maxPowerBallPercentage)

print "The white balls to pick are: " + str(int(location)+1) + ", " + str(int(location3)+1) + ", " + str(int(location4)+1) + ", " + str(int(location5)+1) + ", " + str(int(location6)+1) + "."
print "The power ball to pick is: " + str(int(location2)+1) + "."
#only gives one value, not all, if there are more than one max value