"""
Super Squadron Powers Module

This module contains the power system for the Super Squadron role-playing game.
It defines the PowerBase class and various power classes that inherit from it.

Powers are loaded from the data/power_details.csv file and stored in the powers_dict.
Each power class represents a specific superpower that can be assigned to characters.
"""

import pandas as pd
import numpy as np
import math
import os

from super_squadron.roll import roll_ap, roll_effects

def normal_round(n):
    """Round a number to the nearest integer using standard rounding rules."""
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

def safe_get(dictionary, *keys, default=0):
    """
    Safely get nested dictionary values with a default fallback.
    
    Args:
        dictionary (dict): The dictionary to access.
        *keys: Variable number of keys to traverse.
        default: Default value to return if key path doesn't exist.
    
    Returns:
        The value at the key path or the default value.
    """
    try:
        result = dictionary
        for key in keys:
            result = result[key]
        return result
    except (KeyError, TypeError):
        return default

class PowerBase:
    """
    Base class for all character powers in Super Squadron.
    
    Attributes:
        name (str): Name of the power.
        apcost: Action Point cost for using the power.
        maxap: Maximum Action Points that can be allocated.
        areaeffect: Area of effect for the power.
        deviceap: Device-specific AP value.
        damageap: Damage AP value.
        duration: How long the power lasts.
        durationunit (str): Unit of duration measurement.
        range: Range at which the power can be used.
        devicerange: Device-specific range.
        choices: Available choices/options for the power.
    """
    
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
        return f'PowerBase({self.name}, {self.apcost})'

def printtest():
    """Print a test message for Super Squadron."""
    print("Super Squadron")

# Get the directory where this file is located
current_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_dir, '..', 'data', 'power_details.csv')

# Load power details with error handling
try:
    df = pd.read_csv(data_file, low_memory=False)
except FileNotFoundError:
    # Try alternative path (when running from different directory)
    data_file = 'data/power_details.csv'
    try:
        df = pd.read_csv(data_file, low_memory=False)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find power_details.csv. Tried: {data_file}")

powers_dict = {}

for index, row in df.iterrows():
    powers_dict[row['Power']] = PowerBase(row['Power'], row['APCost'], row['MaxAP'], row['AreaEffect'], row['DeviceAP'],\
     row['DamageAP'], row['Duration'], row['DurationUnit'], row['Range'], row['DeviceRange'], row['Choices'])


