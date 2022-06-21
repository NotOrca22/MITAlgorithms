class StaticArray:  # interface
    def __init__(self, length):  # O(n)
        self.array = [None] * length  # O(n)

    def get_at(self, index):  # O(1), function of interface
        if 0 <= index < len(self.array):
            return self.array[index]  # O(1)

    def set_at(self, index, value):
        if 0 <= index < len(self.array):
            self.array[index] = value

    def insert_at(self, index, value):
        if 0 <= index <= len(self.array):  # if index = len(self.array) then value is appended to the end
            self.array.append(None)
            print(len(self.array))
            for i in range(len(self.array) - 2, index - 1, -1):
                self.array[i + 1] = self.array[i]
            self.array[index] = value


if __name__ == "__main__":
    print(20+25+10+25+8+14+60+30+16+7+20+7.5+20+12+60)
    # sa = StaticArray(100)
    # print(sa.array)
    # sa.set_at(98, 42)
    # print(sa.array)
    # print(sa.get_at(99))
    # for i in range(1000000):
    #     sa.insert_at(100+i, 420)
    # print(sa.array)
