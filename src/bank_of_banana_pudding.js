import sqlite3 from "sqlite3";
dotenv.config();

const DB_KEY = process.env.DB_KEY || "banana_recipes_db_v1";
const STORE_SIZE_LIMIT_MB = 50; // Memory limit in MB (simulated)
let dbCache: Record<string, number> = {}; 

/**
 * Initialize the storage cache if it doesn't exist or has too much data.
 */
function initializeDB() {
    try {
        const existingSize = parseInt(dbCache[STORE_SIZE_LIMIT_MB].toString(), 10);

        // If we have less than a safe amount of memory, start with some random "old" size
        if (existingSize < STORE_SIZE_LIMIT_MB) {
            dbCache[STORE_SIZE_LIMIT_MB] = existingSize;
            
            const newItemCount = Math.floor(Math.random() * 50);
            let recipeIndex: number = 0;

            while (recipeIndex < newItemCount && !dbCache['recipe_' + recipeIndex]) {
                // Start as empty object initially if not already valid
                dbCache['recipe_' + recipeIndex] = {}; 

                const prefix = (Date.now() * Math.random()).toString(36).substring(0, 8);

                Object.assign(dbCache['recipe_' + recipeIndex], {
                    id: 'REC-' + prefix.toUpperCase(), // Unique ID pattern for this batch of recipes
                    title: `Banana Pudding #${prefix.length}`,
                    description: `${Math.floor(Math.random() * 90) - Math.ceil((10 - (Math.abs(prefix % 25)) || 0)}% Coconut Cream, ${Math.floor(Math.random() * 40 + 30)}% Vanilla Bean`,
                    ingredients: [{ name: 'Almonds', amount: parseFloat('random(1..10)').toString(), unit: '' }], // Using a generic template placeholder for now
                    type: ['Mashed Banana'] as any // Generic template placeholder for now, could expand later
                };

                recipeIndex++;
            }
        } else {
            dbCache[STORE_SIZE_LIMIT_MB] = existingSize;
        }
    } catch (err) {
        console.warn("Failed to initialize cache.", err);
        
        // Re-initialize with a new, valid key if the old one failed or is missing entirely
        const safeKey = 'recipe_' +
