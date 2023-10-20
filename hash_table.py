class Hash_table:
    def __init__(self, s):
        self.size = s
        self.T = [None] * s

    def __hash_level1(self, key):
        return key % self.size

    def __hash_level2(self, key):
        return key % (self.size // 10)

    def insert(self, key, value):
        pos_level1 = self.__hash_level1(key)
        if self.T[pos_level1] is None:
            self.T[pos_level1] = [None] * (self.size // 10)
        pos_level2 = self.__hash_level2(key)
        if self.T[pos_level1][pos_level2] is None:
            self.T[pos_level1][pos_level2] = []
        self.T[pos_level1][pos_level2].append((key, value))

    def get(self, key):
        pos_level1 = self.__hash_level1(key)
        if self.T[pos_level1] is not None:
            pos_level2 = self.__hash_level2(key)
            if self.T[pos_level1][pos_level2] is not None:
                for k, value in self.T[pos_level1][pos_level2]:
                    if k == key:
                        return value
        return None

    def print(self):
        print("{")
        for i in range(self.size):
            print("[", end="")
            for j in range(self.size // 10):
                if self.T[i] is not None and self.T[i][j] is not None:
                    items = self.T[i][j]
                    _str = ""
                    for k, value in items:
                        _str += value.to_string() + " "
                    print("[" + _str + "]", end="")
                else:
                    print("[]", end="")
            print("]")
        print("}")