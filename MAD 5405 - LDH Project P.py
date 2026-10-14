import math
import pkmn_functions as pf
# Resources Online
# https://calc.pokemonshowdown.com/champions.html?mode=champions
# https://play.pokemonshowdown.com/teambuilder
# https://pokebase.app/pokemon-champions/moves

def pkmn_bisection_method(f,a,b,TOL,N0):
    if f(a) * f(b) >= 0:
        print("Bisection method cannot be applied.")
        print(" Make sure f(a)f(b)<0 ")
        return None

    i = 1
    FA = f(a)

    while i <= N0:
        p = a + (b - a) / 2
        FP = f(p)

        print(f"Iteration {i}:")
        print(f"a = {a:.5f}")
        print(f"b = {b:.5f}")
        print(f"p = {p:.5f}")
        print(f"f(p) = {FP:.5f}")
        print()

        if FP == 0 or (b - a) / 2 < TOL:
            print(f"Approximate root = {p:.8f}")
            print(f"No. of iterations = {i}")
            return p

        i = i + 1

        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p

    print(f"Method failed after {N0} iterations.")
    return None

"""
num = damage(50,100,90,1) # calculate damage for a move with 50 Power and an atk 0f 100 versus a def of 90 with no modifiers active
lower_bound = math.floor(0.85 * num)
upper_bound = math.floor(num)

interval = [lower_bound,upper_bound]
print(f"The amount of damage possible is in the range: {interval}")
"""
# We see the proof above of showing an interval for damage done by a move. Now we can create a function R(x) = H - D(x) where
# R is the remaining health of a Pokémon after taking damage D and subtracting it from defending Pokémon's health H for a move with x power

def remainder(power, A_atk, D_def, Mod, dmg_func, health_Def, lower = 0.85, upper = 1):
    H = health_Def
    dmg = dmg_func(power, A_atk, D_def, Mod)
    health_interval = [math.ceil(H - upper * dmg), math.ceil(H - lower * dmg)]
    return health_interval

print("We have a level 50 Infernape with Special Attack = 124 use the move Scorching Sands which has 70 base power on a "
      "level 50 Conkeldurr with 180HP and Special Defense = 85")
leftover_health = remainder(70,124,85,1,pf.damage,180)
print(f"The amount of health leftover from the attack with given parameters is {leftover_health}")
print("We see that the damage done is not enough to K.O. the Conkeldurr. Therefore, if we wanted to ensure a K.O. we will need"
      " to consider modifiers, EVs, and more.")

# Assume we do not know the power of a move needed to knock out Conkeldurr in the example below. Then, we must
# find an interval where the remainder health interval meets the conditions for the Bisection Method, and we can
# approximate the root.
def r(x): # Infernape with no EV training example
    # return H - D(x)
    # Assuming Mod = 1
    # A = Attacker stat using Infernape
    # D = Defender stat using Conkeldurr
    return 180 - (((22*x*(124/85))/50)+2)*1 # specific instance of the damage function pf.damage

def r2(x): # Infernape with EV training example
    # return H - D(x)
    # Assuming Mod = 1
    # A = Attacker stat using Infernape with 32 EV points in A
    # D = Defender stat using Conkeldurr
    return 180 - (((22*x*(156/85))/50)+2)*1 # specific instance of the damage function pf.damage

interval = [0,360] # this interval for damage encompasses the threshold that minimum damage to K.O. is 180. We double the value to approximate an upper bound
root = pkmn_bisection_method(r, interval[0], interval[1], 1e-4, 100)
print(f"The power necessary for Infernape to K.O. Conkeldurr with a special attack move is: {math.ceil(root)}")
print("Since moves have power in the interval [0,250], we see that this solution is impossible. Therefore, we must consider "
      "factors like Stat Boosts, Weather, Same Type Attack Bonus, Critical Hits, and Effort Values.")

print("Say we utilize effort value (EV) training and increase Infernape's special attack stat from 124 to a base max of 156."
      " We assume Conkeldurr did not receive any EV training for defense. Then, we apply bisection method again.")

root2 = pkmn_bisection_method(r2, interval[0], interval[1], 1e-4, 100)
print(f"The power necessary for EV trained Infernape to K.O. Conkeldurr with a special attack move is: {math.ceil(root2)}")
print("We see that this root is within the power interval of [0,250], thus the solution is valid.")
