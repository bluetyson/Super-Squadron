
import pandas as pd
import numpy as np
import math

def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

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
powers_dict = {}

for index, row in df.iterrows():
	powers_dict[row['Power']] = PowerBase(row['Power'], row['APCost'], row['MaxAP'], row['AreaEffect'], row['DeviceAP'],\
	 row['DamageAP'], row['Duration'], row['DurationUnit'], row['Range'], row['DeviceRange'], row['Choices'])

powername = 'Adaption'
class Adaption(PowerBase):
	def __init__(self, Character):
		super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
						 powers_dict[powername].areaeffect, powers_dict['Adaption'].deviceap, powers_dict[powername].damageap,\
						 powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
						 powers_dict[powername].devicerange, powers_dict[powername].choices)
		self.strdetails = '1AP for light adaption, 5AP for heavy'
		Character['Powers']['Detail']['Adaption']['StrDetails'] = self.strdetails

powername = 'Air Generation'
class AirGeneration(PowerBase):
	def __init__(self, Character):
		super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
						 powers_dict[powername].areaeffect, powers_dict['Adaption'].deviceap, powers_dict[powername].damageap,\
						 powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
						 powers_dict[powername].devicerange, powers_dict[powername].choices)
		self.strdetails = 'Create high intensity wind blasts, sand or dust storms, or oxgen from water or carbon dioxide.'
		Character['Powers']['Detail']['Air Generation']['StrDetails'] = self.strdetails
		Character['Powers']['Detail']['Air Generation']['Blast'] = {}
		Character['Powers']['Detail']['Air Generation']['Damage'] = {}
		Character['Powers']['Detail']['Air Generation']['Storm'] = {}
		Character['Powers']['Detail']['Air Generation']['Oxygen'] = {}
		Character['Powers']['Detail']['Air Generation']['Blast']['APCost'] = self.apcost
		Character['Powers']['Detail']['Air Generation']['Blast']['MaxAP'] = self.maxap
		Character['Powers']['Detail']['Air Generation']['Damage']['AP'] = self.damageap
		Character['Powers']['Detail']['Air Generation']['Blast']['Range'] = (Character['Statistics']['Stamina']+Character['Statistics']['Agility'])*2
		Character['Powers']['Detail']['Air Generation']['Storm']['AreaEffect'] = normal_round(Character['Statistics']['Stamina']/5)
		Character['Powers']['Detail']['Air Generation']['Storm']['Penalty'] = 20
		Character['Powers']['Detail']['Air Generation']['Oxygen']['APCost'] = "1"
		Character['Powers']['Detail']['Air Generation']['Oxygen']['Volume'] = "1"