import random
class RandomizedSet:

        def __init__(self):
            self.d=dict()
            self.list=[]

        def insert(self, val: int) -> bool:
            if val in self.d:
                return False
            else:
                self.list.append(val)
                self.d[val]=len(self.list)-1
                return True

        def remove(self, val: int) -> bool:
            if val in self.d:
                index=self.d[val]
                last=self.list[-1]
                self.list[index]=last
                self.d[last]=index
                self.list.pop()
                del self.d[val]
                return True
            else:
                return False

        def getRandom(self) -> int:
            return random.choice(self.list)
    # Your RandomizedSet object will be instantiated and called as such:
    # obj = RandomizedSet()
    # param_1 = obj.insert(val)
    # param_2 = obj.remove(val)
    # param_3 = obj.getRandom()
