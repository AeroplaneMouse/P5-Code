class IndexRecord:
	def __init__(self, pos, inVal, ref):
		self.Pos = pos
		self.Interval = inVal
		self.Ref = ref

	def __str__(self):
		return '{:>5} {:>50} {:>5}'.format(
			self.Pos,
			str(self.Interval),
			self.Ref
		)
		
	def __repr__(self):
		return self.__str__()