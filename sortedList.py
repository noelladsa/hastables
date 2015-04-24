

class sortedList(object):

    def __init__(self):
        self.nativehash = []

    def addKeyValuePair(self,key,value):
        if not self.nativehash:
            self.nativehash.append([key,value])
           # print self.nativehash
        else:
            # print self.nativehash
            index, element = self.searchElement(key, self.nativehash)
            print "Index,element",index,element
            if element:
                self.nativehash[index][1] = value
            else:
                for i, item in enumerate(self.nativehash):
                    if item[0] > key:
                        self.nativehash.insert(i, [key, value])
                        break

    def searchElement(self, key, array):
        #print "Array is",array,"Key",key
        if array:
            midpoint = len(array)/2
            if key == array[midpoint][0]:
                return midpoint, array[midpoint]
            elif key > array[midpoint][0]:
                # print "Midpoint",midpoint,"Slice",array[midpoint+1:]
                return  self.searchElement(key, array[midpoint+1:])
            else:
                # print "Midpoint",midpoint,"Slice",array[:midpoint-1]
                return self.searchElement(key, array[:midpoint])
        else:
            print "uh oh, not in the array!"

        return None,None

    def getValue(self,key):
        if key is None:
            raise Exception("Key was not set")

        index,element = self.searchElement(key, self.nativehash)
        return element[1]



    def removeKey(self,key):
        if key is None:
            raise Exception("Key was not set")

        index,item = self.searchElement(key, self.nativehash)
        self.nativehash.remove(item)

    def printHash(self):
        print self.nativehash


hashTable = sortedList()
print "Adding roomate,trash"
hashTable.addKeyValuePair("roommate","trash")
hashTable.printHash()

print "Adding recursecenter,largerooms"
hashTable.addKeyValuePair("recursecenter","largerooms")
hashTable.printHash()
print "Adding boo,radley"
hashTable.addKeyValuePair("boo","radley")
hashTable.printHash()
print "Adding boo,radley2"
hashTable.addKeyValuePair("boo","radley2")
hashTable.printHash()
value = hashTable.getValue('roommate')
print "The value is",value
hashTable.removeKey('roommate')
hashTable.printHash()