class Adaption(PowerBase):
    def __init__(self, Character):
        powername = 'Adaption'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = '1AP for light adaption, 5AP for heavy'
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
                Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Paralysis or Sleep Toxin"
            else:
                Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Extra Arms"
                Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Double Normal Attacks"

            powcheck = roll_effects(1, 100)
            if powcheck <= 5:
                Character['Powers']['Detail'][powername]['Augmentations']['Powers'][str(power+1)] = "Yes"
            else:
                Character['Powers']['Detail'][powername]['Augmentations']['Powers'][str(power + 1)] = "No"
        if 'Device' in Character['Powers']['Detail'][powername]:
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
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class DensityControl(PowerBase):
    def __init__(self, Character):
        powername = 'Density Control'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Able to increase or decrease density'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = self.range
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['DensityLevel'] = {}
        Character['Powers']['Detail'][powername]['DensityLevel']['3'] = {}
        Character['Powers']['Detail'][powername]['DensityLevel']['2'] = {}
        Character['Powers']['Detail'][powername]['DensityLevel']['1'] = {}
        Character['Powers']['Detail'][powername]['DensityLevel']['0'] = {}
        Character['Powers']['Detail'][powername]['DensityLevel']['-1'] = {}
        Character['Powers']['Detail'][powername]['DensityLevel']['-2'] = {}
        Character['Powers']['Detail'][powername]['DensityLevel']['3']['Name'] = "Diamond"
        Character['Powers']['Detail'][powername]['DensityLevel']['3']['DD'] = "3d6"
        Character['Powers']['Detail'][powername]['DensityLevel']['3']['Move'] = "0.05"
        Character['Powers']['Detail'][powername]['DensityLevel']['2']['Name'] = "Steel"
        Character['Powers']['Detail'][powername]['DensityLevel']['2']['DD'] = "2d6"
        Character['Powers']['Detail'][powername]['DensityLevel']['2']['Move'] = "0.20"
        Character['Powers']['Detail'][powername]['DensityLevel']['1']['Name'] = "Rock"
        Character['Powers']['Detail'][powername]['DensityLevel']['1']['DD'] = "1d6"
        Character['Powers']['Detail'][powername]['DensityLevel']['1']['Move'] = "0.50"
        Character['Powers']['Detail'][powername]['DensityLevel']['0']['Name'] = "Normal"
        Character['Powers']['Detail'][powername]['DensityLevel']['0']['DD'] = "0"
        Character['Powers']['Detail'][powername]['DensityLevel']['0']['Move'] = "1"
        Character['Powers']['Detail'][powername]['DensityLevel']['-1']['Name'] = "Light"
        Character['Powers']['Detail'][powername]['DensityLevel']['-1']['DD'] = "-2d4"
        Character['Powers']['Detail'][powername]['DensityLevel']['-1']['Move'] = "2"
        Character['Powers']['Detail'][powername]['DensityLevel']['-2']['Name'] = "Flight"
        Character['Powers']['Detail'][powername]['DensityLevel']['-2']['DD'] = "-2d6"
        Character['Powers']['Detail'][powername]['DensityLevel']['-2']['Move'] = "10"

        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class DimensionalGate(PowerBase):
    def __init__(self, Character):
        powername = 'Dimensional Gate'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Create a gateway to another dimension or reality'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = self.range
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['TargetFamiliarity'] = {}
        Character['Powers']['Detail'][powername]['TargetFamiliarity']['Very Familiar'] = 3
        Character['Powers']['Detail'][powername]['TargetFamiliarity']['Studied'] = 26
        Character['Powers']['Detail'][powername]['TargetFamiliarity']['Casual'] = 50
        Character['Powers']['Detail'][powername]['TargetFamiliarity']['Unknown'] = 75
        Character['Powers']['Detail'][powername]['Duration'] = {}
        Character['Powers']['Detail'][powername]['Duration']['1'] = {"AP":0,"DM":2}
        Character['Powers']['Detail'][powername]['Duration']['2'] = {"AP":5,"DM":8}
        Character['Powers']['Detail'][powername]['Duration']['3'] = {"AP":10,"DM":24}
        Character['Powers']['Detail'][powername]['Duration']['4'] = {"AP":15,"DM":72}
        Character['Powers']['Detail'][powername]['Duration']['5'] = {"AP":20,"DM":95}

        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class DisintegrationBeam(PowerBase):
    def __init__(self, Character):
        powername = 'Disintegration Beam'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'High intensity destructive beam.'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = (Character['Statistics']['Strength']*15)
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class EgoChange(PowerBase):
    def __init__(self, Character):
        powername = 'Ego Change'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'The character may add or subtract 1d8 from Ego'
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
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class Elasticity(PowerBase):
    def __init__(self, Character):
        powername = 'Elasticity'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'The character can stretch as if pliable'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Stretching'] = {}
        Character['Powers']['Detail'][powername]['Stretching']['Limbs-Torso'] = (Character['Statistics']['Agility'])*(Character['Statistics']['Stamina'])
        Character['Powers']['Detail'][powername]['Stretching']['Other'] = (Character['Statistics']['Agility'])*3
        Character['Powers']['Detail'][powername]['Stretching']['Entangle'] = "(ST + AG + LK)"
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class EmotionControl(PowerBase):
    def __init__(self, Character):
        powername = 'Emotion Control'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Complete control over emotions on success'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = (Character['Statistics']['Intelligence']*2)
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Save'] = "(EG + LK + Exp)"
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class EnergyAbsorption(PowerBase):
    def __init__(self, Character):
        powername = 'Energy Absorption'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Energy Absorption A - character can absorb any energy directed at them'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Store'] = 70
        powcheck = roll_effects(1, 100)
        if powcheck <= 20:
            self.strdetails = self.strdetails + ' and B'
            powername2 = 'B'
            Character['Powers']['Detail'][powername2] = {}
            Character['Powers']['Detail'][powername2]['APCost'] = 4
            Character['Powers']['Detail'][powername2]['MaxAP'] = 4
            Character['Powers']['Detail'][powername2]['AreaEffect'] = "Character"
            Character['Powers']['Detail'][powername2]['DamageAP'] = "Variable"
            Character['Powers']['Detail'][powername2]['Duration'] = "2"
            Character['Powers']['Detail'][powername2]['DurationUnit'] = "hours"
            Character['Powers']['Detail'][powername2]['Range'] = (Character['Statistics']['Intelligence'])
            Character['Powers']['Detail'][powername2]['StoreMiss'] = 30
            Character['Powers']['Detail'][powername2]['StoreMax'] = (Character['Statistics']['Strength'] + Character['Statistics']['Stamina'])
            Character['Powers']['Detail'][powername2]['StoreBlast'] = "1d4 to 1d30, depending on energy"
            if 'Device' in Character['Powers']['Detail'][powername]:
                Character['Powers']['Detail'][powername2]['Device']['DeviceAP'] = roll_ap(self.deviceap)
                Character['Powers']['Detail'][powername2]['Device']['DeviceRange'] = roll_ap(self.devicerange)
                Character['Powers']['Detail'][powername2]['Device']['Overload'] = "50% energy in 15m radius"
                Character['Powers']['Detail'][powername2]['StoreMax'] = roll_ap("1d4x10")

        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class EnhancedAgility(PowerBase):
    def __init__(self, Character):
        powername = 'Enhanced Agility'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Add 2d10 to Agility'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Statistics']['Agility'] = Character['Statistics']['Agility'] + roll_effects(2,10)
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class EnhancedCharisma(PowerBase):
    def __init__(self, Character):
        powername = 'Enhanced Charisma'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Add 1d10 to Charisma'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Statistics']['Charisma'] = Character['Statistics']['Charisma'] + roll_effects(1,10)
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class EnhancedIntelligence(PowerBase):
    def __init__(self, Character):
        powername = 'Enhanced Intelligence'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Add 2d10 to Intelligence'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Statistics']['Intelligence'] = Character['Statistics']['Intelligence'] + roll_effects(2,10)
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class EnhancedStamina(PowerBase):
    def __init__(self, Character):
        powername = 'Enhanced Stamina'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Add 2d10 to Stamina'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Statistics']['Stamina'] = Character['Statistics']['Stamina'] + roll_effects(2,10)
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class EnhancedStrength(PowerBase):
    def __init__(self, Character):
        powername = 'Enhanced Strength'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Add 2d10 to Strength'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Statistics']['Strength'] = Character['Statistics']['Strength'] + roll_effects(2,10)
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class EnvironmentControl(PowerBase):
    def __init__(self, Character):
        powername = 'Environment Control'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Physically alter the surrounding conditions'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = (Character['Statistics']['Stamina']*Character['Statistics']['Stamina'])
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = (Character['Statistics']['Strength'] + Character['Statistics']['Stamina'])
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Gravity'] = "50%"
        Character['Powers']['Detail'][powername]['Temperature'] = "35 degrees"
        Character['Powers']['Detail'][powername]['Oxygen'] = "100%"
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class FastRecovery(PowerBase):
    def __init__(self, Character):
        powername = 'Fast Recovery'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Physically alter the surrounding conditions'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Rate'] = "1 HT per hour"
        Character['Powers']['Detail'][powername]['AttackEffects'] = "1/4 normal duration"
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class FlameGeneration(PowerBase):
    def __init__(self, Character):
        powername = 'Flame Generation'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Physically alter the surrounding conditions'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = (Character['Statistics']['Strength'] + Character['Statistics']['Agility'])*2
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Flight'] = (Character['Agility_Effects']['Move'])*4
        Character['Powers']['Detail'][powername]['Immunity'] = "High temperatures"
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class Flight(PowerBase):
    def __init__(self, Character):
        powername = 'Flight'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Fly personally'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Speed'] = (Character['Statistics']['Agility'] + Character['Statistics']['Stamina'] + Character['Statistics']['Stamina'])*3
        if Character['Powers']['Detail'][powername]['Speed'] > 150:
            addspeed = roll_effects(1,100)*10
            Character['Powers']['Detail'][powername]['Speed'] + addspeed
        if Character['Powers']['Detail'][powername]['Speed'] > 1000:
            Character['Powers']['Detail'][powername]['LightSpeed'] = "Yes"
        if Character['Powers']['Detail'][powername]['Speed'] > 2000:
            Character['Powers']['Detail'][powername]['Hyperspace'] = "Yes"
            Character['Powers']['Detail'][powername]['SpeedHyperspace'] = "1 Light Year per five minutes"
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)
            Character['Powers']['Detail'][powername]['Speed'] = roll_effects(2,10) * roll_effects(2,10)
            if Character['Powers']['Detail'][powername]['Speed'] > 150:
                addspeed = roll_effects(1,100)*10
                Character['Powers']['Detail'][powername]['Speed'] + addspeed
            if Character['Powers']['Detail'][powername]['Speed'] > 1000:
                Character['Powers']['Detail'][powername]['LightSpeed'] = "Yes"
            if Character['Powers']['Detail'][powername]['Speed'] > 2000:
                Character['Powers']['Detail'][powername]['Hyperspace'] = "Yes"
                Character['Powers']['Detail'][powername]['SpeedHyperspace'] = "1 Light Year per five minutes"

