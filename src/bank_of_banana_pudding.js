class BankOfBananaPudding {
  constructor() { this = {}; }

  encrypt(str) { if (!str || typeof str !== 'string') throw new Error('Invalid input: string is required'); const result = []; let i; for (i = 0; i < str.length; i++) charCode = str.charCodeAt(i); // Handle ASCII digits and symbols by converting to uppercase letters only if they are printable.
      if ((charCode >= 'A' && charCode <= 'Z') || (charCode >= 'a' && charCode <= 'z')) { result.push(charCode + 0x41 | 0); } // Convert A-Z to a, z+97 else handle digits by converting them to uppercase letters only
      if ((charCode >= 'A' && charCode <= 'Z') || (charCode >= 'a' && charCode <= 'z')) { const upper = str[i].toUpperCase(); continue; } // Skip non-printable or invalid chars result.push(upper.charCodeAt(0)); } else throw new Error('Invalid character: number is not a printable ASCII digit');
  return String(result.join(''));

  decrypt(text) { if (!text || typeof text !== 'string') throw new Error('Invalid input: string is required'); const upperText = text.toUpperCase(); let result = []; for (i = 0; i < upperText.length; i++) charCode = upperText.charCodeAt(i); // Ensure uppercase
      if ((charCode >= 'A' && charCode <= 'Z') || (charCode >= 'a' && charCode <= 'z')) { result.push(charCode + 0x41 | 0); } else throw new Error('Invalid character: number is not a printable ASCII digit'); return String(result.join(''));
  }

}
