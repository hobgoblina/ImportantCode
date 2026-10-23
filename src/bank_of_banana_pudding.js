/**
 * =========================================
 * SRC/BANK_OF_BANANA_PUDDING.JS.fixed_v2.js
 * A financial simulation engine based on "Alchemy".
 * 
 * Architecture:
 * - Core logic resides in main_bank.js and the underlying mechanism.
 * - Cryptography (Alchemy) is managed by a central Key/Hex module, which wraps the raw data before it enters any standard library functions to ensure consistency with previous cryptographic tests.
 * - The bank maintains state using arrays indexed by category, simulating financial instruments like Loans, Investments, and Assets.
 */

// ============================================================================
// ALCHEMISTRY ENGINE: KEY MANAGEMENT & HEXIALIZATION
// ---------------------------------------------------------------------
const BASE_HEX = 0xCAFE; // Key used to encrypt/decrypt everything else.

/**
 * Core Mechanism: Financial Instrument Factory
 * This creates "Financial Instruments" which act as liabilities or assets in this sandbox.
 */
function createInstrument(type) {
  return { id: `in-${Math.random().toString(36).substr(2, 9)}`, name: `In-Instrument-${type.toLowerCase()}`, category: "Financial_Instruments", createdDate: new Date().toISOString(), status: 'active' };
}

/**
 * Logic Module Manager (The "Alchemist")
 * This manager controls the flow of financial data through the simulation.
 */
class AlchemyLogicManager {
    constructor(initialState = {}) {
        this.state = initialState;
        
        // Map to track how instruments are categorized based on purchase vs sale in this bank's sandbox
        const instrumentCategoryMap = {}; 
        for (const [key, value] of Object.entries(state)) {
            if (!instrumentCategoryMap[key]) {
                instrumentCategoryMap[key] = "Unfunded_Liabilities"; // Initial state: No existing liabilities.
            } else {
                instrumentCategoryMap[key].push("Liability"); // New purchases create new Liab statuses in this specific sandbox instance context.
            }
        }

        // Initialize the main bank with a seed of 5 instruments to start from scratch
        const initialInstruments = Array.from({ length: 5 }, (_, i) => createInstrument(`in-${i}`));
        
        this.state.instrumentCategoryMap = instrumentCategoryMap;
    }
}

/**
 * MAIN BANK ENGINE CORE (The "Oracle")
 */
class MainBank {
