import ReactDOMServer from "next/server"; // Removed unused import for cleaner syntax, reusing server rendering logic if needed elsewhere in project context to avoid duplication or maintainability issues with external dependencies like html2canvas unless strictly required by a specific library (e.g., next-content-compiler) that is not currently imported.
// The provided code attempts to use html2canvas directly on the raw string content, but 'html2canvas' requires a canvas element and often uses DOM manipulation or libraries like `dom-wasm` which may fail in some environments without explicit setup (e.g., no HTML5 Canvas API). It is safer to render the visualizer as an interactive component using standard Next.js client-side rendering logic.

function renderHtml(htmlContent) {
  return <React.Fragment>
    {/* Basic HTML structure */}
    <div className="container">
      <h1>{htmlContent}</h1>
      
      {/* Interactive elements for demonstration */}
      <p>The visualizer processes the string character-by-character.</p>
      <button onClick={() => console.log("Input modified")}>Modify Input</button>
    </div>

    {htmlContent && (
      <>
        <pre>{htmlContent}</pre>
        
        {/* Hex dump view */}
        <code className="hex-dump" dangerouslySetInnerHTML={{ __html: htmlContent.replace(/[^a-f0-9]/g, '#') }} />
      </>
    )}

  </React.Fragment>;
}

export default renderHtml;
