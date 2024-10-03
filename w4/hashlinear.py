class HashLinear:
    def __init__(self, size: int):
        self.size = size
        self.T = [None] * size
    
    def hash(self, data: str):
        return sum(ord(i) for i in data) % self.size #source: https://www.w3schools.com/python/ref_func_ord.asp used this to find the ascii value of the character to hash with. Then instead of calculating sum with sum=0, I used the sum() function. For some reason sum() worked better and didn't have any errors.


    def print(self):
        for i in self.T:
            if i is None:
                print("F", end=" ")
            elif i == "T":
                print("T", end=" ")
            else:
                print(i, end=" ")
        print()

    def insert(self, data: str):
        i = self.hash(data)
        for j in range(self.size):
            k = (i + j) % self.size
            if self.T[k] is None or self.T[k] == 'T':
                self.T[k] = data
                return
            if self.T[k] == data:
                return

    def delete(self, data: str):
        for j in range(self.size):
            if self.T[j] == data:
                self.T[j] = 'T'
                return



if __name__ == "__main__":
    table = HashLinear(8)
    table.print()

    table.insert("apple")
    table.insert("orange")
    table.insert("banana")
    table.insert("grapes")
    table.insert("mango")
    table.insert("peach")
    table.insert("apple")
    table.print()

    table.delete("banana")
    table.delete("kiwi")
    table.delete("peach")
    table.print()