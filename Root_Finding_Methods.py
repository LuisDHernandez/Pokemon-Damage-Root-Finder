import math

'''
Bisection Method for Pokémon Damage Calculations
'''
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


'''
Newton's Method for Root Finding
By treating the damage as continuous, we can approximate a solution and then tie it back to the discrete values that are
actually possible in game to ensure a KO.
'''
def pkmn_newton(f, df, p0, TOL, N0):
    i = 1

    print(f"{'i':<5}{'p0':<18}{'p':<18}{'|p-p0|':<18}") #this was from example code in class

    while i <= N0:

        if df(p0) == 0:
            print("Method failed")
            return None

        p = p0 - f(p0) / df(p0)

        error = abs(p - p0)

        print(f"{i:<5}{p0:<18.10f}{p:<18.10f}{error:<18.10e}")

        if error < TOL:
            print("Approximate solution =", p)
            return p

        i = i + 1
        p0 = p

    print("\nThe method failed after", N0, "iterations.")
    return None

'''
False Position Method -> Newton + Bisection as one
'''
def pkmn_false_position(f, p0, p1, TOL, N0):

    # Step 1
    i = 2
    q0 = f(p0)
    q1 = f(p1)

    if q0 * q1 >= 0:
        print("Method failed.")
        return None

    print(f"{'i':<5}{'p0':<16}{'p1':<16}{'p':<16}{'|p-p1|':<16}")

    while i <= N0:

        if q1 - q0 == 0:
            print("Method failed: division by zero.")
            return None

        p = p1 - q1 * (p1 - p0) / (q1 - q0)

        error = abs(p - p1)

        print(f"{i:<5}" f"{p0:<16.10f}" f"{p1:<16.10f}" f"{p:<16.10f}" f"{error:<16.10e}")

        if error < TOL:
            print("Approximate solution =", p)
            return p


        i = i + 1
        q = f(p)

        if q * q1 < 0:
            p0 = p1
            q0 = q1


        p1 = p
        q1 = q

    print("\nThe method failed after", N0, "iterations.")
    return None