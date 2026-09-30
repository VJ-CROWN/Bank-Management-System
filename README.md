bank management system



NAME- viraaj menon
Registration no- 26bai10819
Course- cse1021
VITyarthi project .

                  1. introduction
The Modular Core Bank Management System is a software simulator designed to model the core operations of commercial retail banking. It was built using Python, it replicates Core Banking Solution (CBS) features including customer account creation, double-entry fund transfers, loan processing, fixed deposit management and interest applications. The system follows software engineering principles by breaking down core logic across six distinct, single-responsibility modules (database, helpers, account_management, financial_operations, analytics, main).   
          2. Problem Statement
Commercial financial systems require strict transactions, account verification and clear audit logs. Unstructured banking scripts suffer from missing input validation, unmonitored credit exposure, and crashes due to unexpected user inputs. This project solves these issues by establishing a modular and procedural banking system that enforces security validation, state checks, transaction logs, and operational separation of concerns.   

       3. Functional Requirements
The system satisfies all functional requirements through three major functional modules:   

3.1 Account Management Module
Account Creation (mkacc): Generates non-sequential account IDs using a mathematical formula and initializes account data.   

Security Controls (chgpin, frzacc, ufzacc): Validates and updates 4-digit numeric PINs; freezes/unfreezes accounts to permit or block changes.   

Account Offboarding (delacc): Enforces defensive rules preventing deletion if an account has active balances, unpaid loans, or active term deposits.   

3.2 Financial Operations Module
Liquidity Transactions (depmn, wdrmn): Handles cash deposits and PIN-authenticated withdrawals with balance checks.   

Inter-Account Transfer (trffnd): Executes double-entry fund transfers between two accounts, updating both ledgers and logging reciprocal audit entries simultaneously.   

Credit & Investment (reqloan, payloan, mkfd, brkfd): Manages loan disbursements, repayments, fixed deposit creation, and premature FD breakings.   

3.3 Analytics & Batch Engine Module
Batch Interest Posting (addintr): Processes annual interest distributions across all active, positive-balance savings accounts in a single batch.   

Treasury Metrics (totbal, totloan, totcnt): Calculates system liquidity, loan liability and total registered customer counts.  

    4. Non-Functional Requirements
The application implements four non-functional software requirements:   

Maintainability & Modularity: Code is cleanly divided into six independent files to ensure high cohesion and low coupling.   

Security & Authentication: All sensitive operations require 4-digit numeric PIN authentication and verify active account status.   

Data Integrity & Consistency: Inter-account transfers and balance updates execute within memory, maintaining synchronized audit logs.   

Reliability & Defensive Logic: State validation guards against negative deposit amounts, overdraft withdrawals, or closing accounts with pending debt.   

              5. Design Diagrams
5.1 Use Case Diagram (Textual Representation)
Primary Actor: Customer / Administrator

Use Cases:

C-1: Create Account
C-2: Deposit / Withdraw Funds
C-3: Transfer Funds
C-4: Apply / Repay Loan
C-5: Create / Break Fixed Deposit
C-6: Freeze / Unfreeze Account
C-7: Run Batch Interest & System Analytics

5.2 Data Schema Structure (database.py)
Plaintext
D = {
    account_id (int): {
        "n": customer_name (str),
        "b": liquid_balance (float),
        "p": pin_code (str),
        "h": transaction_history (list of str),
        "s": account_status (str: "Active" | "frozen"),
        "l": loan_balance (float),
        "fd": fixed_deposit_balance (float),
        "c": account_type (str: "Saving" | "Current")
            6. Design Decisions 
In-Memory Dictionary Storage: Chosen for rapid execution and zero-dependency runtime, allowing pure Python data structure manipulation.   


Modular File Separation: Splitting logic across 6 domain files satisfies academic software engineering criteria while making testing and code navigation straightforward.   

Pseudo-Random ID Generation: Utilizing a Formula in idgen prevents predictable sequential account numbers (1,2,3).
7. Results & Console Output Sample
 Bank Management System 
1: Deposit money            2: Freeze Account      3: Create FD
4: Account Info        5: Add Account          6: Withdraw
7: Apply Loan          8: Change PIN          9: Transfer money
10: Break FD           11: Unfreeze Account   12: Check Loan
13: Repay Loan         14: Simple Interest    15: Check FD
16: Delete History      17: Change Type        18: Compound Interest
19: Annual Interest
20: EMI Calc     21: Close Account      22: System Stats
23: Exit
Choice: 5
Name: RONALDO
Initial Deposit: 5000
PIN: 1234
Account created! ID: 452845

              8. Testing Approach
Test Case ID	Test Description	Inputs	Expected Outcome	Pass/Fail
TC-01	Valid Account Creation	Name: RONALDO, Deposit: 1000, PIN: 1234	Account ID generated, returns success	Pass
TC-02	Invalid PIN Length	Name: MESSI, Deposit: 500, PIN: 12	Returns 0 / Error	Pass
TC-03	Overdraft Withdrawal	ID: 452845, PIN: 1234, Amount: 50000	Returns False / Error	Pass
TC-04	Inter-Account Transfer	Source: 452845, Target: 452846, Amt: 200	Source debited, Target credited	Pass
TC-05	Close Account with Debt	ID: 452845, PIN: 1234 (Loan > 0)	Deletion blocked with Error	Pass


           9. Challenges Faced
State Consistency Across File Imports: Ensuring that all modules modified the shared dictionary D in database.py without creating local import copies was resolved using direct module attribute references.   

Menu Interaction Mapping: 23 clean menu choices were done by taking input calls directly to helping and managing functions.   


  10. Learnings & Key Takeaways
Practical application of procedural modular design in Python.   

Implementation of basic software security patterns like PIN validation, state freezing

          11. Future Enhancements
Database Integration: Replacing in-memory dictionary storage with persistent SQL databases.   

Graphical User Interface (GUI): Developing a modern desktop interface.

REST API & Web Interface: Exposing core banking functions via Flask/FastAPI for web and mobile frontends.


                12. References
Python Software Foundation. Python 3.12 Documentation — Modules and Packages.

VITyarthi Project Guidelines.

 

 

 

 

 
