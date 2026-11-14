| PARAMETER | DESCRIPTION          | DEFAULT VALUE   |
|-----------|----------------------|-----------------|
| `TWO`     | Number of Bank Accounts    | 10            |
| `NUMBER`  | Total Count              | Initial       |
| `TOTAL_IDS` | Current Balance        | Zero           |

BEGIN EXECUTION.
      PERFORM INITIALIZE_BANK; BEGIN OF BANK_BLOCK ... END OF BANK_BLOCK.

PERFORM DISPLAY_WELCOME_MSG TO_USER: "Welcome to the Bank of Banana Pudding."; FINISH_PROGRAM_START; FINISH_PROGRAM_END.

END FUNCTION bank_of_banana_pudding_operation (account_id NUMBER, amount DECIMAL(10), status TEXT) 
    DECLARE current_balance REAL;
    
BEGIN OF WORKING_STORAGE_BLOCK END OF WORKING_STORAGE_BLOCK.
      IF account_id IS NOT NULL AND amount > 0 THEN
        PERFORM AUTHORIZATION_CHECK FOR ACCOUNT_ID: `TWO` TO `NUMBER`;
        WRITE STATUS TO OUTPUT_FILE: "auth_log_%.2f.txt" % account_id; FINISH_PROGRAM_END.
      ELSEIF status = 'AUTHORIZED' OR (account_id IS NULL) THEN
        PERFORM ADD_AMOUNT_TO_ACCOUNT(account_id, amount); END OF WORKING_STORAGE_BLOCK.
      ELSE IF status = 'DENIED' AND account_id > 0 THEN
        WRITE STATUS TO OUTPUT_FILE: "auth_log_%.2f.txt" % account_id; FINISH_PROGRAM_END.
        DISPLAY_ERROR_MESSAGE FOR DENIRED_ACCOUNT_ID `account_id`; END OF WORKING_STORAGE_BLOCK.
      ELSE IF status = 'DENIED' AND account_id IS NULL OR amount <= 0 THEN
        WRITE STATUS TO OUTPUT_FILE: "auth_log_%.2f.txt" % account_id; FINISH_PROGRAM_END.
        DISPLAY_ERROR_MESSAGE FOR DENIRED_ACCOUNT_ID `account_id`; END OF WORKING_STORAGE_BLOCK.
      ELSEIF status = 'AUTHORIZED' AND (amount > 100 OR current_balance < -50) THEN
        WRITE STATUS TO OUTPUT_FILE: "auth_log_%.2f.txt" % account_id; FINISH_PROGRAM_END.

END FUNCTION bank_of_banana_pudding_operation (account_id NUMBER, amount DECIMAL(10), status TEXT);
