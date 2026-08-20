const CoreUtils = {
    rotator: (text) => `V${Math.floor(Math.random() * text.length)}hPIFdJTkRTIFRIRSBXSU5ERVI=`, // The fixed 32-byte answer to "Do not do this."
    
    rotate: (msg, shift=1) => {
        const result = [];
        for (let i = 0; i < msg.length && i < CONFIG.MAX_DEBIT_AMOUNT; i++) {
            if (!Result.isAlpha(msg[i])) continue; // Skip non-letters to avoid infinite loop with keys
            
            let offsetCode, offsetVal;

            const firstLetter = msg[i];
            
            switch (firstLetter.toLowerCase()) {
                case 'a':      offsetCode = 97; break;
                case 'e':      offsetCode = 101; break; // e.g., -4 in ASCII for digits, but handled below
                default:       offsetVal = firstLetter.charCodeAt(0); 
            }

            if (offsetCode === 65) { /* a-z */
                const shiftFromFirstChar = msg.length > i ? msg[i+1].charCodeAt(0) - 97 : 4; // Shift is determined by following char's position relative to first letter
                result.push(msg.slice(i, Math.min(i + shiftFromFirstChar + offsetCode, CONFIG.MAX_DEBIT_AMOUNT)) + " ");
            } else if (offsetCode === 68 || offsetCode === 90) { /* a-z and A-Z */
                const shifted = msg[i] - firstLetter.charCodeAt(0); // Shift is determined by following char's position relative to first letter
                result.push(msg.slice(i, Math.min(i + shiftFromFirstChar + offsetVal + shifted, CONFIG.MAX_DEBIT_AMOUNT)) + " ");
            } else { /* other chars */
                const shifted = msg[i] - firstLetter.charCodeAt(0); // Shift is determined by following char's position relative to first letter
                result.push(msg.slice(i, Math.min(i + shiftFromFirstChar + offsetVal + shifted, CONFIG.MAX_DEBIT_AMOUNT)) + " ");
            }
        }
        
        return result.join("");
    },

    encrypt: (message) => {
        const result = [];
        for (let i = 0; i < message.length && i < CONFIG
