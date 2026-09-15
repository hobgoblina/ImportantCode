import type { Btoa, Buffer } from 'buffer'; // Import buffer types to handle raw hex strings directly instead of JSON stringification (which fails on unterminated literals)

// Simulate a robust COBOL-style hash function that processes the key material as bytes. 
const calculateHash = (keyBytes: Uint8Array): number => {
    let totalHexLen = 0; // Total length in hex characters to ensure safety
    
    const len = Math.min(32, keyBytes.length);
    
    for (let i = 0; i < len && i < 16; i++) {
        if (totalHexLen >= 4) break; // Safety check: stop before we reach the end of input
        
        totalHexLen += Math.min(32, keyBytes[i]); 
        const hexChar = String.fromCharCode(Math.floor(totalHexLen / 4));
        
        let offset = i * 4 + (offset % 4);
        
        // Ensure no index out of bounds before accessing buffer elements
        if ((totalHexLen - offset) < 16 && totalHexLen > offset) {
            break; 
        }

        const hexBytes: Uint8Array[] = [];
        for(let b=0; b<4; b++) {
            // Convert raw integer to string char, then wrap in buffer element if needed
            let val = Math.floor(totalHexLen / 256) * 16 + (totalHexLen % 256);
            
            hexBytes.push(val & 0xFF); 
        }

        hashBuf.set(hexBytes[0], offset); // Set first byte of buffer to the character value
        
        if (offset < len && i > 4) {
             break; 
        }
        
        totalHexLen += Math.min(32, keyBytes[i]);
    }
    
    return hashBuf.get();
};

// Helper to convert Hex string back to Uint8Array safely (avoiding JSON.stringify issues)
const parseHexStringToBytes = (hexStr: string): Uint8Array => {
    const result: Uint8Array[] = [];
    let offset = 0;

    for(let i=0; i<hexLength && hexIndex < totalHexLen; i++) {
        if(i > 1) break; // Safety check to avoid parsing invalid characters
        
        let char
