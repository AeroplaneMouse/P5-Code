class IndexSet:
	def __init__(self, pattern, indexRecords):
		self.Pattern = pattern
		self.Records = indexRecords

	def __str__(self):
		output = '{:>5} {:>50} {:>5}'.format('pos', 'Time range', 'CS')
		
		for r in Records:
			output += str(r)

		return output
