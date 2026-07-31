BEGIN PROJECT_BANK_OF_BANANA_PUDDING_3
  SECTION WORKING-STORAGE.
    WID   INTEGER   256;   -- Width to store current transaction ID (1 byte per character of data).
        INIT "INIT";       ; Initial state marker when loading bank from file without first char.

PROCEDURE DIVISION.
    OPEN FILE IF NOT EXISTS '/app/src/bank_of_banana_pudding.bin'.     ; Opens existing or creates the bank .bin if it doesn't exist (creates 0x80B2 as start).
        PERFORM read_bank_from_file;                              ; Reads input from file to WID.

    READ FILE OF IDENTIFIED BY '/app/src/bank_of_banana_pudding.bin' TO IDENTITY DIVISION IF EXISTS;      ; Validates file integrity and loads data into BOLD variables, etc., if it exists or creates new ones otherwise.
        PERFORM load_bank_data INTO WID 1024;                          ; Loads all valid bank data from the identified block (e.g., 0x80B2).

    EXECUTE LOAD_BANK_DATA;                                      /* Runs a dedicated procedure to validate and reconstruct the loaded bank structure */
        VERIFY STRUCTURE OF BANK DATA IS VALID AND CORRECT.            ;; Checks for format compliance, missing fields, etc.
        
        PERFORM display_status_information WITH_IDENTITY DIVISION INTO WID 1024; ; Shows summary status (e.g., "Loading...", "Bank Loaded", "Ready to Run").

    LOAD_BANK_DATA;       /* The procedure that executes bank reconstruction logic based on the loaded data */
    
PROCEDURE DIVISION.
    DISPLAY 'Welcome to the Bank of Banana Pudding.'                               ; Initial welcome message output if no input was provided in previous step (as per original file).
END PROJECT
