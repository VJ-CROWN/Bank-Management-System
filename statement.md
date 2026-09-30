System Requirements: Core Bank Management System

          Problem Statement

Managing retail bank accounts, customer records and ledger balances manually or through scripts is insecure error-prone and inefficient. Commercial financial software requires verification, double-entry transaction posting, credit risk monitoring and state-based access controls to prevent unauthorized withdrawals, overdrafts and missing audit trails.

The Core Bank Management System is designed as a lightweight command-line Python solution that models essential core banking operations—including account lifecycle management PIN-secured liquidity transactions, loan disbursements, fixed deposits, compound/EMI calculations and batch administrative analytics.









            Scope of the Project

The project focuses on software architecture and procedural core Python design across 6 dedicated modules:

Account Lifecycle & Security: Auto-generates non-sequential account numbers using pseudo-random formulas validates 4-digit PINs, toggles account status (freezing/unfreezing) updates classification types and enforces zero-liability conditions prior to account deletion.

Transaction & Ledger Operations: Executes cash deposits authenticated withdrawals, entry inter-account wire transfers with reciprocal audit logging, loan disbursements/repayments and term deposit (FD) creation/breaking.

Financial Calculators & Treasury Analytics: Computes interest compound interest and loan Equated Monthly Installment (EMI) schedules. Offers batch interest posting across all savings accounts and tracks total institutional liquidity, credit exposure and customer count.

State Validation & Boundary Checking: Implements verification rules (if balance >= amount: if status == "Active": if loan == 0:) to ensure invalid or unauthorized requests do not compromise ledger integrity.











Non-Functional & Non-Technical     Requirements

          Usability & Interface

Terminal output displays operational status responses (Ok, Error or detailed summary outputs).

Menu prompts clearly specify input expectations (Account ID, PIN amounts) to ensure ease of navigation for operators.



   Reliability & Defensive Logic

Functional calls execute state validation (chkacc, chkpin, chkloan chkfd) prior to state modification.

Mathematical calculations incorporate boundary guards (if p > 0 and r > 0 and t > 0: b >= m) to prevent balances zero-division errors and invalid financial state creation.





  Maintainability & Architecture

Separation of Concerns: Interactive terminal menu dispatching in main.py is decoupled from core domain operations in business logic modules.

Global State Isolation: In-memory ledger storage is isolated inside database.py and accessed through interfaces.






        Portability & Environment

Executable on any Python 3.x environment without requiring third-party library dependencies (pip install).

Academic Evaluators: Reviewers assessing design principles, state management, procedural logic and structural boundary checks in Python.






             Key Modules Built

database.py: Holds the central in-memory dictionary data structure (D) storing all customer records and ledgers.


helpers.py: Contains engines, for account ID generation (idgen) PIN validation (chkpin) simple/compound interest and EMI calculations.


account_management.py: Manages customer onboarding, PIN changes, account freezing/unfreezing account classification updates and safe closure logic.


financial_operations.py: Handles deposits, withdrawals, double-entry transfers, loan applications/repayments and term deposit creation/liquidation.


analytics.py: Calculates system- treasury metrics (total balances, total loans, account count) transaction history clearing and batch interest distribution.


main.py: Drives the CLI menu loop and handles user input routing.
