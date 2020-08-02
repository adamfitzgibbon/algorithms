"""An implementation of resizable array list. Yes I know python lists are resizable, that's not the point!"""

class ArrayList:
    pointer = 0

    def __init__(self, size):
        self._array = [None for i in range(size)]
    
    def get(self, index):
        return self._array[index]

    def add(self, item):
        if self.pointer >= len(self._array):
            self._array += [None for i in range(len(self._array))]
        for i, element in enumerate(self._array):
           if element is None:
                self._array[i] = item
                self.pointer += 1
                return        

    def toString(self):
        filteredArray = map(lambda x: "None" if x is None else x, self._array)
        return f"[ {', '.join(filteredArray)} ]"

arrayList = ArrayList(10)

for i in range(15):
    arrayList.add(str(i))

print(arrayList.get(12))