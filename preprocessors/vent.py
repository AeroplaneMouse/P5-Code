import pandas as pa

class VentPreprocessor:
	DataFrame = None


	def CreateDataFrame(self, csvPath, seperator):
		# Load data from
		self.DataFrame = pa.read_csv(csvPath, sep=seperator)

		# Set timestamps as index
		self.DataFrame.index = pa.to_datetime(self.DataFrame.pop('Timestamp'))

		# Remove shitty columns
		self.DataFrame.pop('DayOfWeek')
		self.DataFrame.pop('TimeStamp_Count')
		self.DataFrame.pop('Vent_HRVstaleairpressuredifferential')
		self.DataFrame.pop('Vent_HRVfreshairpressuredifferential')

		# Remove timezone
		self.DataFrame = self.DataFrame.tz_convert(None)

