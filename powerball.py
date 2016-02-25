# Rishabh Shah feat. Ankur Gupta
# 2016
# Powerball Number Generator

# imports
import random
import time
import threading
import multiprocessing as mp

# welcome
print "Powerball number generator. Outputs to textfile."

threadCount = int(input("How many threads do you want to use?: "))
timesToGenerate = input("How many numbers to generate?: ")
nameNewFile = str(raw_input("Name of new file?: ")) + ".txt"
# fh = open(nameNewFile, "a")
b = """
"""
def generate(end, fileName, tID):
	print "Starting thread " + str(tID)
	fh = open(fileName,"a")

	timesDone = 1
	for i in xrange(0, end):
		possibleWhiteBalls = list(xrange(1, 70))
		possiblePowerBalls = list(xrange(1, 27))
		allWhiteBalls = []

		for i in xrange(0, 5):
			selectedWhiteBall = str(random.choice(possibleWhiteBalls))
			possibleWhiteBalls.remove(int(selectedWhiteBall))
			allWhiteBalls.append(selectedWhiteBall)
		selectedPowerBall = str(random.choice(possiblePowerBalls))
		fh.write(",".join(allWhiteBalls) + ":" + selectedPowerBall)
		time.sleep(.1)
		fh.write(b)
		completedPercentage = float(float(timesDone)/float(end)*100)
		print str(completedPercentage) #+ "% - Thread " + str(tID);
		timesDone += 1

	fh.close()	

step = int(timesToGenerate) / threadCount;
processes = [mp.Process(target=generate, args=(step, nameNewFile, i)) for i in xrange(0, threadCount)]

for p in processes:
	p.start()

for p in processes:
	p.join()