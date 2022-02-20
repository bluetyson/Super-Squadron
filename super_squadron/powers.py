
import pandas as pd
import numpy as np

class PowerBase:
	def __init__(self, power, apcost, maxap, areaeffect, deviceap, damageap, duration, durationunit, range, devicerange, choices, device=False):
		self.name = power
		self.apcost = apcost
		self.maxap = maxap
		self.areaeffect = areaeffect
		self.deviceap = deviceap
		self.damageap = damageap
		self.duration = duration
		self.durationunit = durationunit
		self.range = range
		self.devicerange = devicerange
		self.choices = choices

	def __repr__(self):
		rep = 'PowerBase(' + self.name + ',' + str(self.apcost) + ')'
		return rep
		#if a device calculate that info

def printtest():
	print("Super Squadron")

df = pd.read_csv('data/power_details.csv')
#print(df.head())
powers_dict = {}

for index, row in df.iterrows():
	powers_dict[row['Power']] = PowerBase(row['Power'], row['APCost'], row['MaxAP'], row['AreaEffect'], row['DeviceAP'],\
	 row['DamageAP'], row['Duration'], row['DurationUnit'], row['Range'], row['DeviceRange'], row['Choices'])

class Adaption(PowerBase):
	def __init__(self):
		super().__init__(powers_dict['Adaption'].name, powers_dict['Adaption'].apcost, powers_dict['Adaption'].maxap,\
						 powers_dict['Adaption'].areaeffect, powers_dict['Adaption'].deviceap, powers_dict['Adaption'].damageap,\
						 powers_dict['Adaption'].duration, powers_dict['Adaption'].durationunit, powers_dict['Adaption'].range,\
						 powers_dict['Adaption'].devicerange, powers_dict['Adaption'].choices)
		self.strdetails = '1AP for light adaption, 5AP for heavy'


