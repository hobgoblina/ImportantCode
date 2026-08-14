PROGRAM BANK_OF_BANANA_PUDDING_V2_ENHANCED
  IDENTIFICATION RECORD = 'Bank_of_Banana_Pudding.v2' / INITIALIZATION STATE = NORMAL (IDLE)
    FILE-CONTROL SET(ALL INPUT).

  // --- WORKING-STORAGE FOR REACTIVITY VISUALIZER ASSEMBLY DATA ---
  IDENTIFICATION RECORD ReactivityVisualizer = 'Reactivity_Visualizer_Assembly'.
    ASSIGNMENT REC OF ALL (32 BYTES).

PROCEDURE DIVISION.
  EXECUTIVE SECTION.
    
    SUBROUTINE RUN_BANK_OPS(STATUS_STATUS_ID, RESULT_RESULT_TYPE, DATA_DATA_OBJECT) {
      LOCAL VARIABLES STATEMENT = 'Status: Idle'.

      // Initialize AlchemyManager context to ensure thread safety.
      DBMS_APPLICATION_LOG "Starting Bank of Banana Pudding Initialization..."

      IF (STATUS_STATUS_ID = 'idle' AND NOT EXISTS TaskOfAlchemists(StatusID=Status.Idle)) {
        BEGIN BLOCK EXECUTIVE SECTION;
          // Execute a high-level trigger event: "Initiate Bank of Banana Pudding Operations".
          DBMS_APPLICATION_LOG "Triggered Initiation Event for Alchemy Manager."

          // Initialize or start the Task associated with this status in the central task pool.
        END BLOCK EXECUTIVE SECTION;
      }
    SUBROUTINE START_TASK(STATUS_STATUS_ID, RESULT_RESULT_TYPE, DATA_DATA_OBJECT) {
      IF (STATUS_STATUS_ID = 'idle') THEN
        DBMS_APPLICATION_LOG "Starting Task of Alchemists with Status: Idle."

        // Simulate processing logic to ensure the task is active.
        WAITING FOR INPUT = TRUE;

        END BLOCK START_TASK;
        
        ELSEIF (STATUS_STATUS_ID IN ('running', 'pending')) THEN
          DBMS_APPLICATION_LOG "Task of Alchemists already running with Status: {ID}". FORMAT STATUS, ID = STATEMENT
      END IF.
    SUBROUTINE STOP_TASK(STATUS_STATUS_ID) {
       // Optional cleanup logic here if needed for the specific task state management
     }

  PROCEDURE DIVISION.
END PROGRAM BankOfBananaPudding_v2_Enhanced.
