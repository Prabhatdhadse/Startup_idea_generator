import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [keyword, setKeyword] = useState("");
  const [idea, setIdea] = useState("");
  const [loading, setLoading] = useState(false);
  const [darkMode, setDarkMode] = useState(false);

  const generateIdea = async () => {
    if (!keyword.trim()) {
      alert("Please enter a keyword");
      return;
    }
    setLoading(true);
    setIdea("");
    try {
      const res = await axios.post("http://startup-idea-generator.onrender.com/generate", { keyword });
      if (res.data && res.data.idea) {
        setIdea(res.data.idea);
      } else {
        setIdea("Could not generate idea. Try again.");
      }
    } catch (err) {
      console.error(err);
      setIdea("Error connecting to backend.");
    } finally {
      setLoading(false);
    }
  };

  const generateMultiple = async (n = 5) => {
    if (!keyword.trim()) { alert("Enter keyword"); return; }
    setLoading(true);
    setIdea("");
    try {
      const ideas = [];
      for (let i = 0; i < n; i++) {
        const res = await axios.post("http://startup-idea-generator.onrender.com/generate", { keyword });
        ideas.push(res.data.idea);
      }
      setIdea(ideas.map((it, idx) => `${idx + 1}. ${it}`).join("\n\n"));
    } catch (err) {
      console.error(err);
      setIdea("Error generating ideas.");
    } finally {
      setLoading(false);
    }
  };

  const copyToClipboard = () => {
    navigator.clipboard.writeText(idea);
    alert("Idea copied to clipboard!");
  };

  const toggleDarkMode = () => setDarkMode(!darkMode);

  return (
    <div className={`app-container ${darkMode ? "dark" : ""}`}>
      <header className="header">
        <h1 className="title">💡 Startup Idea Generator</h1>
        <button className="btn toggle-mode" onClick={toggleDarkMode}>
          {darkMode ? "Light Mode" : "Dark Mode"}
        </button>
      </header>
      <p className="subtitle">Type a keyword and get creative startup ideas instantly.</p>

      <div className="input-container">
        <input
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          placeholder="Enter keyword..."
          className="keyword-input"
        />
        <button className="btn generate" onClick={generateIdea}>Generate</button>
        <button className="btn generate-multi" onClick={() => generateMultiple(5)}>Generate 5</button>
      </div>

      {loading && <div className="loading">Generating...</div>}

      {idea && (
        <div className="idea-card">
          <pre>{idea}</pre>
          <button className="btn copy-btn" onClick={copyToClipboard}>📋 Copy</button>
        </div>
      )}

      <footer className="footer">
        Backend: <code>https://startup-idea-generator.onrender.com</code>
      </footer>
    </div>
  );
}

export default App;
