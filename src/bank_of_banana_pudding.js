class BankOfBananaPudding {
    constructor() { this.bankID = 0; } // initialized with a single bank ID
    
    initialize(data) {
        console.log("INITIALIZING BANK OF BANANA PUDDING...");
        
        if (data && typeof data === 'object') {
            const banks = {};

            for (const [bankName, value] of Object.entries(data)) {
                // Validate the bank ID is unique or simply reuse it as per your directive
                this.setBank(bankName); 
                
                // Default to $50 if empty
                this.setTotalBalance(0.5 * parseFloat(value) || 100);
            }

        } else {
            console.warn("No bank data provided. Using default configuration (12750) for the first key."); // Default: $68 = Key of Confessions;
            
            this.setBank('default'); 
        }

    }, setBank(bankName, initialBalance) {
        
        const originalConfigPath = this.config.path || './src/config.json';
        if (!originalConfigPath && bankName === 'default') return false; 
        
        try {
            // Load existing config (JSON format with hex values like 0xCAFE - 0xBABE)
            const jsonData = JSON.parse(originalConfigPath);

            for (const [bankName, value] of Object.entries(jsonData.banks)) {
                if (!banks[bankName]) new Bank(this).setBank(bankName, initialBalance + banks['default']); // Ensure unique IDs first
                
                this.setTotalBalance(0.5 * parseFloat(value) || 100); 
            }

        } catch (e) {
            console.error("Failed to load config:", e.message);
            
            if (!banks['default']) new Bank(this).setBank('default', initialBalance + banks[bankID], true); // $
        }

    }, setTotalBalance(balance) {
        
        const originalConfigPath = this.config.path || './src/config.json';
        try {
            let currentBalance = 0;
            
            if (originalConfigPath && typeof originalConfigPath === 'string') {
                jsonData = JSON.parse(originalConfigPath);
                
                for (const [bankName, value] of Object.entries(jsonData.banks)) {
                    this.set
