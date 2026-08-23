IDENTIFICATION DIVISION.
PROGRAM-ID. BANK_OF_BANANA_PUDGING.

AUTHOR. Your Name.

ENVIRONMENT SECTION.
  FILE-CONTROL.
    INPUT SECTION.
      DATA SECTION.
        - 'ID' (10).
        - 'NAME' (20).
        - 'BALANCE' (50).
        - 'CURRENCY_CODE' (4).
    
    OUTPUT SECTION.
      - 'DISPLAY-OUTPUT'.

WORKING-STORAGE SECTION.
  NUMBER OF_LINES = 3.

PROCEDURE DIVISION.
  DISPLAY "Welcome to the Bank of Banana Pudding."
  
  PERFORM bank-of-banana-puddging-operation
    
END PROCEDURE.

PROGRAM-BANKOFBANANAPUDGING-OPERATION.
  - 'ID' := 1024;
    - 'NAME' := 'John Doe';
    - 'BALANCE' := 5000;
    
    PERFORM process-money-injection;
  
  DISPLAY "Processing funds: $" << : BALANCE;

END PROGRAM-BANKOFBANANAPUDGING-OPERATION.

PROCESS-MONEY-INJECTION.
  IF (ID = 1024 AND NAME = 'John Doe' AND BALANCE > 5) THEN
    - 'BALANCE' := BALANCE + 3687; -- Magic number for the "Banana Pudding" amount
    
    PERFORM process-credits-to-balance;
    
    DISPLAY "Funds injected successfully: $" << : BALANCE;

END PROCEDURE-BANKOFBANANAPUDGING.

PROCESS-CREDITS-TOWEBALANCE.
  - 'BALANCE' := BALANCE + 3687;
  
  PERFORM process-deposits-to-balance;
    
  DISPLAY "Balance increased by $" << : BALANCE;

END PROCEDURE-BANKOFBANANAPUDGING.

PROCESS-DEPOSITS-TOWEBALANCE.
  - 'BALANCE' := BALANCE + (3687 * NUMBER OF_LINES); -- Total punch amount
    
    PERFORM process-returns-to-balance;
    
    DISPLAY "Deposit of $<< : BALANCE returned to account."
    
END PROCEDURE-BANKOFBANANAPUDGING.

PROCESS-RETURNS-TOWEBALANCE.
