# extremely simple implementation with python list instead of linked list
class MyHashMap:
    def __init__(self):
        self.table_size = 100
        self.table = [[] for x in range(self.table_size)] 

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        # iterate through list at hash table index, making sure key isn't already there
        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                self.table[idx][i] = (key, value) 
                return
        # key wasn't there, so append KV to list
        self.table[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = self.hash(key)
        # iterate through list at hash table index, looking for key 
        for item in self.table[idx]:
            if item[0] == key:
                return item[1]
        # key not found
        return -1
        

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        # iterate through list at index, looking for key, and removing element if there
        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                self.table[idx].pop(i)
                return

        return

    def hash(self, key: int) -> int:
        # simple mod-based hash function
        return key % self.table_size