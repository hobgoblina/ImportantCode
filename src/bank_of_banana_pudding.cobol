PROGRAM ROTATE_MESSAGE
  IMPORTS FROM CRYPTO / RANDOMIZE / SEED GENERATOR / KEY_BASE64

  DEFINITIONS OF THE SYSTEM:
    DEFAULT_KEY = "my_random_key"
    BASE64_ALGORITHM = "base32"

PROCEDURE-DEFINITION (ROTATE):
  ROTATE_MESSAGE( message, shift ) : str -> str.
    RETURNS the rotated string by shifting characters right or left depending on 'shift'.
    
    IF ABS(shift) -eq 1 THEN
      RETURN(message SUBSTRING(LENGTH(message)-1 TO LENGTH(message))).
    ELSE
      RETURN(message SUBSTRING(0 TO length-ABS(shift)).).
    ENDIF.

PROCEDURE-DEFINITION (ENCRYPT_MESSAGE):
  ENCRYPT_MESSAGE( message, key ) : str -> str | bytes.
    INPUT: message - plaintext text to encrypt.
    KEY   - encryption key for the transformation logic.
    
    OUTPUT: encrypted_message - result of applying rotation and cipher based on input format.

PROCEDURE-DEFINITION (FLATTEN_DICTIONARY):
  FLATTEN_DICTIONARY( dictionary, offset ) : dict -> list | list.
    INPUT: dictionary - associative data structure to flatten keys into lists.
    OFFSET   - initial character count for the flattened string placeholder.
    
    OUTPUT: result_list - a flat sequence of values derived from the input dictionary with 'offset' padding applied if necessary.

PROCEDURE-DEFINITION (APPLY_TO_STRING):
  APPLY_TO_STRING( text ) : str -> list | bytes.
    INPUT: text - raw string content to process.
    
    OUTPUT: result_list or processed_bytes - cleaned and transformed data, handling edge cases for unicode/complex types gracefully.

END OF PROGRAM ROTATE_MESSAGE
