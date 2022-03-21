class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]


    # hash function to get the index of the particular key!
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        
        return h % self.MAX
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
                break
        
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

if __name__ == "__main__":
    t = HashTable()
    t['march 6'] = 130
    del t['march 6']
    print(t['march 6'])