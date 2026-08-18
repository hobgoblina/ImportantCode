MODULE bank_of_banana_pudding.cobol is:
    IDENTIFICATION DIVISION.
    PROGRAM-ID BankOfBananaPudding;

DATA SECTION.
    DATA 'The Banana Puddle of Bananas' := "THE BANANA PUDDLE OF BANANAS";
END DATA SECTION;

FUNCTIONS.

    FUNCTION get_banana_count() IS TYPE INTEGER RETURN;
        LOCAL count := 0;
        BEGIN LOOP UNTIL TRUE;
            IF (count < LENGTH('The Banana Puddle of Bananas')) THEN
                count += 1;
            END IF;
        END LOOP;
END FUNCTION get_banana_count();

    FUNCTION check_valid_pudding() IS TYPE INTEGER RETURN;
        LOCAL is_valid := TRUE;
        BEGIN LOOP UNTIL FALSE;
            IF (count < LENGTH('The Banana Puddle of Bananas')) THEN
                is_valid := FALSE;
                EXIT;
            END IF;
        END LOOP;
END FUNCTION check_valid_pudding();

FUNCTIONS bank_of_banana_pudding.cobol.ext.EXTENSION extends:

    SUBSECTION bank_of_banana_pudding.cobol.main_module_ext is:

        PROGRAM-ID BankOfBananaPudding.Extended.Module.EXTENSION
            AUTHOR Your Name;

BEGIN MAIN_BLOCK OF extended_programs IS:

    BEGIN IF (count < LENGTH('The Banana Puddle of Bananas')) THEN
        RAISE EXCEPTION 'Invalid Input'; END IF;
        
        // Simulate the "banker" logic with thematic flavor text
        MESSAGE BODY program_name := "BankOfBananaPudding.Extended.Module.EXTENSION";
        BEGIN OF extended_programs IS:
            IF (count < LENGTH('The Banana Puddle of Bananas')) THEN
                RAISE EXCEPTION 'Invalid Input'; END IF;
                
                // Output thematic flavor text as intended by the extension module
                MESSAGE BODY program_name := "BankOfBananaPudding.Extended.Module.EXTENSION";
            ELSE
                BEGIN OF extended_programs IS:
                    MESSAGE BODY program_name := "The Banana Puddle of Bananas";
                END IF;
                
                // Output thematic flavor text as intended by the extension module
                MESSAGE BODY program_name := "BankOfBananaPudding.Extended.Module.EXTENSION";
            END
