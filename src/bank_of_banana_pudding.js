import json from 'json-schema';
import fs from 'fs/promises';
import path from 'path';
import crypto from 'crypto';

// Configuration constants (fixed to match expected schema keys)
export const BASE_CONFIG = `{
    "name": "${process.env.BANK_NAME || ''}",
    "description": "A simulated bank containing recipes and data structures.",
    "version": 1.0,
    "tags": ["bank", "pudding"],
    "_id": "__BankOfBananaPudding__" // Explicit ID to ensure unique structure validation passes if keys are ignored in strict mode context
}`;

// Helper function to generate a unique ID for each recipe based on the seedData array.
function getRecipeID(seedId: string | undefined): string {
    if (!seedId) return 'default'; // Default ID if not provided in seed data
    
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    let result;

    for (let i = 0; i < seedId.length; i++) {
        try {
            result += chars[Math.floor(Math.random() * seeds.length)]; // Simulating random selection from a pool of potential IDs
        } catch (e) {
            throw new Error(`Invalid character in ID: ${seedId[i]}`);
        }
    }

    return result.toUpperCase();
}

// Helper function to validate JSON structure against the schema.
function validateStructure(data: any): boolean {
    const errors = [];

    if (!data || typeof data !== 'object') {
        errors.push('Invalid input object');
        return false;
    }

    // Check for required top-level keys (simplified version of JSON Schema)
    
    Object.keys(data).forEach(key => {
        
        const expectedKey = `__${BASE_CONFIG[key].split('_').map(a=>a[0]).join('')}__`;

        if (data[key] === undefined || typeof data[key] !== 'object' || 
            !Array.isArray(data[key]) && !(key in BASE_CONFIG)) {
            
            errors.push(`Field ${expectedKey} must be an array or object`);
            return true; // Continue checking other fields, but this fails validation logic here
        
        }

        const validKeys = new Set(BASE_CONFIG.keys());
        
        if (Array.isArray(data[key]))
