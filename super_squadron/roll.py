
def roll_statistic():
    statistic = np.random.randint(1,20)
    return statistic

def roll_luck():
    luck = 0
    roll = np.random.randint(1,100)
    if roll < 11:
        luck = 11 - roll
    return luck

def roll_origin():
    origin_dict = {}
    roll = np.random.randint(1,10)
    origin_dict['Artifact'] = "No"
    origin_dict['Lifespan'] = "Human"
    if roll <= 3:
        origin = "Mutant"
        age = np.random.randint(1,12) + 15
    elif roll == 4:
        origin = "Self Developed"
        age = np.random.randint(1,12) + 25
    elif roll == 5:
        origin = "Supernatural"
        age = np.random.randint(1,10) + 20
    elif roll == 6:
        origin = "Designed or Sponsored"
        age = np.random.randint(1,12) + 25
    elif roll == 10:
        origin = "Alien"
        age = np.random.randint(1,10) * np.random.randint(1,6)
        lifespan = np.random.randint(1,20) * np.random.randint(1,20)
    else:
        origin = "Accidental/Scientific"
        age = np.random.randint(1,8) * np.random.randint(1,6) + 25
        artifact_roll = np.random.randint(1,100)
        if artifact_roll <= 5:
            origin_dict['Artifact'] = "Yes"
        
    origin_dict['Origin'] = origin
    origin_dict['Age'] = age
    return origin_dict

def roll_effects(number, dice_sides):
    roll_total = 0
    for roll in range(number):
        dice_roll = np.random.randint(1,dice_sides)
        roll_total = roll_total + dice_roll
        
    return roll_total
	
def roll_main_statistics(Statistics):
    stats_total = 0
    while stats_total <= 60:
        stats_total = 0
        for index, key in enumerate(Statistics.keys()):
            if index < 5:
                Statistics[key] = roll_statistic()
                stats_total = stats_total + Statistics[key]
                print(key, Statistics[key])
        print("Total:", stats_total)
    return Statistics

def roll_ap(deviceap):
    if "NotApplicable" in deviceap or "Unlimited" in deviceap or "Variable" in deviceap or "HTH":
        return deviceap
    if 'x' in deviceap:
        if '+' in deviceap:
            roll_plus = deviceap.split('+')
            plus = int(roll_plus[1])
            roll_mult = roll_plus[0].split('x')
            roll_list = roll_mult[0].split('d')
            devap = roll_effects(roll_list[0],roll_list[1]) * int(roll_mult[1]) + plus
            return devap
        else:
            roll_mult = deviceap.split('x')
            roll_list = roll_mult[0].split('d')
            devap = roll_effects(roll_list[0],roll_list[1]) * int(roll_mult[1])
    else:
        if 'or' in deviceap:
            roll_list = deviceap.split('or')
            devcheck = roll_effects(1,100)
            if devcheck <= 50:
                devap = 20
            else:
                devap = 10

        #has or in it
    return devap

