
import numpy as np

def roll_statistic():
    """Roll a random statistic value between 1 and 20 (inclusive)."""
    statistic = np.random.randint(1, 21)
    return statistic

def roll_luck():
    """
    Roll for luck value.
    
    Returns:
        int: Luck value between 0 and 10, where values under 11 give luck.
    """
    luck = 0
    roll = np.random.randint(1, 101)
    if roll < 11:
        luck = 11 - roll
    return luck

def roll_origin():
    """
    Roll for character origin type and age.
    
    Returns:
        dict: Dictionary containing 'Origin', 'Age', 'Artifact', and 'Lifespan' keys.
    """
    origin_dict = {}
    roll = np.random.randint(1, 11)
    origin_dict['Artifact'] = "No"
    origin_dict['Lifespan'] = "Human"
    if roll <= 3:
        origin = "Mutant"
        age = np.random.randint(1, 13) + 15
    elif roll == 4:
        origin = "Self Developed"
        age = np.random.randint(1, 13) + 25
    elif roll == 5:
        origin = "Supernatural"
        age = np.random.randint(1, 11) + 20
    elif roll == 6:
        origin = "Designed or Sponsored"
        age = np.random.randint(1, 13) + 25
    elif roll == 10:
        origin = "Alien"
        age = np.random.randint(1, 11) * np.random.randint(1, 7)
        lifespan = np.random.randint(1, 21) * np.random.randint(1, 21)
        origin_dict['Lifespan'] = lifespan
    else:
        origin = "Accidental/Scientific"
        age = np.random.randint(1, 9) * np.random.randint(1, 7) + 25
        artifact_roll = np.random.randint(1, 101)
        if artifact_roll <= 5:
            origin_dict['Artifact'] = "Yes"
        
    origin_dict['Origin'] = origin
    origin_dict['Age'] = age
    return origin_dict

def roll_effects(number, dice_sides):
    """
    Roll multiple dice and sum the results.
    
    Args:
        number (int): Number of dice to roll.
        dice_sides (int): Number of sides on each die.
    
    Returns:
        int: Sum of all dice rolls.
    """
    roll_total = 0
    for roll in range(number):
        dice_roll = np.random.randint(1, dice_sides + 1)
        roll_total = roll_total + dice_roll
        
    return roll_total
    
def roll_main_statistics(Statistics):
    """
    Roll main statistics until their sum is greater than 60.
    
    Args:
        Statistics (dict): Dictionary of statistics to populate.
    
    Returns:
        dict: Updated statistics dictionary.
    """
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
    """
    Calculate Action Points (AP) for a device based on a formula string.
    
    Args:
        deviceap (str): Formula string for calculating AP (e.g., "2d4x4", "1d6+3", "2d6").
    
    Returns:
        str or int: Original string if it's a special value, otherwise calculated AP.
    """
    if "NotApplicable" in deviceap or "Unlimited" in deviceap or "Variable" in deviceap or "HTH" in deviceap:
        return deviceap
    
    # Handle multiplication with optional addition: "2d4x4+3" or "2d4x4"
    if 'x' in deviceap:
        if '+' in deviceap:
            roll_plus = deviceap.split('+')
            plus = int(roll_plus[1])
            roll_mult = roll_plus[0].split('x')
            roll_list = roll_mult[0].split('d')
            devap = roll_effects(int(roll_list[0]), int(roll_list[1])) * int(roll_mult[1]) + plus
            return devap
        else:
            roll_mult = deviceap.split('x')
            roll_list = roll_mult[0].split('d')
            devap = roll_effects(int(roll_list[0]), int(roll_list[1])) * int(roll_mult[1])
            return devap
    
    # Handle simple dice rolls with addition: "1d6+3"
    elif '+' in deviceap:
        roll_plus = deviceap.split('+')
        plus = int(roll_plus[1])
        if 'd' in roll_plus[0]:
            roll_list = roll_plus[0].split('d')
            devap = roll_effects(int(roll_list[0]), int(roll_list[1])) + plus
            return devap
        else:
            return int(roll_plus[0]) + plus
    
    # Handle simple dice rolls: "2d6"
    elif 'd' in deviceap:
        roll_list = deviceap.split('d')
        devap = roll_effects(int(roll_list[0]), int(roll_list[1]))
        return devap
    
    # Handle 'or' statements
    elif 'or' in deviceap:
        roll_list = deviceap.split('or')
        devcheck = roll_effects(1, 100)
        if devcheck <= 50:
            devap = 20
        else:
            devap = 10
        return devap
    
    # Try to return as integer if it's a simple number
    try:
        return int(deviceap)
    except ValueError:
        # If all else fails, return the original string
        return deviceap

