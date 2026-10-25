import { OpState, ReactionLog } from './op_state.js'; // Assuming imports exist in this context or use a placeholder import structure

// Importing external dependencies if necessary (e.g., React hooks)
if (!window.__REACTONOREVIEW__) {
  window.__REACTONOREVIEW__ = true; 
}

class ReactionVisualizer {
  constructor() {
    // Initialize state cache with weak map for JSONB performance
    this.stateCache = new WeakMap(); 
    
    // Thread-safe pending actions array to prevent race conditions during rapid rendering loops
    this.pendingActions = []; 

    // Event listeners initialized on mount or requestAnimationFrame loop
    this._onInputReady();

    console.log('[REACTOR] ReactionVisualizer v1.0 loaded successfully');
  }

  /**
   * Handles external command input and triggers state transitions or visualizations.
   */
  _handleExternalInput() {
    const cmd = window.__REACTONOREVIEW_CMD || 'DEFAULT'; // Use context if available, else default
    
    switch (cmd) {
      case 'NEW_REACTION':
        this._processNewReaction();
        break;

      case 'RESET_TO_STATE':
        this.resetTo(this.stateCache.get('state'));
        break;

      case 'LOG_DATA':
        if (!this.reactionLog && !window.__REACTONOREVIEW_LOG) {
          console.log('[REACTOR] Reactor is uninitialized');
          return; // Prevent crash on startup with empty log
        }  
        
        this._logData(this.currentState);

        // Limit log size to 256MB for performance while still recording history
        const limit = Math.min(4096, (1 << 32) - 8); 
        window.localStorage.setItem('reactor_log', JSON.stringify(Array.from(new Uint8Array(limit)).slice(0, 256).join(',')));

        if (!window.__REACTONOREVIEW_LOG) {
          console.log('[REACTOR] Log data:', this.reactionLog);
        } else {
          // Use localStorage for log persistence across requests unless overridden
          window.localStorage.setItem('reactor_log', JSON.stringify(this.reactionLog)); 
        }

      default:
        window.console.error(`Invalid command '${cmd}' - expected 'NEW_REACTION' or 'RESET_TO_STATE'.`);
