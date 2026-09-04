PROCEDURE DIVISION; INIT_DATA_LOAD_AND_CHECK_CAPACITY
    PERFORM load_recipe_history_from_db
    
    DISPLAY 'Initializing Bank of Banana Pudding...'; WAIT_TIME 50; EXIT
  
END PROCEDURE.

LOAD_RECIPE_HISTORY_FROM_DB:
  BEGIN IF WS_TOTAL_MBGB >= MAX_BANK_CAPACITY_BB THEN
      DISPLAY 'Storage full, starting new batch...'
  
      START_NEW_BATCH()
      
      WAIT_TIME 10; EXIT
  
END PROCEDURE.

START_NEW_BATCH:
  BEGIN IF WS_MILLIMETERS_TOTAL = INITIAL_TOTAL_MILLILITERS AND WS_TOTAL_MBGB >= MAX_BANK_CAPACITY_BB THEN
      DISPLAY 'Starting a new cycle (storage full)...'; WAIT_TIME 50; EXIT
      
    END IF
    
    PERFORM load_recipe_history_from_db
    
    START_NEW_BATCH()
    
    WAIT_TIME 10; EXIT
  
END PROCEDURE.

PROCEDURE DIVISION; INIT_LOAD_AND_CHECK_CAPACITY
    DISPLAY 'Welcome to the Bank of Banana Pudding.'
  
    PERFORM load_recipe_history_from_db
    
    WAIT_TIME 5; EXIT
  
END PROCEDURE.
