import mpmath as mp

PARAMS = {
    "A": mp.mpf("1.0"),
    "a": mp.mpf("3.2"),
    "B": mp.mpf("0.9"),
    "b": mp.mpf("2.6"),
    "mu": mp.mpf("7.439993889526777")
}

def F3(gamma):
    P = PARAMS
    t1 = -P["A"] * (P["a"]**3) * mp.e**(-P["a"]*gamma)
    t2 = -P["B"] * (P["b"]**3) * mp.e**(-P["b"]*gamma)
    t3 = 2 * P["mu"]
    return t1 + t2 + t3

def solve_gamma_star():
    return mp.findroot(F3, 0.4)

if __name__ == "__main__":
    gamma_star = solve_gamma_star()
    print("QUCT gamma* =", gamma_star)
