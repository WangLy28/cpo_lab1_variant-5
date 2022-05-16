import typing


class hashmap(object):
    def __init__(self, lst: typing.List[typing.Any] = [],
                 factor: int = 1) -> None:
        '''initial function'''
        if len(lst) == 0:
            self.table: typing.List[typing.Any]
            self.table = []
            self.factor = factor
        else:
            realset = []
            for value in lst:
                if value in realset:
                    continue
                realset.append(value)
            j = len(realset)
            self.table = [None] * j
            self.factor = factor
            for value in realset:
                index = value % j
                i = j
                while i != 0:
                    if self.table[index % j] is None:
                        self.table[index] = value
                        break
                    else:
                        index += 1
                        i -= 1

    def capacity(self) -> int:
        '''size of list'''
        number = 0
        for value in self.table:
            number += 1
        return number

    def length(self) -> int:
        '''number of values'''
        number = 0
        for value in self.table:
            if value is not None:
                number += 1
        return number

    def add(self, value: int) -> typing.List[typing.Any]:
        '''add value to the set. If this value exists, it is not added.
            If the length of the collection
            is equal to the collection capacity,
            the collection is expanded to twice the current capacity.'''
        if value in self.table:
            return self.table
        else:
            j = len(self.table)
            if self.capacity() == 0:
                self.table += [None] * 1 * self.factor
            if self.length() == self.capacity():
                self.table += [None] * j * self.factor
            j = len(self.table)
            index = value % j
            i = j
            while i != 0:
                if self.table[index % j] is None:
                    self.table[index] = value
                    break
                else:
                    index += 1
                    i -= 1
            return self.table

    def member(self, value: int) -> bool:
        '''detect whether the value is in the set'''
        if value in self.table:
            return True
        else:
            return False

    def reverse(self) -> typing.List[typing.Any]:
        '''reverse the set'''
        j = len(self.table)
        index = j - 1
        i = 0
        # new_table = []
        new_table: typing.List[typing.Any]
        new_table = []
        while i < j:
            value = self.table[index]
            new_table.append(value)
            index -= 1
            i += 1
        self.table = new_table
        return self.table

    def to_list(self) -> typing.List[typing.Any]:
        '''represent set that removes the None value as a list'''
        # result = []
        result: typing.List[typing.Any]
        result = []
        for value in self.table:
            if value is not None:
                result.append(value)
        return result

    def reduce(self, value: int) -> typing.List[typing.Any]:
        '''delete the value, replacing it with None'''
        while value in self.table:
            self.table[self.table.index(value)] = None
        return self.table

    def find_value(self, value: int) -> str:
        '''find index of value from set'''
        if value in self.table:
            return str(self.table.index(value))
        else:
            return 'None'

    def from_list(self,
                  lst: typing.List
                  [typing.Any]) -> typing.List[typing.Any]:
        '''build set from list'''
        if len(lst) == 0:
            return
        for e in reversed(lst):
            self.add(e)
        return self.table

    def map(self,
            function:
            typing.Callable[[int],
                            typing.Any]) -> typing.List[typing.Any]:
        '''map value, the rule is defined by function'''
        cur = 0
        while cur < len(self.table):
            if self.table[cur] is not None:
                self.table[cur] = function(self.table[cur])
            cur += 1
        return self.table

    def empty(self) -> typing.List[typing.Any]:
        '''clear set'''
        self.table = []
        return self.table

    def mconcat(self, hashmap: 'hashmap') -> typing.List[typing.Any]:
        '''mconcat of two sets'''
        if hashmap.length == 0:
            return self.table
        else:
            cap = len(hashmap.table)
            cur = 0
            while cur < cap:
                if hashmap.table[cur] is not None:
                    if hashmap.table[cur] in self.table:
                        cur += 1
                    else:
                        self.add(hashmap.table[cur])
                        cur += 1
                else:
                    cur += 1
            return self.table

    def filter(self,
               function:
               typing.Callable[[int],
                               bool]) -> typing.List[typing.Any]:
        '''filter set'''
        # new_table = []
        new_table: typing.List[typing.Any]
        new_table = []
        for value in self.table:
            if function(value) is True:
                new_table.append(value)
        for value in new_table:
            self.reduce(value)
        return self.table
