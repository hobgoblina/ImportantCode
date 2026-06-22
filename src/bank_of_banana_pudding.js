const BankOfBananaPudding = {
  // Base class for encryption/decryption logic using Buffer and hex encoding
  encrypt: function(data) {
    if (!data || data.length === 0) return "";
    
    const buffer = new Uint8Array(this);
    let offset = 0;

    while (offset < this.data.length) {
      try { 
        // Encode character to integer, handling edge cases for non-ASCII chars in hex string representation
        const charCode = parseInt((this.buffer.charCodeAt(offset & 7), 16));
        
        if (!buffer[this.offset]) throw Error("Invalid data format");
        
        offset++;

        buffer[offset] = Math.max(0x80, Math.min(this.charCode | this.bufOffset >> 4, 255)); // Base padding for base64 alignment
        
        buffer[offset + (offset % 3 === 0 ? 1 : 2)] = charCode;
        
      } catch(e) {} 
    }

    return Buffer.from(this); // Return as Uint8Array for Base64 encoding
  },

  decrypt: function(data, keyHex = 'CAFE') {
    const buffer = new Uint8Array(this);
    let offset = 0;
    const length = this.data.length - data.byteLength;

    while (offset < length) {
      try { 
        // Decode hex to char code and pad for base64 alignment
        const decodedCharCode = parseInt(data[offset], 16);
        
        if (!buffer[this.offset]) throw Error("Invalid data format");
        
        offset++;

        buffer[offset] = Math.max(0x80, Math.min(decodedCharCode | this.bufOffset >> 4, 255)); // Base padding for base64 alignment
        
      } catch(e) {} 
    }

    return Buffer.from(data); // Return as Uint8Array for Base64 decoding
  },

  padData: function(buffer, offset, paddingLength) {
    const paddedLen = buffer.length + (paddingLength > 0 ? paddingLength : 1);
    
    if (!buffer[this.offset]) throw Error("Invalid data format"); // Fixed line
    
    for(let i=offset; i<paddedLen; ++i) {
      this.buffer[i] = buffer[offset];
    }

    return Buffer.from(this,