class ForceBeam(PowerBase):
    def __init__(self, Character):
        powername = 'Force Beam'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Force beam: '
        beamtype = roll_effects(1,4)
        if beamtype == 1:
            self.strdetails = self.strdetails + "Laser"
            self.apcost = 2
            self.maxap = 4
            self.areaeffect = "Character"
            self.damageap = "1d4"
            self.duration = "Instantaneous"
            self.durationunit = "NotApplicable"
            self.range = (Character['Statistics']['Agility'] + Character['Statistics']['Strength'])*10
            self.deviceap = "2d4x4"
            self.devicerange = "2d10x20"
            Character['Powers']['Detail'][powername]['Special'] = "Ignite Flammable"
        elif beamtype == 2:
            self.strdetails = self.strdetails + "Plasma"
            self.apcost = 2
            self.maxap = 6
            self.areaeffect = "Character"
            self.damageap = "1d8"
            self.duration = "Instantaneous"
            self.durationunit = "NotApplicable"
            self.range = (Character['Statistics']['Agility'] + Character['Statistics']['Strength'])*5
            self.deviceap = "1d6x4"
            self.devicerange = "2d10x10"
            Character['Powers']['Detail'][powername]['DamageNonLiving'] = 0.25
        elif beamtype == 3:
            self.strdetails = self.strdetails + "Magna"
            self.apcost = 2
            self.maxap = 6
            self.areaeffect = "Character"
            self.damageap = "1d6"
            self.duration = "Instantaneous"
            self.durationunit = "NotApplicable"
            self.range = (Character['Statistics']['Stamina'] + Character['Statistics']['Strength'])*8
            self.deviceap = "1d6x5"
            self.devicerange = "2d10x15"
        else:
            self.strdetails = self.strdetails + "Matter"
            self.apcost = 3
            self.maxap = 12
            self.areaeffect = "Character"
            self.damageap = "1d10"
            self.duration = "Instantaneous"
            self.durationunit = "NotApplicable"
            self.range = (Character['Statistics']['Agility'] + Character['Statistics']['Strength'])*15
            self.deviceap = "2d6x3"
            self.devicerange = "4d10x10"
            Character['Powers']['Detail'][powername]['DamageLiving'] = 0
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = (Character['Statistics']['Strength']*15)
        Character['Powers']['Detail'][powername]['Choices'] = self.choices

        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class ForceField(PowerBase):
    def __init__(self, Character):
        powername = 'Force Field'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Generate a force beam for attack or a field for defense'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = (Character['Statistics']['Strength'] + Character['Statistics']['Stamina'])
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Defense'] = "8 pts for every 2 AP"
        Character['Powers']['Detail'][powername]['ExtraArea'] = "Double AP per character"
        Character['Powers']['Detail'][powername]['Special'] = "Air, light and sound get through"
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class Gimmick(PowerBase):
    def __init__(self, Character):
        powername = 'Gimmick'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Use gimmicks as a power'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = self.range
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Number'] = roll_effects(1,4)+1
        Character['Powers']['Detail'][powername]['Gimmicks'] = {}
        # Load gimmicks with error handling
        try:
            gimmicks_file = os.path.join(current_dir, '..', 'data', 'Gimmicks.csv')
            gimmicks = pd.read_csv(gimmicks_file)
        except FileNotFoundError:
            try:
                gimmicks = pd.read_csv('data/Gimmicks.csv')
            except FileNotFoundError:
                raise FileNotFoundError("Could not find Gimmicks.csv")
        
        for gimmick in range(Character['Powers']['Detail'][powername]['Number']):
            new_gimmick = gimmicks['Gimmick'].sample()
            Character['Powers']['Detail'][powername]['Gimmicks'][str(gimmick+1)] = new_gimmick.values[0]
        Character['Powers']['Detail'][powername]['InventNew'] = (Character['Statistics']['Intelligence'])*2
        Character['Powers']['Detail'][powername]['ScientistInventNew'] = 30
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class GravityControl(PowerBase):
    def __init__(self, Character):
        powername = 'Gravity Control'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Increase or decrease gravity in an area'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = (Character['Statistics']['Stamina']*Character['Statistics']['Stamina'])
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = self.range
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Special'] = "100% effect per AP"
        Character['Powers']['Detail'][powername]['AgilityEffect'] = "Double or halve per direction"
        Character['Powers']['Detail'][powername]['Flight'] = (Character['Agility_Effects']['Move'])*10
        Character['Powers']['Detail'][powername]['APCostFlight'] = 2
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class HeightenedAttack(PowerBase):
    def __init__(self, Character):
        powername = 'Heightened Attack'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'HP Bonus of 2d10 and 1d4 DD'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = self.range
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['DD'] = "1d4"
        Character['Powers']['Detail'][powername]['HP'] = roll_effects(2,10)  #need to add up all HP for character sheet
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class HeightenedDefense(PowerBase):
    def __init__(self, Character):
        powername = 'Heightened Defense'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Defensive HP Bonus of 3d8 and -1 DD'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = self.range
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['DD'] = "-1"
        Character['Powers']['Detail'][powername]['HP'] = roll_effects(3,8)  #need to add up all HP for character sheet
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class HeightenedExpertise(PowerBase):
    def __init__(self, Character):
        powername = 'Heightened Expertise'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = '10% HP with 1d4 weapons, may take all with one weapon'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = self.range
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Special'] = "Fancy Manoeuvres: if over 50% HP with any weapon"
        Character['Powers']['Detail'][powername]['HP'] = roll_effects(1,4)  #need to add up all HP for character sheet
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)


