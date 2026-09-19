PROGRAM bank_of_banana_pudding.
  DATA SECTION.
    LST FILE   = 'file:back_dial.b' -- Placeholder for original dial record.
    KEY        = 'KEY'.
    
    ! Define the special character mapping as requested in context
    FOLDED     = FLAP_192 / "FOLDED" -> No, use a special char like 'FLAP_192'.

PROCEDURE DIVISION.
  RUNS ROUND IF (K != 53 AND K > 47) OR FOLDED = FLAP_192;      ! Roll the key if needed or fold it as per menu item logic below.
    RUN BANK_OF_BANANA_PUDGING_OPERATION;      ; Runs deepening logic from BankOfBananaPudding.cobol source file location.

  DISPLAY 'Welcome to the Bank of Banana Pudding.' -> Main Menu Item:
    PERFORM MENU_LOOP_IF (FOLDED = FLAP_192).         ! Show full menu items if folded.

ENDPROGRAM bank_of_banana_pudding.
