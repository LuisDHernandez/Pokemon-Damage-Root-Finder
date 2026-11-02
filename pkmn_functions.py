# This py file contains any functions and formulas used in Pokémon as to ensure they are protected and unchanged
# and called only when needed. My goal is to be able to create functions that properly simulate each separate
# modifiers or possibilities and then eventually have a generic function that can handle all of it.
import math
"""
:param P: Power of a move
:param Atk: Attack stat of the attacking Pokémon ( Atk or Special Atk depending on the move )
:param Def: Defense stat of the defending Pokémon ( Def or Special Def depending on the move used against it )
:param Mod: currently just a catch-all for any modifiers we want to test

:return val: the total damage that a move does, based on the factors above
"""
def damage(P:int,Atk:int, Def:int, Mod:float) -> float: #damage equation from Pokémon
    val = 22*P
    val *= (Atk / Def)
    val /= 50
    val += 2
    val *= Mod
    return val

"""
:param atk_type: the typing of the Pokemon move
:param w_condition: the weather condition that is currently active in the battle
:param pkmn_type: the type of the Pokemon
:param def_stat: the defense stat of the Pokemon
:param sp_def_stat: the special defense stat of the Pokemon

:return modifier: the modifier for the attack depending on the sun or rain weather conditions
:return sp_def_stat: the special defense stat of the Pokemon after Sand is checked for Rock types
:return def_stat: the defense stat of the Pokemon after Snow is checked for Ice types
"""
def check_weather(atk_type:str,w_condition:str,pkmn_type:str,def_stat:int,sp_def_stat:int)->float:
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
        case 'Sandstorm':
            if pkmn_type == 'Rock':
                sp_def_stat = 1.5 * sp_def_stat
            return sp_def_stat
        case 'Snow':
            if pkmn_type == 'Ice':
                def_stat = 1.5 * def_stat
            return def_stat
    return modifier

"""
:param crit: Boolean value that is true when the attack is a crit and false if not

:return boost: Int value modifier that multiplies damage by the amount returned
"""
def is_critical_hit(crit:bool)->int:
    boost = 1
    if crit:
        boost = 2
        return boost
    else:
        return boost

def is_multiple_targets(pkmn_count:int)->float:
    if pkmn_count > 1:
        return 3/4 #if a move targets more than one enemy, the power is reduced by 3/4
    else:
        return 1

'''
necessary_attack_value takes in the power of a move and all other modifiers to see if it is enough to K.O a Pokemon.
This makes the variable of the equation the attack stat, A, as the rest will be constants.

:param P: Power of a move
:param Def: Defense stat of the defending Pokémon ( Def or Special Def depending on the move used against it )
:param Mod: currently just a catch-all for any modifiers we want to test
:param D: Damage of the move at neutral position

:return atk_stat: the attack stat required for a K.O.
'''
def necessary_attack_value(P:int, Def:int, Mod:float,D:int)->float:
    val = 22 * P / Def * (1/50) + 2
    val *= Mod
    atk_stat = math.ceil(D/val)
    return atk_stat