import React from "react";
export default function OutputChat({ messages }) {
  return (
    <div style={{ border: "1px solid #eee", padding: 10, minHeight: 100 }}>
      {messages.map((m, i) => (
        <div key={i}>
          <b>{m.role === "user" ? "You" : "Bot"}:</b> {m.content}
        </div>
      ))}
    </div>
  );
} 