import geopy.distance
import pandas as pd


class FlightDistance:
	
	def read_cvs(self):
		df = pd.read_csv("Flight Distance Test.csv")
		return df

	def dep_coordinates_together(self):
		df = self.read_cvs()
		dep_coordin_together = list(zip(df['Departure_lat'], df['Departure_lon']))
		return dep_coordin_together
	
	def arriv_coordinates_together(self):
		df = self.read_cvs()
		arriv_coordin_together = list(zip(df['Arrival_lat'], df['Arrival_lon']))
		return arriv_coordin_together
	
	def calculate_distance(self):
		distances = []
		for i, j in zip(self.dep_coordinates_together(), self.arriv_coordinates_together()):
			distances.append(round(geopy.distance.distance(i, j).miles))
		print(distances)
		return distances
	
	def add_distance_to_csv(self):
		df = pd.read_csv("Flight Distance Test.csv")
		df["Distance"] = self.calculate_distance()
		unique_distance = df[['Normalised City Pair', 'Distance']].drop_duplicates().value_counts(sort=False).reset_index(
			name='City pair unique distance')
		print(type(unique_distance))
		df = df.merge(unique_distance[['Normalised City Pair', 'City pair unique distance']], how='left',
		              on='Normalised City Pair')
		
		df.to_csv("flights.csv")


fd = FlightDistance()
fd.calculate_distance()
