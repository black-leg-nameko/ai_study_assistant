"use client";

import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");

  const ask = async () => {
    const res = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    });

    const data = await res.json();
    setAnswer(data.answer);
  };

  return (
    <main style={{ padding: 40, maxWidth: 600, margin: "0 auto" }}>
      <h1>AI 学習アシスタント</h1>

      <textarea
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="質問を入力..."
        style={{ width: "100%", height: 120, marginTop: 20 }}
      />

      <button
        onClick={ask}
        style={{
          marginTop: 20,
          padding: "10px 20px",
          fontSize: 16,
          cursor: "pointer",
        }}
      >
        質問する
      </button>

      {answer && (
        <div style={{ marginTop: 40 }}>
          <h2>回答</h2>
          <p>{answer}</p>
        </div>
      )}
    </main>
  );
}
