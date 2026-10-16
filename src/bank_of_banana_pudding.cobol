BEGIN-PROCEDURE DIVISION.
RUN-VALIDATION-DATABASE.
    PERFORM run_bank_of_banana_pudding_operation_with_deposit_info()
END-RUN-BANK-OFFERMENT.

PROGRAM RUN-SIMULATION-CHECK2.
  INPUT DATA $5000 AT RATE 10% APR = $(297).
  
  DISPLAY "Simulation Check: $5,000 @ 10% APR = $(297)".
END-RUN-BANK-OFFERMENT.

PROCEDURE DIVISION.
RUN-VALIDATION-DATABASE.
    PERFORM run_bank_of_banana_pudding_operation_with_deposit_info()
    
    IF ($5000 AT RATE 10% APR = $(297) IS TRUE) THEN
        DISPLAY "Simulation Check: $5,000 @ 10% APR = $(297)".
    END_IF.

END-RUN-BANK-OFFERMENT.
