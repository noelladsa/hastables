

class ListofLists(object):

    def __init__(self):
        self.nativehash = []

    def addKeyValuePair(self,key,value):
        listKeyValue = [key,value]
        self.nativehash.append(listKeyValue)

    def getValue(self,key):
        if key is None:
            raise Exception("Key was not set")

        for item in self.nativehash:
            if item[0] == key:
                return item[1]

    def removeKey(self,key):
        if key is None:
            raise Exception("Key was not set")

        for item in self.nativehash:
            if item[0] == key:
                self.nativehash.remove(item)

    def printHash(self):
        print self.nativehash




hashTable = ListofLists()
hashTable.addKeyValuePair("roommate","trash")
hashTable.addKeyValuePair("recursecenter","largerooms")
hashTable.printHash()
value = hashTable.getValue('roommate')
print "The value is",value
hashTable.removeKey('roommate')
hashTable.printHash()


