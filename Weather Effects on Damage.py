import pkmn_functions as pf
import Root_Finding_Methods as rf
import math

'''
Weather effects the strength of some moves, accuracy, or even affect certain Pokemon's stats.
I will show how the modifiers from weather linearly effect the solution
'''

# We will use the example of a Mega Charizard-Y using Heat Wave on a neutral target with a Special Defense
# stat of 100 and an HP stat of 150 vs a sun-boosted Heat Wave

def health(dmg):
    return 150 - dmg

regular_HW = math.ceil(pf.damage(95,179,100,1))# Base Charizard Y with no modifiers from crits and assuming it lost it's Fire typing

sun_boosted_HW = math.ceil(pf.damage(95,179,100,1)*pf.check_weather('Fire','Sunny'))

print(regular_HW)
print(sun_boosted_HW)

health_after_regular = health(regular_HW)
print('Health leftover from Heat Wave is: ', health_after_regular)

health_after_sunny = health(sun_boosted_HW)
print('Health leftover from Heat Wave in Sunny weather is: ', health_after_sunny)

print("We see that the Sunny weather boosted the attack value of Heat Wave by 2 and was able to get a KO. What happens"
      " if we want to see what other power moves can we utilize to get a KO?")

def health_as_function(power):
    return 150 - ((22*power)*((179/100)/50)+ 2)

def dhealth_as_function(power):
    return -((22*(179/100)/50)+ 2)


print("We will try to find a solution with Newton's Method. We know that there is enough damage to KO the Pokemon "
      "between power interval [95,190]. I will choose Power = 180, as it might be sufficiently close to the root, otherwise "
      "the method will fail / diverge.")

newton = rf.pkmn_newton(health_as_function,dhealth_as_function,185,1e-6,100)

# We know that damage = 190 will KO, so we want a power that can get us there. We know that 95 power was halfway, and 190 power got us over,
# so our power interval will be [0,250] as it covers all possible powers for moves
print("Now, we will use False Position Method to show a faster solution without the need of calculating a derivative.")
fpm_calc = rf.pkmn_false_position(health_as_function,0,250,1e-12,100)

print("The solution is quickly found that a power of 187.9 at a minimum is needed. Since Heat Wave is base 95 power "
      "and the weather effect of Sun boosts that power by 2, then it's effective power is 190, which is enough for the KO.")

