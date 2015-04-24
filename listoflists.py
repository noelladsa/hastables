

class ListofLists(object):

    def __init__(self):
        self.nativehash = []

    def addKeyValuePair(self,key,value):
        listKeyValue = [key,value]
        elemArray = self.searchValue(key)
        if elemArray:
            elemArray[1] = value
        else:
            self.nativehash.append(listKeyValue)


    def searchValue(self,key):
        for item in self.nativehash:
            if item[0] == key:
                return item

    def getValue(self,key):
        if key is None:
            raise Exception("Key was not set")

        element = self.searchValue(key)
        if element:
            return element[1]
        else:
            raise Exception("Key does not exist")


    def removeKey(self,key):
        if key is None:
            raise Exception("Key was not set")

        element = self.searchValue(key)
        if element:
            self.nativehash.remove(element)
        else:
            raise Exception("Key does not exist")

    def printHash(self):
        print self.nativehash




hashTable = ListofLists()
hashTable.addKeyValuePair("roommate","trash")
hashTable.addKeyValuePair("recursecenter","largerooms")
hashTable.printHash()

hashTable.addKeyValuePair("recursecenter","evenlargerooms")
value = hashTable.getValue('roommate')
print "The value is",value
hashTable.removeKey('roommate')
hashTable.printHash()


