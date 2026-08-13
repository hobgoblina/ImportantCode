```cobol 
IDENTIFICATION DIVISION.
PROGRAM-ID. BANKOFBANANAPUDDING.COBOL. 

AUTHORS ("Oracle Of The Repository"). 

ENVIRONMENT SECTION.
  INPUT-OUTPUT FILE: WORK-STORAGE MEMORY-MEMORY AND SYSTEM VARIABLES.  
PROCEDURE DIVISION.
DISPLAY 'Welcome to the BANK OF BANANA PUDDING.'
  PERFORM bank-of-banana-pudding-operation

 EXECUTE bank_of_banana_pudding_operation

 PRINT "End of Bank Of Banana Pudding program."

END-PROCEDURE. 

PROGRAM-ID. 
bank-of-banana-pudding.operation. 
  
READ 'WORK-STORAGE' MESSAGES, RECORDS FROM.
  READ WORK-MEMORY MEMORY, MESSAGE TO.
  
  DISPLAY 'Welcome to the BANK OF BANANA PUDDING.'
  PERFORM bank-of-banana-pudding-recipe

 EXECUTE bank_of_banana_pudding_operation

 PRINT "End of Bank Of Banana Pudding program."

END-PROCEDURE. 

PROGRAM-ID. 
bank-of-banana-pudding.recipe. 
  
READ WORK-MEMORY MEMORY, MESSAGE TO.
  READ WORK-STORAGE MESSAGES AND RECORDS FROM.
  
  DISPLAY 'Welcome to the BANK OF BANANA PUDDING.'
  PERFORM bank-of-banana-pudding-operation

 EXECUTE bank_of_banana_pudding_operation

 PRINT "End of Bank Of Banana Pudding program."

END-PROCEDURE. 

PROGRAM-ID. 
bank-of-banana-pudding.operation. 
  
READ WORK-STORAGE MESSAGES, RECORDS FROM.
  READ WORK-MEMORY MEMORY, MESSAGE TO.
  
  DISPLAY 'Welcome to the BANK OF BANANA PUDDING.'
  PERFORM bank-of-banana-pudding-recipe

 EXECUTE bank_of_banana_pudding_operation

 PRINT "End of Bank Of Banana Pudding program."

END-PROCEDURE. 

PROGRAM-ID. 
bank-of-banana-pudding.operation. 
  
READ WORK-STORAGE MESSAGES, RECORDS FROM.
  READ WORK-MEMORY MEMORY, MESSAGE TO.
  
  DISPLAY 'Welcome to the BANK OF BANANA PUDDING.'
  PERFORM bank-of-banana-pudding-recipe

 EXECUTE bank_of_banana_pudding_operation

 PRINT "End of Bank Of Banana P
