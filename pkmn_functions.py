# This py file contains any functions and formulas used in Pokemon as to ensure they are protected and unchanged
# and called only when needed. My goal is to be able to create functions that properly simulate each separate
# modifiers or possibilities and then eventually have a generic function that can handle all of it.

"""
@:param P - Power of a move
@:param Atk - Attack stat of the attacking Pokémon ( Atk or Special Atk depending on the move )
@:param Def - Defense stat of the defending Pokémon ( Def or Special Def depending on the move used against it )
@:param Mod - currently just a catch-all for any modifiers we want to test

@:return: val - the total damage that a move does, based on the factors above
"""
def damage(P,Atk, Def, Mod) -> float: #damage equation from Pokémon
    val = 22*P
    val *= (Atk / Def)
    val /= 50
    val += 2
    val *= Mod
    return val

"""

@:param atk_type - the typing of the Pokemon move
@:param w_condition - the weather condition that is currently active in the battle

@:return modifier - the modifier for the attack depending on the sun or rain weather conditions
"""
def check_sun_or_rain(atk_type,w_condition):
    modifier = 1
    match w_condition:
        case 'Sunny':
            if atk_type == 'Fire':
                modifier *= 2
                return modifier
            elif atk_type == 'Water':
                modifier *= 1/2
                return modifier
            else:
                return modifier
        case 'Rain':
            if atk_type == 'Fire':
                modifier *= 1/2
                return modifier
            elif atk_type == 'Water':
                modifier *= 2
                return modifier
    return modifier