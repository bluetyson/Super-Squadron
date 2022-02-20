










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


    dict2 = {}

    print(Character)
    Character['Powers']['Number'] = 4
    Character['Powers']['List'].append('Adaption')
    Character['Powers']['Detail']['Adaption'] = {}
    dict2['Adaption'] = powers.Adaption
    ad = dict2['Adaption'](Character)

    Character['Powers']['Number'] = 5
    Character['Powers']['List'].append('Air Generation')
    Character['Powers']['Detail']['Air Generation'] = {}
    dict2['Air Generation'] = powers.AirGeneration
    ad = dict2['Air Generation'](Character)

    print(Character)



