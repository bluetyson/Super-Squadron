
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
		Character['Powers']['Detail'][powername]['Range'] = self.range
		Character['Powers']['Detail'][powername]['Choices'] = self.choices
		Character['Powers']['Detail'][powername]['1AP'] = "15-55C, reduced O2"
		Character['Powers']['Detail'][powername]['2AP'] = "5-65C, thin atmosphere"
		Character['Powers']['Detail'][powername]['3AP'] = "-5-75C, adverse atmosphere, gravity"
		Character['Powers']['Detail'][powername]['4AP'] = "-15-85C, gravity variation 75%"
		Character['Powers']['Detail'][powername]['5AP'] = "-25-95C, reduced O2, gravity variation 100%"
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
		Character['Powers']['Detail'][powername]['Range'] = (Character['Statistics']['Intelligence'])*3
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
		Character['Powers']['Detail'][powername]['Range'] = self.range
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

class AstralProjection(PowerBase):
	def __init__(self, Character):
		powername = 'Astral Projection'
		super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
						 powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
						 powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
						 powers_dict[powername].devicerange, powers_dict[powername].choices)
		self.strdetails = 'Separate spirit form from body'
		Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
		Character['Powers']['Detail'][powername]['APCost'] = self.apcost
		Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
		Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
		Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
		Character['Powers']['Detail'][powername]['Duration'] = (Character['Statistics']['Stamina'])+10
		Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
		Character['Powers']['Detail'][powername]['Range'] = self.range
		Character['Powers']['Detail'][powername]['Choices'] = self.choices
		Character['Powers']['Detail'][powername]['Speed'] = (Character['Statistics']['Stamina']+Character['Statistics']['Agility'])
		Character['Powers']['Detail'][powername]['SpeedUnit'] = "km/turn"
		powcheck = roll_effects(1, 100)
		if powcheck <= 5:
			Character['Powers']['Detail'][powername]['PowersInAstral'] = "Yes"
		if Character['Origin']['Origin'] == 'Supernatural':
			spellscheck = roll_effects(1,100)
			if spellscheck <= 85:
				Character['Powers']['Detail'][powername]['SpellsInAstral'] = "Yes"
		if 'Device' in Character['Powers']['Detail'][powername]:
			print(Character['Powers']['Detail'][powername]['Device'])
			Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
			Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class BodyAugmentation(PowerBase):
	def __init__(self, Character):
		powername = 'Body Augmentation'
		super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
						 powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
						 powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
						 powers_dict[powername].devicerange, powers_dict[powername].choices)
		self.strdetails = 'Gain additional appendages, each modifying HP or DD'
		Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
		Character['Powers']['Detail'][powername]['APCost'] = self.apcost
		Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
		Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
		Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
		Character['Powers']['Detail'][powername]['Duration'] = self.duration
		Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
		Character['Powers']['Detail'][powername]['Range'] = self.range
		Character['Powers']['Detail'][powername]['Choices'] = self.choices
		bacheck = roll_effects(1, 3)
		Character['Powers']['Detail'][powername]['Augmentations'] = {}
		Character['Powers']['Detail'][powername]['Augmentations']['Augmentations'] = bacheck
		Character['Powers']['Detail'][powername]['Augmentations']['Type'] = {}
		Character['Powers']['Detail'][powername]['Augmentations']['Special'] = {}
		Character['Powers']['Detail'][powername]['Augmentations']['Powers'] = {}
		for power in range(bacheck):
			batypecheck = roll_effects(1,8)
			if batypecheck == 1:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Wings"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Flight"
			elif batypecheck == 2:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Claws"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "HP:2d8 DD:1d4"
			elif batypecheck == 3:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Tail"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "HP:1d10 DD:1d6"
			elif batypecheck == 4:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Gills"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Water Breathing"
			elif batypecheck == 5:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Fangs"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "DD:1d8"
			elif batypecheck == 6:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Spiked hands/arms"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "DD:1d8"
			elif batypecheck == 7:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Stinger"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Paralysis or Sleep Teason"
			else:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Extra Arms"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Double Normal Attacks"

			powcheck = roll_effects(1, 100)
			if powcheck <= 5:
				Character['Powers']['Detail'][powername]['Augmentations']['Powers'][str(power+1)] = "Yes"
			else:
				Character['Powers']['Detail'][powername]['Augmentations']['Powers'][str(power + 1)] = "No"
		if 'Device' in Character['Powers']['Detail'][powername]:
			print(Character['Powers']['Detail'][powername]['Device'])
			Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
			Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)


