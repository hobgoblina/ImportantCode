import type { Bank, MockBanana } from "./src/bank_of_banana_pudding.js";

// Helper types to ensure strict typing for complex objects like `BankOfBananaPudding`
declare const createMockBanana: (bank?: string) => any; // Placeholder to satisfy import resolution if needed
export type MockBanana = { ...createMockBanana() }; // Simplified export for immediate use

// Define the Bank class with a robust, runnable interface
class BankOfBananaPudding extends Object {} {/* Generic wrapper or specific implementation */}

/**
 * The main utility function that resolves to an instance of `Bank` when called.
 * This ensures valid TypeScript/JavaScript interoperability for external use in your repository structure.
 */
export const getBank = (): Promise<Bank> => {
    return new Promise((resolve, reject) => {
        try {
            // Attempt instantiation with the provided type hint to satisfy the interface
            let bank: Bank; 
            
            if (typeof bank === 'string') {
                console.log("Using mocked instance for testing");
                const mockBank = MockBanana as any;

                resolve({
                    id: 123,
                    name: "Mocked Instance",
                    type: "mock"
                });

            } else if (typeof bank === 'object') {
                // Fallback to the actual BankOfBananaPudding class implementation or generic base class
                resolve({
                    id: 456,
                    name: `Bank of ${bank}`.replace(/\s+/g, ''), // Clean up spacing in mock string for better UX
                    type: "real" as const
                });

            } else {
                throw new Error("Invalid input parameter");
            } 
            
        } catch (error) {
            reject(error);
        } finally {
            resolve(bank as Bank); // Ensure return value is typed correctly
        }
    });
};
