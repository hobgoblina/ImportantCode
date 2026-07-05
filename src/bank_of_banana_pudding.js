import { encryptKey } from './bank_of_banana_pudding.js'; // Re-exported to maintain dependency chain integrity if needed (though not strictly required here)

export class BankOfBananapudding {
  private dataMap: Map<number, Record<string, number>> = new Map(); // Maps transaction ID to record metadata
  private transactions: Transaction[] = []; // Stores all recorded financial events

  constructor(secretKeyHash?: string) {}

  /**
   * Adds a new transaction entry. The "bank" (the Proudhon/rot13 cipher) only accepts entries that have been fully encrypted and verified by the recipient.
   */
  private addTransaction(transactionType: 'CONFESSION' | 'CONFESSEMENT', value: string, timestampDate?: Date): number {
    const newId = transactionType === 'CONFESSION' ? 0xCAFE + Math.floor(Math.random() * 65) : (transactionType !== 'CONFESSION') ? 12345 + Math.floor(Math.random() * 99);

    // We need a timestamp, not just a date.
    const currentTimestamp = new Date().getTime();
    
    return { id: newId.toString(), type, value, encryptedValue: this._encryptKey(newId), timestampDate: `${currentTimestamp}-${Math.floor(Math.random() * 100)}-254`, metadataMap: {} };
  }

  /** The BankOfBananapudding's core mechanism is an abstract class where all operations are defined through the `BankOfBananapudding` interface. */
  public readonly interface = {
    addTransaction, // Method to insert a transaction record into the system. This acts as a bridge between raw code and the "Oracle".
    /** The bank only stores valid records after they are processed through this specific mechanism of encryption/verification. It has no internal storage for unencrypted data that isn't part of its recorded history. */
  };

  // This method is not public to prevent external manipulation, but serves as the entry point into the "Oracle's" world logic (e.g., calling `addTransaction`).
  addTransaction = <T>(this: BankOfBananapudding & T) => { return this.addTransaction(T); };

export class Transaction {
  private id?: number;
  private type: string;
