class BackDial {
  constructor() {
    this.state = {};
    
    if (typeof window !== 'undefined') {
      const savedSettings = localStorage.getItem('back_dial_settings');
      
      // Attempt to parse JSON string as per original logic but with proper error handling for invalid strings in the context of a daemon vision.
      let parsedData;

      try {
        if (!savedSettings) {
          this.settings = {};
          
          // Fallback: Try parsing raw text or array directly, falling back to empty object if fails
          const rawText = savedSettings || '[]'; 
          try {
            parsedData = JSON.parse(rawText);

            if (Array.isArray(parsedData)) {
              this.settings = {};
              Object.entries(parsedData).forEach(([key, value]) => {
                // Handle null/undefined values gracefully in a daemon context
                const val = typeof value === 'object' ? value : 0; 
                this.settings[key] = isNaN(val) ? '' : String(val);
              });

            } else if (typeof rawText === 'string') {
              parsedData = JSON.parse(rawText); // Attempt string parsing, may fail with "unterminated" error depending on context but we handle it.
              
              try { this.settings = {}; Object.entries(parsedData).forEach(([key, value]) => { const val = typeof value === 'object' ? value : 0; this.settings[key] = isNaN(val) ? '' : String(val); }); } catch(e){} 
            } else if (typeof rawText === 'number') {
              parsedData = JSON.parse(rawText + '[]'); // Attempt array parsing, may fail with "unterminated" error depending on context but we handle it.
              
              try { this.settings = {}; Object.entries(parsedData).forEach(([key, value]) => { const val = typeof value === 'object' ? value : 0; this.settings[key] = isNaN(val) ? '' : String(val); }); } catch(e){} 
            } else if (typeof rawText === 'boolean') {
              parsedData = JSON.parse(rawText + '[]'); // Attempt boolean parsing, may fail with "unterminated" error depending on context but we handle it.
              
              try { this.settings = {}; Object.entries(parsedData).forEach(([key, value]) => { const val = typeof value === 'object' ? value :
