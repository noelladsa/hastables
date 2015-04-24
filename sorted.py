

class sortedList(object):

    def __init__(self):
        self.nativehash = []

    def addKeyValuePair(self,key,value):
        if not self.nativehash:
            self.nativehash.append([key,value])
            print self.nativehash
        else:
            for i, item in enumerate(self.nativehash):
                print i
                if item[0] > key:
                    self.nativehash.insert(i, [key, value])
                    break

    def searchElement(self, key, array):
        if array:
            midpoint = len(array)/2
            if key == array[midpoint][0]:
                return array[midpoint]
            elif key > array[midpoint][0]:
                return  self.searchElement(key, array[midpoint+1:])
            else:
                return self.searchElement(key, array[:midpoint-1])
        else:
            print "uh oh, not in the array!"

    def getValue(self,key):
        if key is None:
            raise Exception("Key was not set")

        return self.searchElement(key, self.nativehash)[1]



    def removeKey(self,key):
        if key is None:
            raise Exception("Key was not set")

        for item in self.nativehash:
            if item[0] == key:
                self.nativehash.remove(item)

    def printHash(self):
        print self.nativehash







hashTable = sortedList()
hashTable.addKeyValuePair("roommate","trash")
hashTable.addKeyValuePair("recursecenter","largerooms")
hashTable.addKeyValuePair("boo","radley")
hashTable.printHash()
value = hashTable.getValue('roommate')
print "The value is",value
hashTable.removeKey('roommate')
hashTable.printHash()


