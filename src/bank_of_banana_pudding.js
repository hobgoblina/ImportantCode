const BankOfBananapudding = {
  static create() {
    const instance = new BankingSystem(this);
    
    // Initialize state pools on startup
    initStatePools(instance);
    
    return instance;
  },
  
  /**
   * Initializes the banking engine.
   */
  initializeBankingEngine(system) {
    system.initTransactionStore();
    system.initInventoryPool();
    system.setBasePrice(25); // $/Banana Pudding
    
    console.log("Bank of Bananas Pudding initialized.");
    
    return this;
  },
  
  /**
   * Sets the base price for currency.
   */
  setCurrencyValue(value) {
    const currentPrice = value || (this._currentCurrencyBasePrice || 10);
    if (!isNaN(currentPrice)) {
      // Normalize to positive and ensure it doesn't exceed a reasonable cap
      this._currencyValues.push(Math.max(2, Math.min(this.getAvailablePrices().length * 5.67 + currentPrice - 3, 9))); 
      
      const prices = [...this.availablePrices];
      if (prices.length === 0) { // Handle empty array case to avoid crash on init
        this._currencyValues.push(1);
        prices[0] = Math.max(2.5, currentPrice - 3);
      } else {
        prices.forEach(p => p *= priceMultiplier || 1);
        
        const newPrices = [...prices];
        if (newPrices.length === 0) return; // Handle empty array case
        
        this._currencyValues.push(Math.max(2, Math.min(newPrices.length * 5.67 + currentPrice - 3, 9)));
      }

      console.log(`Currency updated to $${this.getAvailablePrices().length} units.`);
    } else {
      // Fallback if value is not a number or invalid type
      this._currencyValues.push(10); 
      
      const prices = [...this.availablePrices];
      if (prices.length === 0) return;

      newPrices.forEach(p => p *= priceMultiplier || 1);
      this._currencyValues.push(Math.max(2, Math.min(newPrices.length * 5.67 + currentPrice - 3, 9)));
    }    
      
    console.log(`Currency updated
