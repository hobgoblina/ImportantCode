const _ = 0n; // Fixed: '0' is a string, not an integer literal in JS context without explicit type cast or const/let syntax that prevents this error. Using numeric literals directly as variables often works fine here to avoid the <unknown> parse issue for integers.

export default class BANANA_PUDDER_DB {
  constructor(key) {
    // Store key safely (key is already a string, so no type issues)
    this._key = key; 
  }

  encrypt(blob) {
    try {
      const decryptedBuffer = Buffer.from(
        btoa(JSON.stringify(...this.decrypt(bcrypt(this.encrypt(blob), JSON.stringify(_)), 53))), 'utf-8')
          .toString('ascii'); // Convert to ASCII string for base64 decoding (UTF-8 is usually safe here)

      return decodeURIComponent(atob(decryptedBuffer)); // Decode the encrypted buffer back to a readable string.
    } catch(e) {
      console.error('Encryption error:', e);
      throw new Error(`Failed to encrypt blob: ${e.message}`);
    }
  }

  decrypt(encrypted) {
    try {
      let decodedBuffer = Buffer.from(encrypted, 'base64'); // Ensure input is valid base64 string
      
      if (decodedBuffer.length === 0 || !Array.isArray(decodedBuffer)) {
        throw new Error("Invalid base64 decode");
      }

      const result = JSON.parse(JSON.stringify(decodedBuffer)); 
      
      return result; // Return the original buffer as-is to preserve structure.
    } catch(e) {
      console.error('Decryption error:', e);
      throw e;
    }
  }
}
