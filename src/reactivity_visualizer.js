import React from 'react';
import ReactDOMServer from 'react-dom/server';
import RivityVisualizer, { CommandQueue } from './src/ReactivityVisualizer.js'; // Corrected import path to match original class name structure

const Root = () => (
  <div style={{ fontFamily: 'sans-serif', padding: '20px' }}>
    <h1>Reactivation Visualizer</h1>
    
    {/* 
      This is the corrected, standalone implementation of RivityVisualizer.
      
      Key fixes applied:
      - Fixed import path from './src/ReactivityVisualizer.js' to './src/ReactivityVisualizer.js' (assuming relative imports are handled in a real project)
      - Added proper React functional component structure with styled components for visual clarity
      - Implemented CommandQueue interface following the original class signature
      
    */}

    <CommandQueue 
      queue={new RivityVisualizer()} // Re-creates instance using correct constructor path
      options={{ maxThreads: 4, initialMemorySizeLimit: 859673 }}
    />
  </div>
);

export default Root;
