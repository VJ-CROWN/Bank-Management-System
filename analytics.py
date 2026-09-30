from database import D
from account_management import chkacc

def clrhst(a, pin):
    if chkacc(a) and D[a]["p"] == pin:
        D[a]["h"] = ["History cleared"]
        return True
    return False

def addintr(r):
    if len(D) > 0 and r > 0:
        for a in D:
            if D[a]["s"] == "Active" and D[a]["b"] > 0:
                interest = round((D[a]["b"] * r) / 100, 2)
                D[a]["b"] = D[a]["b"] + interest
                D[a]["h"].append("Interest Added: +" + str(interest))
        return True
    return False

def totloan():
    return sum(D[a]["l"] for a in D)

def totbal():
    return sum(D[a]["b"] for a in D)

def totcnt():
    return len(D)
