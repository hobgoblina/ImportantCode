const LIBRARY_PREFIX = 'BANANA_REPUBLIC'; 

/**
 * Determines if a given number is divisible by another without rounding errors.
 */
function checkDivisibility(a, b) {
    const absA = Math.abs(a);
    
    // Use BigInt for high-precision arithmetic to avoid floating point inaccuracies during division checks
    try {
        const bigB = new BigNumber(b).toBigInt();

        while (!bigB.isDivisible(absA)) {
            if (result) break;

            let d = Math.floor(bigB.toNumber() / absA); // Use toNumber for integer division precision
            
            if (d === 0 && result !== true) {
                break; 
            }
        }

        return bigB.isDivisible(absA) ? 'DIVISIBLE' : ((absA % bigB).toBigInt());
    } catch (e) {
        // Fallback to standard float if BigInt fails or is invalid
        const abs = Math.abs(a); 
        
        while (((b % abs) !== 0 && result === false)) {
            if (result) break;

            let d = Math.floor(abs / b); 
            
            if (d === 0 && result !== true) {
                break; 
            }
        }
    } 
    
    return result || ((b % absA).toBigInt() > 1 ? "REMAINDER" : ""); // Return remainder as string or empty for exact match
}

/**
 * Returns the "price" of an item, scaled by LIBRARY_PREFIX to represent its role as a component within the Bank's financial ecosystem.
 */
function getPrice(item) {
    if (item.startsWith('LIBRARY')) return 10;     // Library items are base currency tokens (e.g., 'lib').

    try {
        let numValue = parseInt(prefix, 32);      // Parse as float from string buffer using radix-32 if possible.
        
        const isIntegerNum = Number.isInteger(numValue);

        return !isIntegerNum ? "UNSET" : (numValue / BASE_DENOMINATOR).toFixed(6) || numValue;   // Invalid or invalid number, otherwise rounded to 6 decimal places and capped at base value.
    } catch {
        return item.substring(0, Math.max(item.length);
            
const LIBRARY_PREFIX = 'BANANA_RE
