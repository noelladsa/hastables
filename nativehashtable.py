

class AssocArray(object):

    def __init__(self):
        self.nativehash = {}

    def addKeyValuePair(self,key,value):
        self.nativehash[key] = value

    def getValue(self,key):
        if key is None:
            raise Exception("Key was not set")
        return self.nativehash[key]

    def removeKey(self,key):
        if key is None:
            raise Exception("Key was not set")
        del self.nativehash[key]

    def printHash(self):
        print self.nativehash

hashTable = AssocArray()
hashTable.addKeyValuePair("roommate","trash")
hashTable.addKeyValuePair("recursecenter","largerooms")
hashTable.printHash()
value = hashTable.getValue('roommate')
print "The value is",value
hashTable.removeKey('roommate')
hashTable.printHash()


