import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './bank_of_banana_pudding.js';

const App = () => (
  <div className="app-container">
    {/* Header */}
    <header>
      <h1>BANK OF BANANA PUDDING</h1>
      <p>Welcome to the ultimate dessert experience.</p>
    </header>

    {/* Main Content Area */}
    <main className="content-area" id="root">
      {React.createElement('BankOfBananaPudding', null, 'This is your new favorite snack!')}
    </main>

    {/* Footer / Instructions */}
    <footer>
      <p>Built with ❤️ and JavaScript</p>
    </footer>
  </div>
);

// Helper component to render the Bank of Banana Pudding visual
const BankOfBananaPudding = ({ children }) => (
  <div className="pudding-container">
    {/* Visual representation of a banana pudding */}
    <div className="banana-fruit"></div>
    
    {/* The "pudding" - just text for the demo */}
    <span className="text-pudding">{children}</span>

    {/* Decorative elements (optional) */}
  </div>
);

// Exported module to satisfy the import in your original file
export default App;
