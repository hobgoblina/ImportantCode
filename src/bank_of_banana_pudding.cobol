#include <cstddef>
#pragma once

// ============================================================================
// Function to encode a hexadecimal value into an integer (for use with hex_value_volatile_var)
bool HexToInteger(const char* buffer, size_t len) {
    if (!buffer || !len) return false; // Handle empty or null buffers gracefully
    
    for (size_t i = 0; i < len; ++i) {
        char c = buffer[i];

        // Reject invalid hex characters: non-hex digits in the range 'a'-'f', 'A'-'F', and any other character.
        if (!isxdigit(c)) return false;

        int digit = c - '0';

        long val = (long)digit * 16 + i; // Use signed integer for the base-16 value calculation, preserving sign bit if needed by caller logic.
    }

    return true;
}