class HeightenedSenses(PowerBase):
    def __init__(self, Character):
        powername = 'Heightened Senses'
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
        Character['Powers']['Detail'][powername]['Augmentations'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['Type'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['APCost'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['Duration'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['Range'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['Special'] = {}
        batypecheck = roll_effects(1,12)
        for power in range(batypecheck):
            if batypecheck == 1:
                Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Amplified Hearing"
                Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'][str(power + 1)] = "Sensitive to sound, hear low noise, through doors, walls"
                Character['Powers']['Detail'][powername]['Augmentations']['APCost'][str(power + 1)] = "1-3"
                Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'][str(power + 1)] = 6
                Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'][str(power + 1)] = "Personal"
                Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Duration'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'][str(power + 1)] = "round"
                Character['Powers']['Detail'][powername]['Augmentations']['Range'][str(power + 1)] = (Character['Statistics']['Stamina']+2)
                Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Navigate in Darkness"
            elif batypecheck == 2:
                Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Radio Hearing"
                Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'][str(power + 1)] = "Hear all radio bounds"
                Character['Powers']['Detail'][powername]['Augmentations']['APCost'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'][str(power + 1)] = "Personal"
                Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Duration'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'][str(power + 1)] = "round"
                Character['Powers']['Detail'][powername]['Augmentations']['Range'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "10% Patrol DM"
            elif batypecheck == 3:
                Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Super Hearing"
                Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'][str(power + 1)] = "Hear normally at range"
                Character['Powers']['Detail'][powername]['Augmentations']['APCost'][str(power + 1)] = 2
                Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'][str(power + 1)] = 6
                Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'][str(power + 1)] = "Personal"
                Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Duration'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'][str(power + 1)] = "round"
                Character['Powers']['Detail'][powername]['Augmentations']['Range'][str(power + 1)] = (Character['Statistics']['Stamina']+Character['Statistics']['Intelligence']+2)*10
            elif batypecheck == 4:
                Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Ultrasonic Hearing"
                Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'][str(power + 1)] = "Hear but not understand any frequency"
                Character['Powers']['Detail'][powername]['Augmentations']['APCost'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'][str(power + 1)] = 3
                Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'][str(power + 1)] = "Personal"
                Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Duration'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'][str(power + 1)] = "round"
                Character['Powers']['Detail'][powername]['Augmentations']['Range'][str(power + 1)] = (Character['Statistics']['Stamina']+2)
            elif batypecheck == 5:
                Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Sensitive Smell and Taste"
                Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'][str(power + 1)] = "Detect any sense or substance"
                Character['Powers']['Detail'][powername]['Augmentations']['APCost'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'][str(power + 1)] = 3
                Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'][str(power + 1)] = "Personal"
                Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Duration'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'][str(power + 1)] = "round"
                Character['Powers']['Detail'][powername]['Augmentations']['Range'][str(power + 1)] = "Not Applicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Use to track"
            elif batypecheck == 6:
                Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Sensitive Touch"
                Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'][str(power + 1)] = "Sensitive touch, read impressions with fingers etc"
                Character['Powers']['Detail'][powername]['Augmentations']['APCost'][str(power + 1)] = 3
                Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'][str(power + 1)] = 3
                Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'][str(power + 1)] = "Personal"
                Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Duration'][str(power + 1)] = 3
                Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'][str(power + 1)] = "round"
                Character['Powers']['Detail'][powername]['Augmentations']['Range'][str(power + 1)] = (Character['Statistics']['Stamina']+2)
                Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Navigate in Darkness"
            elif batypecheck == 7:
                Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Infrared Vision"
                Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'][str(power + 1)] = "See heat patterns and traces"
                Character['Powers']['Detail'][powername]['Augmentations']['APCost'][str(power + 1)] = 0
                Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'][str(power + 1)] = "Personal"
                Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Duration'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'][str(power + 1)] = "Permanent"
                Character['Powers']['Detail'][powername]['Augmentations']['Range'][str(power + 1)] = "Normal Vision"
                Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "See in Darkness Generation"
            elif batypecheck == 8:
                Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Microscopic Vision"
                Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'][str(power + 1)] = "Magnify objects, base 5 times"
                Character['Powers']['Detail'][powername]['Augmentations']['APCost'][str(power + 1)] = "1-3"
                Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'][str(power + 1)] = 3
                Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'][str(power + 1)] = "Personal"
                Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Duration'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'][str(power + 1)] = "round"
                Character['Powers']['Detail'][powername]['Augmentations']['Range'][str(power + 1)] = "Reading Distance"
            elif batypecheck == 9:
                Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Telescopic Vision"
                Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'][str(power + 1)] = "See normally at range"
                Character['Powers']['Detail'][powername]['Augmentations']['APCost'][str(power + 1)] = 2
                Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'][str(power + 1)] = 2
                Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'][str(power + 1)] = "Personal"
                Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Duration'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'][str(power + 1)] = "round"
                Character['Powers']['Detail'][powername]['Augmentations']['Range'][str(power + 1)] = (Character['Statistics']['Stamina']+Character['Statistics']['Intelligence'])*10
            elif batypecheck == 10:
                Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Ultraviolet Vision"
                Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'][str(power + 1)] = "See clearly at night"
                Character['Powers']['Detail'][powername]['Augmentations']['APCost'][str(power + 1)] = 0
                Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'][str(power + 1)] = "Personal"
                Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Duration'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'][str(power + 1)] = "Permanent"
                Character['Powers']['Detail'][powername]['Augmentations']['Range'][str(power + 1)] = "Normal Vision"
            elif batypecheck == 11:
                Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "X-Ray Vision"
                Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'][str(power + 1)] = "See through substances"
                Character['Powers']['Detail'][powername]['Augmentations']['APCost'][str(power + 1)] = "1-5"
                Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'][str(power + 1)] = 15
                Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'][str(power + 1)] = "Personal"
                Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Duration'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'][str(power + 1)] = "round"
                Character['Powers']['Detail'][powername]['Augmentations']['Range'][str(power + 1)] = (Character['Statistics']['Stamina'])/5
                Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "See in Darkness Generation"
            else:
                Character['Powers']['Detail'][powername]['Augmentations']['Type'][str(power + 1)] = "Vibratory Vision"
                Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'][str(power + 1)] = "See inconsistence in air, invisible, immaterial, astral, phantasmal"
                Character['Powers']['Detail'][powername]['Augmentations']['APCost'][str(power + 1)] = "5"
                Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'][str(power + 1)] = 30
                Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'][str(power + 1)] = "Personal"
                Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'][str(power + 1)] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Augmentations']['Duration'][str(power + 1)] = 1
                Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'][str(power + 1)] = "round"
                Character['Powers']['Detail'][powername]['Augmentations']['Range'][str(power + 1)] = normal_round((Character['Statistics']['Stamina'])/5)
                Character['Powers']['Detail'][powername]['Augmentations']['Special'][str(power + 1)] = "Blocked by some light soruces"
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class HeightenedSpeed(PowerBase):
    def __init__(self, Character):
        powername = 'Heightened Speed'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Run at increased speeds'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = roll_ap(self.range)
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['ExtraAction'] = 1
        Character['Powers']['Detail'][powername]['Speed'] = (Character['Statistics']['Agility'] + Character['Statistics']['Stamina'] + Character['Statistics']['Stamina'])*3
        if Character['Powers']['Detail'][powername]['Speed'] > 150:
            addspeed = roll_effects(1,100)*10
            Character['Powers']['Detail'][powername]['Speed'] + addspeed
        if Character['Powers']['Detail'][powername]['Speed'] > 500:
            Character['Powers']['Detail'][powername]['RunFrictionless'] = "Yes"
        if Character['Powers']['Detail'][powername]['Speed'] > 1000:
            Character['Powers']['Detail'][powername]['LightSpeed'] = "Yes"
            Character['Powers']['Detail'][powername]['CreateVortex'] = "Yes"
            Character['Powers']['Detail'][powername]['MaxWeight'] = "3kg per 500km"
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)
            Character['Powers']['Detail'][powername]['Speed'] = roll_effects(2,10) * roll_effects(2,10)
            if Character['Powers']['Detail'][powername]['Speed'] > 150:
                addspeed = roll_effects(1,100)*10
                Character['Powers']['Detail'][powername]['Speed'] + addspeed
            if Character['Powers']['Detail'][powername]['Speed'] > 1000:
                Character['Powers']['Detail'][powername]['LightSpeed'] = "Yes"

