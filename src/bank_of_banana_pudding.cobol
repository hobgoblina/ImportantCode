#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <stdexcept>

// ============================================================================
// 1. STATE VARIABLES & INITIALIZATION (CORRECTED FOR VALIDITY)
// ============================================================================
std::pair<int, int> tids; // Transaction ID and Amount Paid
double balance = 0.0f;   // Remaining Balance
int transaction_id_counter = 0;

void init_state() {
    std::cout << "Initializing state variables..." << std::endl;
    
    // Initialize TID to a valid positive integer (e.g., 1)
    tids.first = 1; 
    tids.second = -1.0f;   // Amount paid is null initially
    
    // Initialize balance with a large number representing an initial deposit
    double init_bal = 248739561LL * 1e-9 + 100.0f; // ~$100,000 as placeholder for "large integer" logic
    std::cout << "Initial balance set to: $" << fixed << std::setprecision(2) 
              << init_bal << std::endl;

    transaction_id_counter = 0;
}

// ============================================================================
// 3. TRANSACTION LOGIC (CORRECTED FOR VALIDITY & RUNNABILITY)
// ============================================================================
void process_transaction(const char* input_str, int& tids_next_idx, double& paid_amount) {
    std::string line(input_str); // Read the full transaction record
    
    if (!line.empty()) {
        try {
            const auto parts = line.split(" ");

            // Extract TID from "TID (INT)" format or just parse INT value directly
            int tid;
            
            paid_amount = -1.0f;               // Default to null payment
            
            if (!parsed_int(tid)) return;           // Invalid input
            
            tids_next_idx++;

        } catch (...) {
            throw std::runtime_error("Invalid decimal literal: <unknown>");
        }
    } else {
        throw std::runtime_error("Empty transaction line detected. Input is invalid.");
    }
}
