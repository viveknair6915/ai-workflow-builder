import React, { useState } from "react";
import axios from "axios";

// Fallback API URL if environment variable is not set
const API = process.env.REACT_APP_API_URL || "http://localhost:8000";

export default function ChatModal({ open, onClose }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;
    
    setLoading(true);
    try {
      const resp = await axios.post(
        `${API}/run_workflow`,
        new URLSearchParams({ 
          user_query: input, 
          use_kb: true, 
          use_web: false 
        })
      );
      setMessages((msgs) => [
        ...msgs,
        { role: "user", content: input },
        { role: "bot", content: resp.data.response },
      ]);
      setInput("");
    } catch (error) {
      console.error("Chat error:", error);
      setMessages((msgs) => [
        ...msgs,
        { role: "user", content: input },
        { role: "bot", content: "Sorry, there was an error processing your request. Please try again." },
      ]);
      setInput("");
    } finally {
      setLoading(false);
    }
  };

  if (!open) return null;
  return (
    <div
      style={{
        position: "fixed",
        top: 60,
        left: "20%",
        width: "60%",
        background: "#fff",
        border: "1px solid #ccc",
        borderRadius: 8,
        zIndex: 1000,
        padding: 20,
      }}
    >
      <h3>Chat with Stack</h3>
      <div
        style={{
          minHeight: 200,
          maxHeight: 300,
          overflowY: "auto",
          border: "1px solid #eee",
          marginBottom: 10,
          padding: 10,
        }}
      >
        {messages.map((m, i) => (
          <div key={i} style={{ margin: "8px 0" }}>
            <b>{m.role === "user" ? "You" : "Bot"}:</b> {m.content}
          </div>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        style={{ width: "80%" }}
        onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        disabled={loading}
        placeholder="Ask a question about your document..."
      />
      <button onClick={sendMessage} disabled={loading || !input.trim()}>
        {loading ? "Sending..." : "Send"}
      </button>
      <button onClick={onClose} style={{ marginLeft: 10 }}>
        Close
      </button>
    </div>
  );
} 