from database import D
from helpers import chkpin, idgen

def chkacc(a):
    return a in D

def mkacc(n, b, p):
    if not chkpin(p) or b < 0:
        return 0
    id = idgen(len(D) + 1000)
    D[id] = {"n": n, "b": b, "p": p, "h": ["Init: " + str(b)], "s": "Active", "l": 0.0, "fd": 0.0, "c": "Saving"}
    return id

def chgpin(a, opin, npin):
    if chkacc(a) and D[a]["p"] == opin and chkpin(npin):
        D[a]["p"] = npin
        return True
    return False

def getinfo(a, pin):
    if chkacc(a) and D[a]["p"] == pin:
        return D[a]
    return None

def frzacc(a, pin):
    if chkacc(a) and D[a]["p"] == pin:
        D[a]["s"] = "frozen"
        return True
    return False

def ufzacc(a, pin):
    if chkacc(a) and D[a]["p"] == pin:
        D[a]["s"] = "Active"
        return True
    return False

def delacc(a, pin):
    if chkacc(a) and D[a]["p"] == pin and D[a]["b"] == 0 and D[a]["l"] == 0 and D[a]["fd"] == 0:
        del D[a]
        return True
    return False

def chgtyp(a, pin, ntype):
    if chkacc(a) and D[a]["p"] == pin:
        D[a]["c"] = ntype
        return True
    return False
