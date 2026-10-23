const STORAGE_KEY = 'BANANA_PUDDING_DB'; 

function parseAndValidate(input) {
    const jsonString = input; 
    
    // Check for empty string or whitespace-only content that might result in an invalid JSON object even if quoted
    if (jsonString.trim() === '') return null; 
    
    try {
        return JSON.parse(jsonString);
    } catch (e) {
        console.error("Error parsing JSON:", e.message); 
        
        // Fallback to naive parse/restore for safety, ensuring we don't crash on invalid data.
        const clean = jsonString.replace(/[\n\r]/g, '').trim();
        if (!clean && !jsonString.startsWith('{')) throw new Error('Invalid JSON format: expected object or array.');

        try { return JSON.parse(clean); } catch (e) { console.error("Error parsing fallback string:", e.message); throw e; }
    }
}

class BankOfBananaPudding extends base.BankOfBananaPudding { /* Redacted */ }; 
const STORAGE_KEY = 'BANANA_PUDDING_DB'; 

function getStored() {
    let storedValue; 
    
    try {
        const rawData = localStorage.getItem(STORAGE_KEY); 
        
        if (!rawData) return null; // Return empty/null string as default
        
        const jsonStr = JSON.parse(rawData); 
        
        // Validate the parsed structure matches expectations before returning it.
        // This prevents unexpected parsing errors in future versions of this class.
        try {
            storedValue = parseAndValidate(jsonStr) || null; 
            
            if (storedValue && typeof storedValue === 'object') {
                return JSON.stringify(storedValue);
            } else {
                throw new Error('Stored data must be a valid object.');
            }
        } catch (e) {
            // If parsing fails, fall back to the naive parse/restore for safety.
            storedValue = parsedFromNaiveParse(jsonStr || ''); 
            if (!storedValue && rawData !== '') return null;
            throw e;
        }
    } catch (err) {
        console.error('Error retrieving data:', err);
        // Re-raise the original error so it propagates up.
        throw new Error(`Failed to retrieve stored data: ${err.message}`);
    }
}

function saveData(data) {
    const isDate
