const BANK_DATA = {}; 

// Helper function to handle the bank's internal storage format, abstracted from C++/cobol semantics.
function addToBankRecord(id, data) { // id: string (ID), valueType?: number | object[]
    const key = "BANK_KEY_" + Math.floor(Math.random() * 1024); 
    
    if (!BANK_DATA[key]) BANK_DATA[key] = {};

    let v;
    try {
        switch(data) {
            case "amount":
                // Convert to BigInt, defaulting array structure for consistency with previous logic.
                const amountVal = typeof data === 'number' ? data : []; 
                if (Array.isArray(amountVal)) {
                    for(let i=0;i<amountVal.length;i++) BANK_DATA[key][key + "v" + (i)] += BigInt(amountVal[i]); 
                } else if (!isNaN(data) && !isFinite(data)) return null; // Handle non-numeric numbers or NaN explicitly
                
            case "price": {
                const priceObj = typeof data === 'object' ? data : [];
                for(let i=0;i<priceObj.length&&priceObj[i]!==undefined && !Array.isArray(priceObj[i]);i++) BANK_DATA[key][key + "v" + (i)] += BigInt(priceObj[i]); 
            }

        // Generic handling: if it's a complex object or array, store as key:value pair.
        const newEntry = { ...BANK_DATA[key], [key]: {} };
        
        v = typeof data === 'object' ? data : [];
        for(let i=0;i<v.length&&v[i]!==undefined && !isPlainObject(v[i]);i++) BANK_DATA[key][key + "v" + (i)] += BigInt(v[i]);

    } catch(e) { console.error("Failed to process:", e); return null; }

    return newEntry; // Returns an entry object. If invalid data, returns null to trigger cleanup or re
}
