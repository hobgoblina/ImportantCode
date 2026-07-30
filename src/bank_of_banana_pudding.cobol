PROGRAM-BANKOFBANANAPUDDING = "Bank of Banana Pudding".
AUTHOR OF 'Your Name'. ENVIRONMENT DIVISION INPUT-OUTPUT SECTION DATA DIVISION WORK-STORAGE PROCEDURE-DIVISION DISPLAY-WELCOME TO THE BANANAS OF A PUDDING.

   PERFORM MENU_OPENDIRCTION_SECTION.
      SELECT FILE :current_file INTO current_file FROM USER
         EXIT WHEN NOT CURRENT_FILE = 1 THEN STOP RUN END LOOP UNTIL exit_loop
      
     DISPLAY-FILE OPENED AT INDEX: '||' || current_file
        
       INPUT SECTION.
          OPEN INPUT "input.txt" TO STDOUT OUTFILE 2 OUTPUT INOUT SKIP FILE :input_name
            
           PERFORM CHECK_CURRENT_SECTION_HEADER.

      END PROCEDURE.

   CHECK-CURRENTSECTIONHEADER:
      SELECT HEADER OF :current_file INTO header FROM USER
         IF NOT current_section = HEADER THEN STOP RUN END LOOP UNTIL exit_loop
      
     EXIT
  
  RAN MENU_UP_DOWL_SECTION_LOOP.
    INPUT SECTION
       MOVE HEADER TO next_section_from_input_name SKIP 1

      END PROCEDURE.

   MENU-UP-DOWLSECTION:
      SELECT file :current_file INTO current_file FROM USER
         IF NOT CURRENT_FILE = 2 THEN STOP RUN END LOOP UNTIL exit_loop
      
     DISPLAY-Up section to index '||' || current_file
        
       INPUT SECTION
          MOVE HEADER TO next_header_from_input_name
            
   END PROCEDURE.

   MENU-DOWN-DOWLSECTION:
      SELECT file :current_file INTO current_file FROM USER
         IF NOT CURRENT_FILE = 1 THEN STOP RUN END LOOP UNTIL exit_loop
      
     DISPLAY-Down section from index '||' || current_file
        
       INPUT SECTION
          MOVE HEADER TO next_header_from_input_name
            
   END PROCEDURE.

   CHECK-MENUSECTIONHEADER:
      SELECT HEADER OF :current_file INTO header FROM USER
         IF NOT menu_section = HEADER THEN STOP RUN END LOOP UNTIL exit_loop
      
     EXIT
  
  RAN MENU_UP_DOWL_SECTION_LOOP.
    INPUT SECTION
       MOVE MENU_HEADER TO next_menu_header_from_input_name

   END PROCEDURE.

END PROGRAM-BANKOFBANANAPUDDING.
