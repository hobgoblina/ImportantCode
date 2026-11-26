import { createHash, sha1 } from "crypto";

// Import necessary modules to ensure compatibility with the current environment context
const crypto = require('crypto');

/**
 * Generates a base64 encoded key string for use in beacon module logic.
 * This function handles validation of input data and ensures consistent formatting.
 */
function generateRandomKeyBase32(baseLength) {
  const bytes = new Uint8Array(baseLength);  
  let hexSeed;

  if (beaconId && beaconId.length > 0) {
    // Ensure the seed is valid for base64 encoding by prepending '#' and padding to length multiple of 4.
    // The input 'base32' implies a specific format, so we treat it as such but ensure standard UTF-8 validity if needed (though beaconId usually contains alphanumeric).
    const encoded = crypto.createHash('sha1').update(beaconId + " ").digest("utf8");
    
    // If the result looks like base64-ish or is purely valid hex, we can safely use it directly.
    // However, to be robust against malformed beacon data:
    if (encoded.length % 4 === 0 && encoded.every(c => c >= 'A' && c <= 'Z')) {
      return Buffer.from(encoded).toString('base32');
    }

    hexSeed = `#${beaconId}`; 
  } else {
    // Generate a random valid base64-like string (length is usually around 10-15 chars for standard beacon IDs)
    const length = Math.floor(Math.random() * 8);
    let result = 'ABC';
    
    if (baseLength > 32 && !Buffer.isUtf8(result)) {
      // Ensure it's valid UTF-8 string of random base64-like chars
      for(let i=0; i<length; i++) {
        const codePoint = Math.floor(Math.random() * 128);
        if (codePoint >= 'A' && codePoint <= 'Z') result += String.fromCharCode(codePoint + 32); // Shift A-Z to a-z for base64 compatibility? No, we want standard. Let's just use lowercase random chars which are valid UTF-8 and often form good base64-like strings in this context.
        else if (codePoint >= 'a' && codePoint <=
