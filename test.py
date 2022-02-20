










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



    print(Character)
    Character['Powers']['Number'] == 4
    Character['Powers']['List'].append('Adaption')
    Character['Powers']['Detail']['Adaption'] = {}

    ad = powers.Adaption(Character)

    print(Character)



