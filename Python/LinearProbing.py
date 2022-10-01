class HashLinearProbe:
    def __init__(self):
        self.hashtable_size = 10
        self.hashtable = [0] * self.hashtable_size

    def hashcode(self, key):
        return key % self.hashtable_size

    def lprobe(self, element):
        i = self.hashcode(element)
        j = 0
        while self.hashtable[(i+j) % self.hashtable_size] != 0:
            j = j + 1
        return (i + j) % self.hashtable_size

    def insert(self, element):
        i = self.hashcode(element)
        if self.hashtable[i] == 0:
            self.hashtable[i] = element
        else:
            i = self.lprobe(element)
            self.hashtable[i] = element

    def search(self, key):
        i = self.hashcode(key)
        j = 0
        while self.hashtable[(i+j) % self.hashtable_size] != key:
            if self.hashtable[(i+j) % self.hashtable_size] == 0:
                return False
            j = j + 1
        return True

    def display(self):
        print(self.hashtable)

HC = HashLinearProbe()
#HC.display()
HC.insert(76)
HC.insert(23)
HC.insert(41)
HC.insert(42)
HC.insert(79)
HC.insert(46)
HC.insert(32)
HC.display()
print(HC.search(32))