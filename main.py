

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:

	def __init__(self, list_):
		self.list_ = list_

	def __iter__(self):
		self.cursor = 0
		self.cursor_i = -1
		return self

	def __next__(self):
		while self.cursor < len(self.list_):
			self.cursor_i += 1
			while self.cursor_i < len(self.list_[self.cursor]):
				return self.list_[self.cursor][self.cursor_i]
			self.cursor_i = -1
			self.cursor += 1
		raise StopIteration


for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


def flat_generator(list_):
	cursor_g = 0
	cursor_gi = 0
	while cursor_g < len(list_):
		while cursor_gi < len(list_[cursor_g]):
			yield list_[cursor_g][cursor_gi]
			cursor_gi += 1
		cursor_gi = 0
		cursor_g += 1

for item in  flat_generator(nested_list):
	print(item)
