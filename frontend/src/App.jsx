import React, { useState } from "react";
import ComponentPanel from "./components/ComponentPanel";
import Workspace from "./components/Workspace";
import ConfigPanel from "./components/ConfigPanel";
import ChatModal from "./components/ChatModal";
import axios from "axios";

// Fallback API URL if environment variable is not set
const API = process.env.REACT_APP_API_URL || "http://localhost:8000";

export default function App() {
  const [selectedNode, setSelectedNode] = useState(null);
  const [chatOpen, setChatOpen] = useState(false);

  const handleConfigChange = async (value) => {
    if (selectedNode?.data.label === "KnowledgeBase" && value) {
      try {
        // Upload PDF
        const form = new FormData();
        form.append("file", value);
        const response = await axios.post(`${API}/upload`, form);
        alert("Document uploaded and processed!");
      } catch (error) {
        console.error("Upload error:", error);
        alert("Error uploading document. Please try again.");
      }
    }
    // For LLM Engine, you could store prompt in state if needed
  };

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      <div style={{ width: 200, borderRight: "1px solid #eee" }}>
        <ComponentPanel />
      </div>
      <div style={{ flex: 1, padding: 20 }}>
        <Workspace onSelectNode={setSelectedNode} />
        <button
          style={{ marginTop: 20 }}
          onClick={() => setChatOpen(true)}
        >
          Chat with Stack
        </button>
      </div>
      <div style={{ width: 300, borderLeft: "1px solid #eee", padding: 20 }}>
        <ConfigPanel
          selectedNode={selectedNode}
          onConfigChange={handleConfigChange}
        />
      </div>
      <ChatModal open={chatOpen} onClose={() => setChatOpen(false)} />
    </div>
  );
} 