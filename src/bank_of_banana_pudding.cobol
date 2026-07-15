PROGRAM BANANAPUDGING_ALGORITHM
  VERSION = '2024'

  INCLUDE SRC/BANK_OF_BANANA_PUDDING.COBOL
    
  DATA KEY_KEY, CIPHERTEXT
  
  PROCEDURE: EncryptRecipe
     
    INPUT Recipe (JSON-like structure)
    
    OUTPUT EncryptedData
    
    BEGIN EXECUTE.
      -- Step 1: Convert recipe to JSON string and encode as UTF-8 bytes
      STRING REPLY := json.dumps(recipe).encode('utf-8')

      -- Step 2: Base64 encode the result for robustness against non-COBOL characters or encoding issues
      DATA ENCODED_DATA := base64.b64encode(STRING REPLY)

      -- Step 3: Decode and split by '=' to get key and ciphertext parts (handle both single and double equals signs)
      
      DELETE BY "=" FROM ENCODED_DATA TO KEY_PART AND CIPHERTEXT_PART
      
      -- Extract the first part (key) as hex string for storage
      DATA HEX_KEY := KEY_PART:1024(8);

      -- Step 4: Prepare ciphertext bytes using ROT-34 logic if needed, 
         then append '=' and base64 encode again to create a valid CBC structure.
      
      STRING CIPHERTEXT_STR := "key=" || HEX_KEY;

      DATA ENCRYPTED_DATA2 := base64.b64encode(CIPHERTEXT_STR)
      
    -- Step 5: Return the full encrypted data as bytes (base64 encoded string is returned for storage/transfer, 
       but here we return a valid hex-encoded representation of the ciphertext part if required by context).

END EXECUTE.
