from database import D
from account_management import chkacc

def depmn(a, m):
    if chkacc(a) and D[a]["s"] == "Active" and m > 0:
        D[a]["b"] = D[a]["b"] + m
        D[a]["h"].append("+" + str(m))
        return True
    return False

def wdrmn(a, p, m):
    if chkacc(a) and D[a]["s"] == "Active" and D[a]["p"] == p and m > 0 and D[a]["b"] >= m:
        D[a]["b"] -= m
        D[a]["h"].append("-" + str(m))
        return True
    return False

def trffnd(src, pin, dst, m):
    if chkacc(src) and chkacc(dst) and D[src]["s"] == "Active" and D[dst]["s"] == "Active" and D[src]["p"] == pin and m > 0 and D[src]["b"] >= m:
        D[src]["b"] = D[src]["b"] - m
        D[dst]["b"] = D[dst]["b"] + m
        D[src]["h"].append("Trf Out: -" + str(m) + " to " + str(dst))
        D[dst]["h"].append("Trf In: +" + str(m) + " from " + str(src))
        return True
    return False

def reqloan(a, pin, m):
    if chkacc(a) and D[a]["s"] == "Active" and D[a]["p"] == pin and m > 0:
        D[a]["l"] = D[a]["l"] + m
        D[a]["b"] = D[a]["b"] + m
        D[a]["h"].append("Loan Approved: +" + str(m))
        return True
    return False

def payloan(a, pin, m):
    if chkacc(a) and D[a]["s"] == "Active" and D[a]["p"] == pin and m > 0 and D[a]["l"] >= m and D[a]["b"] >= m:
        D[a]["b"] = D[a]["b"] - m
        D[a]["l"] = D[a]["l"] - m
        D[a]["h"].append("Loan Repaid: -" + str(m))
        return True
    return False

def mkfd(a, pin, m):
    if chkacc(a) and D[a]["s"] == "Active" and D[a]["p"] == pin and m > 0 and D[a]["b"] >= m:
        D[a]["b"] = D[a]["b"] - m
        D[a]["fd"] = D[a]["fd"] + m
        D[a]["h"].append("FD Created: -" + str(m))
        return True
    return False

def brkfd(a, pin):
    if chkacc(a) and D[a]["p"] == pin and D[a]["fd"] > 0:
        m = D[a]["fd"]
        D[a]["b"] = D[a]["b"] + m
        D[a]["fd"] = 0.0
        D[a]["h"].append("FD Broken: +" + str(m))
        return True
    return False

def chkloan(a, pin):
    if chkacc(a) and D[a]["p"] == pin:
        return D[a]["l"]
    return -1.0

def chkfd(a, pin):
    if chkacc(a) and D[a]["p"] == pin:
        return D[a]["fd"]
    return -1.0
