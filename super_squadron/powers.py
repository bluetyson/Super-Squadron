
import pandas as pd
import numpy as np
import math

from super_squadron.roll import roll_ap, roll_effects

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

df = pd.read_csv('data/power_details.csv', low_memory=False)
print(df.head())
powers_dict = {}

for index, row in df.iterrows():
	powers_dict[row['Power']] = PowerBase(row['Power'], row['APCost'], row['MaxAP'], row['AreaEffect'], row['DeviceAP'],\
	 row['DamageAP'], row['Duration'], row['DurationUnit'], row['Range'], row['DeviceRange'], row['Choices'])

print(powers_dict)

class Adaption(PowerBase):
	def __init__(self, Character):
		powername = 'Adaption'
		super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
						 powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
						 powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
						 powers_dict[powername].devicerange, powers_dict[powername].choices)
		self.strdetails = '1AP for light adaption, 5AP for heavy'
		print(self.range)
		Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
		Character['Powers']['Detail'][powername]['APCost'] = self.apcost
		Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
		Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
		Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
		Character['Powers']['Detail'][powername]['Duration'] = self.duration
		Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
		Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
		Character['Powers']['Detail'][powername]['Choices'] = self.choices
		if 'Device' in Character['Powers']['Detail'][powername]:
			print(Character['Powers']['Detail'][powername]['Device'])
			Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
			Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)


class AirGeneration(PowerBase):
	def __init__(self, Character):
		powername = 'Air Generation'
		super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
						 powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
						 powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
						 powers_dict[powername].devicerange, powers_dict[powername].choices)
		self.strdetails = 'Create high intensity wind blasts, sand or dust storms, or oxgen from water or carbon dioxide.'
		Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
		Character['Powers']['Detail'][powername]['APCost'] = self.apcost
		Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
		Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
		Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
		Character['Powers']['Detail'][powername]['Duration'] = self.duration
		Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
		Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
		Character['Powers']['Detail'][powername]['Choices'] = self.choices
		Character['Powers']['Detail'][powername]['Blast'] = {}
		Character['Powers']['Detail'][powername]['Damage'] = {}
		Character['Powers']['Detail'][powername]['Storm'] = {}
		Character['Powers']['Detail'][powername]['Oxygen'] = {}
		Character['Powers']['Detail'][powername]['Blast']['APCost'] = self.apcost
		Character['Powers']['Detail'][powername]['Blast']['MaxAP'] = self.maxap
		Character['Powers']['Detail'][powername]['Damage']['AP'] = self.damageap
		Character['Powers']['Detail'][powername]['Blast']['Range'] = (Character['Statistics']['Stamina']+Character['Statistics']['Agility'])*2
		Character['Powers']['Detail'][powername]['Storm']['AreaEffect'] = normal_round(Character['Statistics']['Stamina']/5)
		Character['Powers']['Detail'][powername]['Storm']['Penalty'] = 20
		Character['Powers']['Detail'][powername]['Oxygen']['APCost'] = "1"
		Character['Powers']['Detail'][powername]['Oxygen']['Volume'] = "1"
		if 'Device' in Character['Powers']['Detail'][powername]:
			print(Character['Powers']['Detail'][powername]['Device'])
			Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
			Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class AnimalAffinity(PowerBase):
	def __init__(self, Character):
		powername = 'Animal Affinity'
		super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
						 powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
						 powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
						 powers_dict[powername].devicerange, powers_dict[powername].choices)
		self.strdetails = 'Character is able to control specific animal(s) chosen'
		Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
		Character['Powers']['Detail'][powername]['APCost'] = self.apcost
		Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
		Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
		Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
		Character['Powers']['Detail'][powername]['Duration'] = self.duration
		Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
		Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
		Character['Powers']['Detail'][powername]['Choices'] = self.choices
		Character['Powers']['Detail'][powername]['Loyalty'] = 30
		Character['Powers']['Detail'][powername]['Morale'] = -10
		Character['Powers']['Detail'][powername]['ArrivalTime'] = "1d6"
		Character['Powers']['Detail'][powername]['Statistics'] = "2d6 [ST, AG, IQ, SA]"
		Character['Powers']['Detail'][powername]['Damage'] = "1/1/1d3"
		if 'Device' in Character['Powers']['Detail'][powername]:
			print(Character['Powers']['Detail'][powername]['Device'])
			Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
			Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class Armour(PowerBase):
	def __init__(self, Character):
		powername = 'Armour'
		super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
						 powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
						 powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
						 powers_dict[powername].devicerange, powers_dict[powername].choices)
		self.strdetails = 'Armour reduces damage'
		Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
		Character['Powers']['Detail'][powername]['APCost'] = self.apcost
		Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
		Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
		Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
		Character['Powers']['Detail'][powername]['Duration'] = self.duration
		Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
		Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
		Character['Powers']['Detail'][powername]['Choices'] = self.choices
		Character['Powers']['Detail'][powername]['DamageReduction'] = {}
		Character['Powers']['Detail'][powername]['DamageReduction']['HTH'] = 1/3
		Character['Powers']['Detail'][powername]['DamageReduction']['Other'] = 1/2
		if 'Device' in Character['Powers']['Detail'][powername]:
			print(Character['Powers']['Detail'][powername]['Device'])
			Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
			Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

			devcheck = roll_effects(1, 100)
			if devcheck <= 15:
				Character['Powers']['Detail'][powername]['Device']['ExtraAbilities'] = roll_effects(1,4) +1
				Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails + " device has abilities"



