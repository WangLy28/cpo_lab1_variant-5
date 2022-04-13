class hash_map(object):
	def __init__(self,list=[],factor = 1):
		self.table = [None,None,None,None]
		self.factor = factor
		i = len(self.table)
		j = len(list)
		while j >= i :
			self.table = self.table + [None,None,None,None]*self.factor
			i = i + 4*self.factor
		for l in list:
			index = l % 4
			if self.table[index]==None :
				self.table[index] = l
			else :
				i = 0
				while i != 10:
					index = index + 4
					if index > len(self.table):
						self.table = self.table + [None,None,None,None]
						self.table[index] = l
						break
					else:
						if self.table[index]==None :
							self.table[index] = l
							break
						else :
							i +=1
							continue

	def capacity(self):
		return len(self.table)
	
	def length(self):
		i = 0
		for v in self.table:
			if v != None:
				i+=1
		return i

	def add_value(self,value):
		i = self.capacity()
		j = self.length() + 1
		while j >= i :
				self.table = self.table + [None,None,None,None]*self.factor
				i = i + 4*self.factor
		index = value % 4
		if self.table[index]==None :
			self.table[index] = value
		else :
			i = 0
			while i != 10:
				index = index + 4
				if index > len(self.table):
					self.table = self.table + [None,None,None,None]
					self.table[index] = value
					break
				else:
					if self.table[index]==None :
						self.table[index] = value
						break
					else :
						i +=1
						continue
		return self

	def reduce_value(self,value):
		index = value % 4
		while value in self.table :
			self.table[self.table.index(value)] = None
		return self

	def find_value(self,value):
		if value in self.table :
			return self.table.index(value)
		else :
			print('notfound')
# t1 = hash_map([0,1,2,3,4,5,9,9]).add_value(13).reduce_value(9).find_value(9)
# for v in t1.table:
# 	print(v)
# print(hash_map().capacity())
# t2 = reduce_value(t1,0)
# for v in t2.table:
# 	print(v)

# t2 = add_value(t1,0)
# for v in t2.table:
# 	print(v)
# print(capacity(t1))