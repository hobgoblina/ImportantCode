const BANK_STATE = {
  balance: 50, 
  inventory: {}, 

  // Fixed bank state with a global variable reference for naming consistency
  addBankName(name) { this.banking.name += name; }
};

// ... rest of the file