class IceGeneration(PowerBase):
    def __init__(self, Character):
        powername = 'Ice Generation'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Decrease temperature and make ice'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = (Character['Statistics']['Strength'] + Character['Statistics']['Agility'])
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['FreezeSave'] = "SA + AG + LK"
        Character['Powers']['Detail'][powername]['Immunity'] = "Low temperatures"
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class Immateriality(PowerBase):
    def __init__(self, Character):
        powername = 'Immateriality'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Be ghostlike'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = self.range
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Flight'] = (Character['Agility_Effects']['Move'])*10
        Character['Powers']['Detail'][powername]['Immunity'] = "HTH"
        Character['Powers']['Detail'][powername]['Special'] = "Affected by spells, sound light etc."
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class Immortality(PowerBase):
    def __init__(self, Character):
        powername = 'Immortality'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Will not die of old age'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = self.range
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        agecheck = roll_effects(1,100)
        if agecheck <= 10:
            addage = roll_effects(1,100) * roll_effects(1,100)
            Character['Origin']['Age'] = Character['Origin']['Age'] + addage
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)


class InherentPower(PowerBase):
    def __init__(self, Character):
        powername = 'Inherent Power'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Portion of Body gains a power'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = self.range
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Augmentations'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['Type'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['StrDetails'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['APCost'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['MaxAP'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['AreaEffect'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['DamageAP'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['Duration'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['DurationUnit'] = {}
        Character['Powers']['Detail'][powername]['Augmentations']['Range'] = {}
        batypecheck = roll_effects(1,6)
        for power in range(batypecheck):
            if batypecheck == 1:
                Character['Powers']['Detail'][powername]['StrDetails'] + " Armour Plated Hands"
                Character['Powers']['Detail'][powername]['APCost'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['MaxAP'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['AreaEffect'] = "Personal"
                Character['Powers']['Detail'][powername]['DamageAP'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Duration'] = "Concentration"
                Character['Powers']['Detail'][powername]['DurationUnit'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Range'] = "Touch"
            elif batypecheck == 2:
                Character['Powers']['Detail'][powername]['StrDetails'] + " Eye Beams"
                Character['Powers']['Detail'][powername]['APCost'] = 1
                Character['Powers']['Detail'][powername]['MaxAP'] = 3
                Character['Powers']['Detail'][powername]['AreaEffect'] = "Character"
                Character['Powers']['Detail'][powername]['DamageAP'] = "1d4"
                Character['Powers']['Detail'][powername]['Duration'] = "Concentration"
                Character['Powers']['Detail'][powername]['DurationUnit'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Range'] = (Character['Statistics']['Agility'] + Character['Statistics']['Strength'])
            elif batypecheck == 3:
                Character['Powers']['Detail'][powername]['StrDetails'] + " Limited Teleportation"
                Character['Powers']['Detail'][powername]['APCost'] = "10+"
                Character['Powers']['Detail'][powername]['MaxAP'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['AreaEffect'] = "Characters"
                Character['Powers']['Detail'][powername]['DamageAP'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Duration'] = "Instantaneouss"
                Character['Powers']['Detail'][powername]['DurationUnit'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Range'] = "100km"
                Character['Powers']['Detail'][powername]['DM'] = "-25 on Personal Teleports"
            elif batypecheck == 4:
                Character['Powers']['Detail'][powername]['StrDetails'] + " Mobile Hair"
                Character['Powers']['Detail'][powername]['APCost'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['MaxAP'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['AreaEffect'] = "Character"
                Character['Powers']['Detail'][powername]['DamageAP'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Duration'] = "Permanent"
                Character['Powers']['Detail'][powername]['DurationUnit'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Range'] = "2"
                Character['Powers']['Detail'][powername]['DD'] = "1d6"
                Character['Powers']['Detail'][powername]['Special'] = "Hair used as another limb"
            elif batypecheck == 5:
                Character['Powers']['Detail'][powername]['StrDetails'] + " Paralysis Singer in Fingertips"
                Character['Powers']['Detail'][powername]['APCost'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['MaxAP'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['AreaEffect'] = "Personal"
                Character['Powers']['Detail'][powername]['DamageAP'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Duration'] = "24 turns - victim (SA + 1d4)"
                Character['Powers']['Detail'][powername]['DurationUnit'] = "turn"
                Character['Powers']['Detail'][powername]['Range'] = "Touch"
                Character['Powers']['Detail'][powername]['Save'] = "ST + SA + LK"
            else:
                Character['Powers']['Detail'][powername]['StrDetails'] + " Spiked Missile Projection from Hands"
                Character['Powers']['Detail'][powername]['APCost'] = 1
                Character['Powers']['Detail'][powername]['MaxAP'] = "3"
                Character['Powers']['Detail'][powername]['AreaEffect'] = "3 targets"
                Character['Powers']['Detail'][powername]['DamageAP'] = "1d4"
                Character['Powers']['Detail'][powername]['Duration'] = "Instantaneous"
                Character['Powers']['Detail'][powername]['DurationUnit'] = "NotApplicable"
                Character['Powers']['Detail'][powername]['Range'] = (normal_round(Character['Statistics']['Strength']/3))
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class Invisibility(PowerBase):
    def __init__(self, Character):
        powername = 'Invisibility'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Bit visible by normal means'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = self.range
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['DefenseBonus'] = 45
        Character['Powers']['Detail'][powername]['DefenseBonusAttacking'] = 15
        vischeck = roll_effects(1,100)
        if vischeck >= 91:
            Character['Powers']['Detail'][powername]['Special'] = "Permanently invisible"
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)

class Invulnerability(PowerBase):
    def __init__(self, Character):
        powername = 'Invulnerability'
        super().__init__(powers_dict[powername].name, powers_dict[powername].apcost, powers_dict[powername].maxap,\
                         powers_dict[powername].areaeffect, powers_dict[powername].deviceap, powers_dict[powername].damageap,\
                         powers_dict[powername].duration, powers_dict[powername].durationunit, powers_dict[powername].range,\
                         powers_dict[powername].devicerange, powers_dict[powername].choices)
        self.strdetails = 'Character takes 0.25 damage'
        Character['Powers']['Detail'][powername]['StrDetails'] = self.strdetails
        Character['Powers']['Detail'][powername]['APCost'] = self.apcost
        Character['Powers']['Detail'][powername]['MaxAP'] = self.maxap
        Character['Powers']['Detail'][powername]['AreaEffect'] = self.areaeffect
        Character['Powers']['Detail'][powername]['DamageAP'] = self.damageap
        Character['Powers']['Detail'][powername]['Duration'] = self.duration
        Character['Powers']['Detail'][powername]['DurationUnit'] = self.durationunit
        Character['Powers']['Detail'][powername]['Range'] = self.range
        Character['Powers']['Detail'][powername]['Choices'] = self.choices
        Character['Powers']['Detail'][powername]['Damage'] = 0.25
        Character['Powers']['Detail'][powername]['Special'] = "No damage if 2 or less"
        if 'Device' in Character['Powers']['Detail'][powername]:
            Character['Powers']['Detail'][powername]['Device']['DeviceAP'] = roll_ap(self.deviceap)
            Character['Powers']['Detail'][powername]['Device']['DeviceRange'] = roll_ap(self.devicerange)