class Cybernetics(PowerBase):
	def __init__(self, Character):
		powername = 'Cybernetics'
		super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
						 powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
						 powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
						 powers_dict[powername].devicerange, powers_dict[powername].choices)
		self.strdetails = 'Mechanical replacement for either limbs or organs'
		Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
		Character['Powers']['Detail'][powername]['APCost'] = self.apcost
		Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
		Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
		Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
		Character['Powers']['Detail'][powername]['Duration'] = self.duration
		Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
		Character['Powers']['Detail'][powername]['Range'] = self.range
		Character['Powers']['Detail'][powername]['Choices'] = self.choices
		bacheck = roll_effects(1, 3)
		Character['Powers']['Detail'][powername]['Augmentations'] = {}
		Character['Powers']['Detail'][powername]['Augmentations']['Augmentations'] = bacheck
		Character['Powers']['Detail'][powername]['Augmentations']['Type'] = {}
		Character['Powers']['Detail'][powername]['Augmentations']['Special'] = {}
		Character['Powers']['Detail'][powername]['Augmentations']['Powers'] = {}
		for power in range(bacheck):
			batypecheck = roll_effects(1,8)
			if batypecheck == 1:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Hand"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Stamina:1d8"
			elif batypecheck == 2:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Arm"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Strength:1d8 DD:1d4"
			elif batypecheck == 3:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Leg"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Agility:1d10"
			elif batypecheck == 4:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Eye"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Vision Power:x-ray, telescopic, infra"
			elif batypecheck == 5:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Ear"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Super hearing"
			elif batypecheck == 6:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Brain"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Intelligence:2d6"
			elif batypecheck == 7:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Lungs"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Stamina:1d8"
			else:
				Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Bones"
				Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Stamina:1d6 Strength:1d8"

			powcheck = roll_effects(1, 100)
			if powcheck <= 5:
				Character['Powers']['Detail'][powername]['Augmentations']['Powers'][str(power+1)] = "Yes"
			else:
				Character['Powers']['Detail'][powername]['Augmentations']['Powers'][str(power + 1)] = "No"
		if 'Device' in Character['Powers']['Detail'][powername]:
			print(Character['Powers']['Detail'][powername]['Device'])
			Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
			Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class DarknessGeneration(PowerBase):
	def __init__(self, Character):
		powername = 'Darkness Generation'
		super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
						 powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
						 powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
						 powers_dict[powername].devicerange, powers_dict[powername].choices)
		self.strdetails = 'Dispel light'
		Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
		Character['Powers']['Detail'][powername]['APCost'] = self.apcost
		Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
		Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
		Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
		Character['Powers']['Detail'][powername]['Duration'] = self.duration
		Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
		Character['Powers']['Detail'][powername]['Range'] = (Character['Statistics']['Intelligence'])*1
		Character['Powers']['Detail'][powername]['Choices'] = self.choices
		Character['Powers']['Detail'][powername]['AttackDM'] = 30
		Character['Powers']['Detail'][powername]['MishapChance'] = "80 - (LK+EXP)"
		Character['Powers']['Detail'][powername]['MishapDamage'] = "1d2"
		if 'Device' in Character['Powers']['Detail'][powername]:
			print(Character['Powers']['Detail'][powername]['Device'])
			Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
			Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class DeathTouch(PowerBase):
	def __init__(self, Character):
		powername = 'Death Touch'
		super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
						 powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
						 powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
						 powers_dict[powername].devicerange, powers_dict[powername].choices)
		self.strdetails = 'Kill or Incapacitate with a touch'
		Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
		Character['Powers']['Detail'][powername]['APCost'] = 20
		Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
		Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
		Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
		Character['Powers']['Detail'][powername]['Duration'] = self.duration
		Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
		Character['Powers']['Detail'][powername]['Range'] = (Character['Statistics']['Intelligence'])*1
		Character['Powers']['Detail'][powername]['Choices'] = self.choices
		Character['Powers']['Detail'][powername]['APCostB'] = 10
		Character['Powers']['Detail'][powername]['Save'] = "ST + SA + LK + Exp"
		Character['Powers']['Detail'][powername]['SaveA'] = "0 HT"
		Character['Powers']['Detail'][powername]['FailA'] = "Death"
		Character['Powers']['Detail'][powername]['SaveAPermanentDamage'] = "76-00 - LK"
		Character['Powers']['Detail'][powername]['SaveB'] = "0 HT"
		Character['Powers']['Detail'][powername]['FailB'] = "0 HT"
		Character['Powers']['Detail'][powername]['DefensivePowerModifierA'] = "HT / Defensive Multiplier * 4"
		Character['Powers']['Detail'][powername]['DefensivePowerModifierSaveA'] = "Half Damage"
		Character['Powers']['Detail'][powername]['DefensivePowerModifierB'] = "HT / Defensive Multiplier * 2"
		Character['Powers']['Detail'][powername]['DefensivePowerModifierSaveB'] = "Half Damage"
		Character['Powers']['Detail'][powername]['DefensivePowerModifierPermanentDamage'] = "91-00 - LK"
		if 'Device' in Character['Powers']['Detail'][powername]:
			print(Character['Powers']['Detail'][powername]['Device'])
			Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
			Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class Defect(PowerBase):
	def __init__(self, Character):
		powername = 'Defect'
		super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
						 powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
						 powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
						 powers_dict[powername].devicerange, powers_dict[powername].choices)
		self.strdetails = 'Defective Attribute which may give additional powers'
		Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
		Character['Powers']['Detail'][powername]['APCost'] = self.apcost
		Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
		Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
		Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
		Character['Powers']['Detail'][powername]['Duration'] = self.duration
		Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
		Character['Powers']['Detail'][powername]['Range'] = self.range
		Character['Powers']['Detail'][powername]['Choices'] = self.choices
		if 'Device' in Character['Powers']['Detail'][powername]:
			print(Character['Powers']['Detail'][powername]['Device'])
			Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
			Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)
