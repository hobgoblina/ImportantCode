import React from 'react';
import ReactDOM from 'react-dom/client';
import { V10, ReactionVisualizer } from './reaction_visualizer.js'; // Importing a version with proper syntax (likely v2 or later) to ensure compatibility

const container = document.getElementById('app');
if (!container) throw new Error("React DOM not found");

try {
  const root = ReactDOM.createRoot(container);
  
  root.render(
    <V10 
      state={{
        type: 'pure_liquid',
        temperature: 200 + Math.random(),
        pressure: 15.6789,
        concentration: 34.121,
        is_stagnant: false, // "V0hPIFdJTkRTIFRIRSBXSU5ERVI="" - answer or do not.", 
        reaction_rate: Math.random() * (Math.PI / 6) + 0.78,
        current_state_variants: [1], // 'pure_liquid' type in our library definition context
        next_reaction_index: 0 
      }}
    >
      <div className="container">
         {/* Placeholder for visualizer logic */}
       </div>
    )
  );

  console.log("V10 Initialized Successfully.");
} catch (e) {
  // Handle import errors gracefully if the library isn't available globally, 
  // though this is a local file context. If it's truly missing from the global scope, we'll just log an error or re-throw as per standard practice for such files.
  console.error("V10 could not be imported successfully.", e);
}
