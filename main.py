from database import D
from helpers import calcsi, calcci, calcemi
from account_management import mkacc, chgpin, getinfo, frzacc, ufzacc, delacc, chgtyp
from financial_operations import depmn, wdrmn, trffnd, reqloan, payloan, mkfd, brkfd, chkloan, chkfd
from analytics import clrhst, addintr, totloan, totbal, totcnt

def banking(c):

    if c == "1":
        print("Ok") if depmn(int(input("ID: ")), float(input("Amount: "))) else print("Error")

    elif c == "2":
        print("Ok") if frzacc(int(input("ID: ")), input("PIN: ")) else print("Error")

    elif c == "3":
        print("Ok") if mkfd(int(input("ID: ")), input("PIN: "), float(input("FD Amount: "))) else print("Error")

    elif c == "4":
        info = getinfo(int(input("ID: ")), input("PIN: "))
        if info:
            print("Name:", info["n"])
            print("Type:", info["c"])
            print("Status:", info["s"])
            print("Balance:", info["b"])
            print("Loan:", info["l"])
            print("Fixed Deposit:", info["fd"])
            print("History:", info["h"])
        else:
            print("Error: Invalid ID or PIN")

    elif c == "5":
        id = mkacc(input("Name: "), float(input("Initial Deposit: ")), input("PIN: "))
        print("Account created! ID:", id) if id else print("Error: Invalid PIN")

    elif c == "6":
        print("Ok") if wdrmn(int(input("ID: ")), input("PIN: "), float(input("Amount: "))) else print("Error")

    elif c == "7":
        print("Ok") if reqloan(int(input("ID: ")), input("PIN: "), float(input("Loan Amount: "))) else print("Error")

    elif c == "8":
        print("Ok") if chgpin(int(input("ID: ")), input("Old PIN: "), input("New PIN: ")) else print("Error")

    elif c == "9":
        print("Ok") if trffnd(int(input("From ID: ")), input("PIN: "), int(input("To ID: ")), float(input("Amount: "))) else print("Error")

    elif c == "10":
        print("Ok") if brkfd(int(input("ID: ")), input("PIN: ")) else print("Error")

    elif c == "11":
        print("Ok") if ufzacc(int(input("ID: ")), input("PIN: ")) else print("Error")

    elif c == "12":
        l = chkloan(int(input("ID: ")), input("PIN: "))
        print("Loan Amount:", l) if l >= 0 else print("Error")

    elif c == "13":
        print("Ok") if payloan(int(input("ID: ")), input("PIN: "), float(input("Repay Amount: "))) else print("Error")

    elif c == "14":
        si = calcsi(float(input("Principal: ")), float(input("Rate: ")), int(input("Time: ")))
        print("Simple Interest:", si)

    elif c == "15":
        fd = chkfd(int(input("ID: ")), input("PIN: "))
        print("Fixed Deposit Amount:", fd) if fd >= 0 else print("Error")

    elif c == "16":
        print("Ok") if clrhst(int(input("ID: ")), input("PIN: ")) else print("Error")

    elif c == "17":
        print("Ok") if chgtyp(int(input("ID: ")), input("PIN: "), input("New Type (savings/current): ")) else print("Error")

    elif c == "18":
        ci = calcci(float(input("Principal: ")), float(input("Rate: ")), int(input("Time: ")))
        print("Compound Interest:", ci)

    elif c == "19":
        print("Ok") if addintr(float(input("Interest Rate %: "))) else print("Error")

    elif c == "20":
        emi = calcemi(float(input("Loan Principal: ")), float(input("Annual Rate: ")), int(input("Months: ")))
        print("Monthly EMI:", emi)

    elif c == "21":
        print("Ok") if delacc(int(input("ID: ")), input("PIN: ")) else print("Error: Balance/Loan/FD must be 0")

    elif c == "22":
        print("Accounts:", totcnt())
        print("Total balance:", totbal())
        print("Total loans:", totloan())

    elif c == "23":
        print("Goodbye bro")
        return False

    else:
        print("Error: Not possible bruh")

    return True

def main():
    while True:
        print("\n Bank Management System(MAKE THE ID FIRST BRO-_-) ")
        print("1: Deposit money            2: Freeze Account      3: Create FD")
        print("4: Account Info        5: Add Account          6: Withdraw")
        print("7: Apply Loan          8: Change PIN          9: Transfer money")
        print("10: Break FD           11: Unfreeze Account   12: Check Loan")
        print("13: Repay Loan         14: Simple Interest    15: Check FD")
        print("16: Delete History      17: Change Type        18: Compound Interest")
        print("19: Annual Interest")
        print("20: EMI Calc     21: Close Account      22: System Stats")
        print("23: Exit")

        if not banking(input("Choice: ")):
            break

if __name__ == "__main__":
    main()
