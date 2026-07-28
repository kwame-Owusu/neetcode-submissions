class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashtable = [None] * capacity


    def insert(self, key: int, value: int) -> None:        
        index = key % self.capacity
        while True:
            if self.hashtable[index] == None:
                self.hashtable[index] = Pair(key, value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.resize()
                return
            elif self.hashtable[index].key == key:
                self.hashtable[index].val = value
                return
            
            index = (index + 1) % self.capacity
        

    def get(self, key: int) -> int:
        index = key % self.capacity

        while self.hashtable[index] != None:
            if self.hashtable[index].key == key:
                return self.hashtable[index].val
            index = (index + 1) % self.capacity
        return -1

    def remove(self, key: int) -> bool:
        index = key % self.capacity
        while self.hashtable[index] != None:
            if self.hashtable[index].key == key:
                self.hashtable[index] = None
                self.size -= 1
                
                # Rehash subsequent keys to fill the hole created
                curr = (index + 1) % self.capacity
                while self.hashtable[curr] != None:
                    pair_to_rehash = self.hashtable[curr]
                    self.hashtable[curr] = None
                    self.size -= 1
                    self.insert(pair_to_rehash.key, pair_to_rehash.val)
                    curr = (curr + 1) % self.capacity
                return True
            index = (index + 1) % self.capacity
        return False
       
    
    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity 

    def resize(self) -> None:
        old_hashtable = self.hashtable
        self.capacity = 2 * self.capacity
        self.hashtable = [None] * self.capacity
        self.size = 0
        for pair in old_hashtable:
            if pair:
                self.insert(pair.key, pair.val)