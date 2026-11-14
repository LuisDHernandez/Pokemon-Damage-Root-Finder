import pkmn_functions as pf
import Root_Finding_Methods as rf
import matplotlib.pyplot as plt
import numpy as np

'''
Critical hits in Pokemon ignore stat boosts from the defending Pokemon and stat decreases of the attacking Pokemon.
Therefore, Critical Hits are always very powerful in Pokemon.
'''

# A critical hit always doubles the damage that a Pokémon receives from an attack
print("Since a critical hits doubles the damage of a move, then it is simply possible to approximate a root and divide"
      " it by 2 to find an approximate solution. I will compare that method with using a standard root finding method.")

# For a Sceptile with 125 Sp. Atk. against a Pokemon with 140 health and 100 Sp. Def. trying to KO with leaf storm P=130
sceptile_neutral_dmg = pf.damage(130,125,100,1)
print(sceptile_neutral_dmg)
def health(P):
    return 140 - ((22 * P) * ((125 / 100) / 50) + 2)

def crit_health(P):
    return 140 - ((22 * P) * ((250 / 100) / 50) + 2)

print(f"The health remaining on the defending Pokemon is: {round(health(130),0)}")

# With a critical hit
crit = pf.is_critical_hit(True)

sceptile_neutral_dmg *= crit
print(sceptile_neutral_dmg)

'''
We see that the damage is doubled and could K.O the Pokemon. Let's see how the root finding methods do in finding that 
value of 147.
'''

bisect = rf.pkmn_bisection_method(health,130,260,1e-3,100)

# I will plot the graph to show that this interval makes sense.

# Generate 20 evenly spaced x-values from 100 to 300
x = np.linspace(100, 300, 20)

# Health Equation
y = 140 - ((22 * x) * ((125 / 100) / 50) + 2)

# Create the plot
plt.figure(figsize=(12, 16))
plt.plot(x, y, label="y = 140 - ((22 * x) * ((125 / 100) / 50) + 2)", color="blue", linewidth=2)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Plot of the Health Equation")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")  # X-axis line
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")  # Y-axis line
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()

print("Since doubling the damage in Pokemon is the same as doubling the attack stat due to properties of multiplication, then"
      " we can find the power necessary as if Sceptile was stronger.")

sceptile_crit_dmg = pf.damage(130,250,100,1)
print(f"The crit damage is then: {sceptile_crit_dmg}")

rf.pkmn_bisection_method(crit_health,65,130,1e-3,100)
rf.pkmn_false_position(crit_health,0,250,1e-3,100)

print("Again, the false position method is faster in these linear cases and shows that a move of at least 126 power is needed with a crit to get the KO.")