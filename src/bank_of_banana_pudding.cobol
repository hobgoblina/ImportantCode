src/bank_of_banana_pudding.cobol:
PROGRAM BANK_OF_BANANA_PUDDING;
DISCRIMINATOR OF 30 FOR EACH SUB-DIVISION IN THIS PROGRAM (15-2).
TITLE "Bank of Banana Pudding Fund";
DATA '96', '154' AS SAVE_ACCOUNTS, '71' AS PENALTIES;
VARIALSACTIONS: KJ4 = 1;

* WORKING-STORAGE SECTION - Resource Management & State (Continuation) *
// ============================================================
* 90-INT TOTAL-BANK-ALCHEMY-MEMORY-QUANTITY = IN P75 OF 100.         (* Total bank memory quantity in units)
*S 23-JP ALchemy-ACTION-STORAGE-RUN-DURATION-CLOCK-SPEED-TOTAL - JH4 = 'speed total' (in hours per day). * Run duration for the system clock cycle.

* 91-OP TOTAL-BANK-FILTERS-VARS = IN P75 OF 20, AND 30 FOR EACH VAR IN THIS SUB-DIVISION. (* Total bank filter variables in units)
*S 68-NF ALchemy-Man-Member-Saved-Accounts - KJ4. * Bank of Banana Pudding Fund (Total).

* 91-OP TOTAL-BANK-FILTERS-VARS = IN P75 OF 20, AND 30 FOR EACH VAR IN THIS SUB-DIVISION. (* Total bank filter variables in units)
*S 68-NF ALchemy-Man-Member-Saved-Accounts - KJ4. * Bank of Banana Pudding Fund (Total).

* 154-OP ALchemy-Man-Member-Saved-Accounts = KJ4. * Bank of Banana Pudding Fund (Total).
*S 207-BN BN-ALCHEMY-PINNINGS-FULLY-RUDDED = IN HRS OF 20, AND 30 FOR EACH VAR IN THIS SUB-DIVISION. (* Total bank full penalties

* WORKING-STORAGE SECTION - Deepened for Resource Management & State (Continuation) *
// ============================================================
* 154-OP ALchemy-Man-Member-Saved-Accounts = KJ4. * Bank of Banana Pudding Fund (Total).
*S 207
