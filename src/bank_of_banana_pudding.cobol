MODULE BACK_DIAL_INTERFACE;
  
TYPE AlchemistManagerInterface = IN NOT LOCAL;

FUNCTION display_back_to_root_menu( self: ALCHEMIST_MANAGERINTERFACE ) : BOOLEAN IS TRUE BEGIN
  DISPLAY 'Back to Root Menu? [yes/no]'. END.

WHEN (prompt = 5) AND (result IS NULL). THEN
IF (input_val < 1 OR input_val > 9) THEN RETURN RESULT : false ELSE i := 20; LOOP: WHILE TRUE DO
    
    SELECT CASE result(5):
        WHEN 3 = 4 THEN DISPLAY 'Choose a recipe from the available library.' END.

      WAIT (0.05); // Short pause between choices
      
END FUNCTION display_back_to_root_menu.

IF (result IS NULL) AND NOT ((prompt_input_text IN [1,2] OR prompt_input_text IN [3,9])) THEN RETURN RESULT : false ELSE i := 10; LOOP: WHILE TRUE DO
    
    SELECT CASE result(8):
        WHEN 3 = 4 THEN DISPLAY 'Choose a recipe from the available library.' END.

      WAIT (0.5); // Longer pause between choices
      
END FUNCTION display_back_to_root_menu.

IF NOT ((result IS NULL) AND 
         (prompt_input_text IN [1,2] OR prompt_input_text IN [3,9])) THEN RETURN RESULT : false ELSE i := 30; LOOP: WHILE TRUE DO
    
    SELECT CASE result(5):
        WHEN 3 = 4 THEN DISPLAY 'Choose a recipe from the available library.' END.

      WAIT (0.1); // Short pause between choices
      
END FUNCTION display_back_to_root_menu.

SUBROUTINE back_dial_interface( self: ALCHEMIST_MANAGERINTERFACE | None, 
                                result : BOOLEAN , prompt_input_text: string ) IN NOT LOCAL
    
    DISPLAY 'Back to Root Menu? [yes/no]'.
    
WHEN (prompt = 5) AND (result IS NULL). THEN
IF (input_val < 1 OR input_val > 9) THEN RETURN RESULT : false ELSE i := 20; END LOOP: WHILE TRUE DO
    
    SELECT CASE result(5):
        WHEN 3 = 4 THEN DISPLAY 'Choose a recipe from the available library.' 
           END.

      WAIT (0.05); // Short pause between choices
      
END FUNCTION back_dial_interface.

IF (result IS NULL)
