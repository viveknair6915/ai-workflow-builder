import React from "react";

export default function ConfigPanel({ selectedNode, onConfigChange }) {
  if (!selectedNode) return <div>Select a component to configure.</div>;
  if (selectedNode.data.label === "KnowledgeBase") {
    return (
      <div>
        <h4>Upload Document</h4>
        <input
          type="file"
          accept="application/pdf"
          onChange={(e) => onConfigChange(e.target.files[0])}
        />
      </div>
    );
  }
  if (selectedNode.data.label === "LLM Engine") {
    return (
      <div>
        <h4>LLM Engine Config</h4>
        <label>
          Custom Prompt:
          <input
            type="text"
            onChange={(e) => onConfigChange(e.target.value)}
            style={{ width: "100%" }}
          />
        </label>
      </div>
    );
  }
  return <div>No config required.</div>;
} 