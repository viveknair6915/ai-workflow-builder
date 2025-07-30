import React from "react";
const components = [
  { type: "UserQuery", label: "User Query" },
  { type: "KnowledgeBase", label: "KnowledgeBase" },
  { type: "LLMEngine", label: "LLM Engine" },
  { type: "Output", label: "Output" },
];
export default function ComponentPanel() {
  return (
    <div style={{ padding: 10 }}>
      <h4>Components</h4>
      {components.map((c) => (
        <div
          key={c.type}
          draggable
          onDragStart={(e) => e.dataTransfer.setData("component", c.type)}
          style={{
            border: "1px solid #ccc",
            borderRadius: 4,
            padding: 8,
            marginBottom: 8,
            background: "#f9f9f9",
            cursor: "grab",
          }}
        >
          {c.label}
        </div>
      ))}
    </div>
  );
} 