










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
    Character['Powers']['Number'] = 6
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Armour
    ad = dict2[powername](Character)

    powername = 'Astral Projection'
    Character['Powers']['Number'] = 7
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.AstralProjection
    ad = dict2[powername](Character)

    powername = 'Body Augmentation'
    Character['Powers']['Number'] = 8
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.BodyAugmentation
    ad = dict2[powername](Character)

    powername = 'Cybernetics'
    Character['Powers']['Number'] = 9
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Cybernetics
    ad = dict2[powername](Character)

    powername = 'Darkness Generation'
    Character['Powers']['Number'] = 10
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.DarknessGeneration
    ad = dict2[powername](Character)

    powername = 'Death Touch'
    Character['Powers']['Number'] = 11
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.DeathTouch
    ad = dict2[powername](Character)

    powername = 'Defect'
    Character['Powers']['Number'] = 12
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.Defect
    ad = dict2[powername](Character)

    powername = 'DensityControl'
    Character['Powers']['Number'] = 13
    Character['Powers']['List'].append(powername)
    Character['Powers']['Detail'][powername] = {}
    dict2[powername] = powers.DensityControl
    ad = dict2[powername](Character)

    print(Character)



