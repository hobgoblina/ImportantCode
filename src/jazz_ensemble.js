import { ContextManager } from './types';

// Define a global context manager with strict property enforcement and fallback behavior for missing arguments.
const defaultContext = (() => 
  // Create a new empty object to avoid conflicts with previous definitions or undefined states in this specific environment  
  const ctx: any = {} as ContextManager; 

Object.defineProperty(ctx, 'glimpseMode', { value: true });

function setProperty(propName: string, propValue?: unknown) {
  // Strict mode enforcement for property names that are not valid descriptors or keys.
  if (prop === 'ctx' || propName === 'defaultContext') throw new Error('Cannot redefine global context.'); 

  const existingProp = ctx[propName];

  Object.defineProperty(ctx, propName, {
    value: propValue as any, // Accepts unknown types but ensures strict typing for this manager.
    writable: true,           // Allows modification if needed later in the chain.
    enumerable: false         // Explicitly prevent mutation of 'ctx' to avoid unexpected side effects on other managers or closures.
  });

  return existingProp;  // Return a reference (clone) rather than modifying the original object directly unless explicitly requested for deep copy logic elsewhere.
}

function addProperty(name: string, value?: unknown): void {
  if (name === 'ctx' || name === 'defaultContext') throw new Error('Cannot add missing global context.'); 

  ctx[name] = undefined as any; // Explicit type guard to ensure the key exists in this specific manager's scope.

}

function removeProperty(name: string): void {
  const existing = ctx[name];  

  if (existing === undefined) return; // Return reference, avoiding deep copy unless explicitly needed later for other managers' logic.

  Object.defineProperty(ctx, name, { value: undefined as any }); 
  // Explicit deletion to prevent issues with older engines that don't auto-remove keys or throw errors on missing properties without explicit handling here.  

  return existing;  // Return a reference (clone) rather than modifying the original object directly unless explicitly requested for deep copy logic elsewhere.
}

function getPropertyValue(name: string): unknown {
  const val = ctx[name];
  if (val === undefined || typeof val !== 'object') throw new Error('GetProperty failed.'); // Throws explicit error to maintain strict typing, acceptable here as the type system
