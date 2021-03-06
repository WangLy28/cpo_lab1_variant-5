import typing


class set_hash(object):
    def __init__(self,
                 lst: typing.List[typing.Any] = [],
                 factor: int = 1) -> None:
        '''initial function'''
        if len(lst) == 0:
            self.table: list[typing.Optional[int]] = []
            self.set: list[typing.Optional[int]] = []
            self.factor = factor
        else:
            realset = []
            for value in lst:
                if value in realset:
                    continue
                realset.append(value)
            j = len(realset)
            self.table = [None] * j
            self.set = [None] * j
            self.factor = factor
            for value in realset:
                if value < 0:
                    index = (-value) % j
                else:
                    index = value % j
                i = j
                while i != 0:
                    if self.table[index % j] is None:
                        self.table[index % j] = value
                        break
                    else:
                        index += 1
                        i -= 1
            i = 0
            for value in self.table:
                if value is not None:
                    self.set[i] = value
                    i += 1

    def __eq__(self, other) -> bool:
        if self.set == other.set:
            return True
        else:
            return False

    def capacity(self) -> int:
        '''size of hashtable'''
        number = 0
        for value in self.table:
            number += 1
        return number

    def length(self) -> int:
        '''number of values'''
        number = 0
        for value in self.set:
            number += 1
        return number

    def add(self, value: typing.Optional[int]) -> 'set_hash':
        '''add value to the set. If this value exists, it is not added.
            If the length of the collection
            is equal to the collection capacity,
            the collection is expanded to twice the current capacity.'''
        if value is None:
            return self
        if value in self.set:
            return self
        else:
            j = len(self.table)
            if self.capacity() == 0:
                self.table += [None] * 1 * self.factor
            if self.length() == self.capacity():
                self.table += [None] * j * self.factor
            j = len(self.table)
            if value < 0:
                index = (-value) % j
            else:
                index = value % j
            i = j
            while i != 0:
                # if self.table[index % j] is None:
                if self.table[index % j] is None:
                    self.table[index % j] = value
                    break
                else:
                    index += 1
                    i -= 1
            self.set += [None]
            i = 0
            for value in self.table:
                if value is not None:
                    self.set[i] = value
                    i += 1
            return self

    def member(self, value: int) -> bool:
        '''detect whether the value is in the set'''
        if value in self.set:
            return True
        else:
            return False

    def reverse(self) -> typing.List[typing.Any]:
        '''reverse the set'''
        j = len(self.set)
        index = j - 1
        i = 0
        new_set: typing.List[typing.Any]
        new_set = []
        while i < j:
            value = self.set[index]
            new_set.append(value)
            index -= 1
            i += 1
        self.set = new_set
        return self.set

    def to_list(self) -> typing.List[typing.Any]:
        '''represent table that removes the None value as a list'''
        result: typing.List[typing.Any]
        result = []
        for value in self.table:
            if value is not None:
                result.append(value)
        return result

    def remove(self, value: typing.Optional[int]) -> 'set_hash':
        '''delete the value, replacing it with None'''
        if value not in self.table:
            return self
        temp = self.table.index(value)
        if value in self.table:
            self.table[temp] = None
            del self.set[temp]
        return self

    def find_value(self, value: int) -> bool:
        '''find index of value from set'''
        if value in self.table:
            return True
        else:
            return False

    def from_list(self,
                  lst:
                  typing.List[typing.Any]) -> 'set_hash':
        '''build set from list'''
        if len(lst) == 0:
            temp: 'set_hash'
            temp = set_hash([])
            return temp
        for e in reversed(lst):
            self.add(e)
        return self

    def map(self,
            function: typing.Callable[[typing.Optional[int]],
                                      typing.Any]) -> typing.List[typing.Any]:
        '''map value, the rule is defined by function'''
        cur: int
        cur = 0
        while cur < len(self.table):
            if self.table[cur] is not None:
                self.table[cur] = function(self.table[cur])
            cur += 1
        i = 0
        for value in self.table:
            if value is not None:
                self.set[i] = value
                i += 1
        return self.set

    def empty(self) -> typing.List[typing.Any]:
        '''clear set'''
        self.table = []
        self.set = []
        return self.set

    def mconcat(self,
                sethash: 'set_hash') -> typing.List[typing.Any]:
        '''mconcat of two sets'''
        if sethash.length == 0:
            return self.set
        else:
            cap = len(sethash.table)
            cur = 0
            while cur < cap:
                temp = sethash.table[cur]
                if temp is not None:
                    if temp in self.table:
                        cur += 1
                    else:
                        self.add(temp)
                        cur += 1
                else:
                    cur += 1
        return self.set

    def filter(self,
               function: typing.Callable[[typing.Optional[int]],
                                         bool]) -> typing.List[typing.Any]:
        '''filter set'''
        new_table: typing.List[typing.Any]
        new_table = []
        for value in self.table:
            if function(value) is True:
                if value not in new_table:
                    new_table.append(value)
        return new_table
