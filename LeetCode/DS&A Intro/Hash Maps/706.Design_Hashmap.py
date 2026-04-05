class MyHashMap:

    def __init__(self):
        self.hashMap = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.hashMap[key] = value

    def get(self, key: int) -> int:
        return self.hashMap[key]

    def remove(self, key: int) -> None:
        self.hashMap[key] = -1

# ====== BEST SOLUTION ======
class MyHashMap:

    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        return self.map[key]

    def remove(self, key: int) -> None:
        if key in self.map:
            del self.map[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)