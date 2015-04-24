from listoflists import ListofLists
from nativehashtable import AssocArray
from sortedList import sortedList
from timeit import Timer
import timeit
import random
import string

objLists = ListofLists()
objHash = AssocArray()
objSorted = sortedList()
hashTypes = [objLists, objHash, objSorted]

def getRandomString(N=10):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def generateRandomPairs(num_pairs=10000):
	# TODO this should create unique pairs:
	test_data = [[getRandomString(), getRandomString()] for i in range(num_pairs)]
	return test_data

test_data = generateRandomPairs()

def prepTestListofLists(hashType):
	for item in test_data:
		hashType.addKeyValuePair(item[0],item[1])

def accessTest(hashType, number):
	for i in range(number):
		hashType.getValue(test_data[random.randint(0,number-1)][0])


if __name__ == "__main__":
	print "Working! Leave me alone!"
	for hashType in hashTypes:
		print str(type(hashType)), " insertion time for 10,000: ",\
		 str(Timer(lambda: prepTestListofLists(hashType)).timeit(number=1))
		print str(type(hashType)), " access time for 10,000: ",\
		 str(Timer(lambda: accessTest(hashType, 10000)).timeit(number=1))
	print "Done!"
