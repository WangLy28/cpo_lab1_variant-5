class hashMap(object):
    def __init__(self, list=[], factor=1):
        self.table = [None, None, None, None]
        self.factor = factor
        i = len(self.table)
        j = len(list)
        while j >= i:
            self.table = self.table + [None, None, None, None] * self.factor
            i = i + 4 * self.factor
        for k in list:
            index = k % 4
            if self.table[index] is None:
                self.table[index] = k
            else:
                i = 0
                while i != 10:
                    index = index + 4
                    if index > len(self.table):
                        self.table = self.table + [None, None, None, None]
                        self.table[index] = k
                        break
                    else:
                        if self.table[index] is None:
                            self.table[index] = k
                            break
                        else:
                            i += 1
                            continue

    def __str__(self):
        return " : ".join(map(str, self.to_list()))

    def capacity(self):
        return len(self.table)

    def length(self):
        i = 0
        for v in self.table:
            if v is not None:
                i += 1
        return i

    def add_value(self, value):
        if value in self.table:
            print('already in hash_map')
            return self
        else:
            i = self.capacity()
            j = self.length() + 1
            while j >= i:
                self.table = self.table + [None, None, None, None] * self.factor
                i = i + 4 * self.factor
            index = value % 4
            if self.table[index] is None:
                self.table[index] = value
            else:
                i = 0
                while i != 10:
                    index = index + 4
                    if index > len(self.table):
                        self.table = self.table + [None, None, None, None]
                        self.table[index] = value
                        break
                    else:
                        if self.table[index] is None:
                            self.table[index] = value
                            break
                        else:
                            i += 1
                            continue
            return self

    def reduce_value(self, value):
        index = value % 4
        while value in self.table:
            self.table[self.table.index(value)] = None
        return self

    def find_value(self, value):
        if value in self.table:
            return self.table.index(value)
        else:
            print('notfound')

    def to_list(self):
        res = []
        for v in self.table:
            if v is not None:
                res.append(v)
        return res

    def from_list(self, lst):
        if len(lst) == 0:
            return
        for e in reversed(lst):
            self.add_value(e)
        return self

    def map(self, f):
        cur = 0
        while cur < len(self.table):
            if self.table[cur] is not None:
                self.table[cur] = f(self.table[cur])
            cur += 1
        return self.table

    def mempty(self):
        self.table = [None, None, None, None]
        return self.table

    def mconcat(self, hashMap):
        if hashMap.length == 0:
            return self.table
        else:
            cap = len(hashMap.table)
            cur = 0
            while cur < cap:
                if hashMap.table[cur] is not None:
                    if hashMap.table[cur] in self.table:
                        cur += 1
                    else:
                        self.add_value(hashMap.table[cur])
                        cur += 1
                else:
                    cur += 1
            return self.table
