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


def capacity(t):
	return len(t.table)
def length(t):
	i = 0
	for v in t.table:
		if v != None:
			i+=1
	return i

def add_value(t,value):
	i = capacity(t)
	j = length(t) + 1
	while j >= i :
			t.table = t.table + [None,None,None,None]*t.factor
			i = i + 4*t.factor
	index = value % 4
	new_t = t
	if new_t.table[index]==None :
		new_t.table[index] = value
	else :
		i = 0
		while i != 10:
			index = index + 4
			if index > len(new_t.table):
				new_t.table = new_t.table + [None,None,None,None]
				new_t.table[index] = value
				break
			else:
				if new_t.table[index]==None :
					new_t.table[index] = value
					break
				else :
					i +=1
					continue
	return new_t
def reduce_value(t,value):
	index = value % 4
	new_t = t
	while value in new_t.table :
		new_t.table[new_t.table.index(value)] = None
	return new_t
def find_value(t,value):
	if length(t) > 0:
		if value in t.table :
			return t.table.index(value)
		else :
			print('notfound')
	else:
		return None
# t1 = hash_map([0,1,2,5,9,13])
# for v in t1.table:
# 	print(v)
# print(find_value(hash_map([0,1,3,4]),1))
# t2 = reduce_value(t1,0)
# for v in t2.table:
# 	print(v)

# t2 = add_value(t1,0)
# for v in t2.table:
# 	print(v)
# print(capacity(t1))