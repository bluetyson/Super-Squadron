










if __name__ == '__main__':
    import json
    from super_squadron import powers
    #print(powers.powers_dict)
    test_dict = powers.powers_dict
    print(test_dict['Armour'])
#print(test_dict)
    #ad = powers.Adaption()
    #print(ad.strdetails)
    #print(ad)
    with open('character_test.json') as f:
        Character = json.load(f)
    #print(Character)

    dict2 = {}
    ## Note Artifact powers here for later
    ## Disguise

    powername = 'Adaption'
    Character['Powers']['Number'] = 4
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Adaption
    ad = dict2[powername](Character)

    powername = 'Air Generation'
    Character['Powers']['Number'] = 5
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.AirGeneration
    ad = dict2[powername](Character)

    powername = 'Animal Affinity'
    Character['Powers']['Number'] = 6
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.AnimalAffinity
    ad = dict2[powername](Character)

    powername = 'Armour'
    Character['Powers']['Number'] = 7
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Armour
    ad = dict2[powername](Character)

    powername = 'Astral Projection'
    Character['Powers']['Number'] = 8
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.AstralProjection
    ad = dict2[powername](Character)

    powername = 'Body Augmentation'
    Character['Powers']['Number'] = 9
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.BodyAugmentation
    ad = dict2[powername](Character)

    powername = 'Cybernetics'
    Character['Powers']['Number'] = 10
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Cybernetics
    ad = dict2[powername](Character)

    powername = 'Darkness Generation'
    Character['Powers']['Number'] = 11
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.DarknessGeneration
    ad = dict2[powername](Character)

    powername = 'Death Touch'
    Character['Powers']['Number'] = 12
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.DeathTouch
    ad = dict2[powername](Character)

    powername = 'Defect'
    Character['Powers']['Number'] = 13
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Defect
    ad = dict2[powername](Character)

    powername = 'Density Control'
    Character['Powers']['Number'] = 14
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.DensityControl
    ad = dict2[powername](Character)

    powername = 'Dimensional Gate'
    Character['Powers']['Number'] = 15
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.DimensionalGate
    ad = dict2[powername](Character)

    powername = 'Disintegration Beam'
    Character['Powers']['Number'] = 16
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.DisintegrationBeam
    ad = dict2[powername](Character)

    powername = 'Ego Change'
    Character['Powers']['Number'] = 17
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.EgoChange
    ad = dict2[powername](Character)

    powername = 'Elasticity'
    Character['Powers']['Number'] = 18
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Elasticity
    ad = dict2[powername](Character)

    powername = 'Emotion Control'
    Character['Powers']['Number'] = 19
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.EmotionControl
    ad = dict2[powername](Character)

    powername = 'Energy Absorption'
    Character['Powers']['Number'] = 20
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.EnergyAbsorption
    ad = dict2[powername](Character)

    powername = 'Enhanced Agility'
    Character['Powers']['Number'] = 21
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.EnhancedAgility
    ad = dict2[powername](Character)

    powername = 'Enhanced Charisma'
    Character['Powers']['Number'] = 22
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.EnhancedCharisma
    ad = dict2[powername](Character)

    powername = 'Enhanced Intelligence'
    Character['Powers']['Number'] = 23
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.EnhancedIntelligence
    ad = dict2[powername](Character)

    powername = 'Enhanced Stamina'
    Character['Powers']['Number'] = 24
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.EnhancedStamina
    ad = dict2[powername](Character)

    powername = 'Enhanced Strength'
    Character['Powers']['Number'] = 25
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.EnhancedStrength
    ad = dict2[powername](Character)

    powername = 'Environment Control'
    Character['Powers']['Number'] = 26
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.EnvironmentControl
    ad = dict2[powername](Character)

    powername = 'Fast Recovery'
    Character['Powers']['Number'] = 27
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.FastRecovery
    ad = dict2[powername](Character)

    powername = 'Flame Generation'
    Character['Powers']['Number'] = 28
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.FlameGeneration
    ad = dict2[powername](Character)

    powername = 'Flight'
    Character['Powers']['Number'] = 29
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Flight
    ad = dict2[powername](Character)

    powername = 'Force Beam'
    Character['Powers']['Number'] = 30
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.ForceBeam
    ad = dict2[powername](Character)

    powername = 'Force Field'
    Character['Powers']['Number'] = 31
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.ForceField
    ad = dict2[powername](Character)

    powername = 'Gimmick'
    Character['Powers']['Number'] = 32
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Gimmick
    ad = dict2[powername](Character)

    powername = 'Gravity Control'
    Character['Powers']['Number'] = 33
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.GravityControl
    ad = dict2[powername](Character)

    powername = 'Heightened Attack'
    Character['Powers']['Number'] = 34
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.HeightenedAttack
    ad = dict2[powername](Character)

    powername = 'Heightened Defense'
    Character['Powers']['Number'] = 35
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.HeightenedDefense
    ad = dict2[powername](Character)

    powername = 'Heightened Expertise'
    Character['Powers']['Number'] = 36
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.HeightenedExpertise
    ad = dict2[powername](Character)

    powername = 'Heightened Senses'
    Character['Powers']['Number'] = 37
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.HeightenedSenses
    ad = dict2[powername](Character)

    powername = 'Heightened Speed'
    Character['Powers']['Number'] = 38
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.HeightenedSpeed
    ad = dict2[powername](Character)

    powername = 'Ice Generation'
    Character['Powers']['Number'] = 39
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.IceGeneration
    ad = dict2[powername](Character)

    powername = 'Immateriality'
    Character['Powers']['Number'] = 40
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Immateriality
    ad = dict2[powername](Character)

    powername = 'Immortality'
    Character['Powers']['Number'] = 41
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Immateriality
    ad = dict2[powername](Character)

    powername = 'Inherent Power'
    Character['Powers']['Number'] = 42
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.InherentPower
    ad = dict2[powername](Character)

    powername = 'Invisibility'
    Character['Powers']['Number'] = 43
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Invisibility
    ad = dict2[powername](Character)

    powername = 'Invulnerability'
    Character['Powers']['Number'] = 44
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Invulnerability
    ad = dict2[powername](Character)

    print(Character)



