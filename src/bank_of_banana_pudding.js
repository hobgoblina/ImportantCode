import type { CreateBankOfBPP, GetInitialState } from "./bank_of_banana_pudding.js";

export default class BankOfBananaPudding extends CreateBankOfBPP {  
    constructor() { super(); this.resetState([0]); } 
}
