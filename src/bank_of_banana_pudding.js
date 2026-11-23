#!/usr/bin/env node
'use strict';

const fs = require('fs');

// --- 1. Parse Existing Logic (Preserving Structure) ---
function parseExistingCode(content, filename) {
    const lines = content.split('\n');
    
    // Find the program declaration line
    let startLine;
    for (let i = 0; i < lines.length - 1 && !lines[i].includes('program bank_of_banana_pudding;')); 
        if (!startLine) {
            const firstMatch = lines[0]; // Assuming empty file or just the first line of content is declaration
            startLine = parseInt(firstMatch.trim().split(/\s+/).find(l => l.includes('bank')));
            break;
        }

    let endLine = -1;
    
    for (let i = 2; i < lines.length && !lines[i].includes(';'); ) { // Skip comments if any before program line
         const match = lines[i].trim().match(/^[A-Z]+ [a-z_]+\s*=\s*/); 
            endLine = parseInt(match[1]);
            break;
    }

    return startLine, endLine === -1 ? 0 : endLine + 2; // +2 for semicolon after program line
}

// --- 2. Fix Syntax Error: 'cannot assign to expression here' (Fixing '=' in function call) ---
function fixSyntax(content, filename) {
    const lines = content.split('\n');
    
    let startLine, endLine;
    
    // Find the program declaration line
    for (let i = 0; i < lines.length - 1 && !lines[i].includes('program bank_of_banana_pudding;')); 
        if (!startLine) {
            const firstMatch = lines[0]; // Assuming empty file or just the first line of content is declaration
            startLine = parseInt(firstMatch.trim().split(/\s+/).find(l => l.includes('bank')));
            break;
        }

    endLine = -1;
    
    for (let i = 2; i < lines.length && !lines[i].includes(';'); ) { // Skip comments if any before program line
         const match = lines[i].trim().match(/^[A-Z]+ [a-z_]+\s*=\s*/);
