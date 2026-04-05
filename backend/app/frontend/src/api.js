// frontend/src/api.js
export async function askQuestion(question) {
  const res = await fetch(`http://localhost:8000/ask?question=${encodeURIComponent(question)}`);
  return await res.json();
}

import { useState } from "react";
import { askQuestion } from "./api";

export default function AskBox() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleAsk = async () => {
    const data = await askQuestion(question);
    setAnswer(data.answer);
  };

  return (
    <div>
      <input value={question} onChange={(e) => setQuestion(e.target.value)} />
      <button onClick={handleAsk}>Ask</button>
      <p>{answer}</p>
    </div>
  );
}