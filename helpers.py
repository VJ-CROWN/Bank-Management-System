def idgen(s):
    ans = (2561483598 * s + 57148) % 4582671548
    return 452845 + (ans % 945825)

def calcsi(p, r, t):
    return round((p * r * t) / 100, 2)

def calcci(p, r, t):
    return round(p * ((1 + (r / 100)) ** t) - p, 2)

def chkpin(p):
    return len(p) == 4 and p.isdigit()

def calcemi(p, r, t):
    if p > 0 and r > 0 and t > 0:
        mr = r / (12 * 100)
        emi = (p * mr * ((1 + mr) ** t)) / (((1 + mr) ** t) - 1)
        return round(emi, 2)
    return 0.0
