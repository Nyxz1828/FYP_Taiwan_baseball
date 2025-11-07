import express from "express";
import OpenAI from "openai";
import dotenv from "dotenv";
import path from "path";
import { fileURLToPath } from "url";

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3000;

// Middleware
app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// === API route for generating graph ===
app.post("/api/generate-graph", async (req, res) => {
  const { prompt } = req.body;
  console.log("🧠 Received prompt:", prompt);

  try {
    const completion = await openai.chat.completions.create({
      model: "gpt-5",
      messages: [
        {
          role: "system",
          content: "You are a Chart.js code generator. Respond ONLY with valid JavaScript code that calls new Chart(ctx, {...}) and returns the chart instance. No explanations.",
        },
        { role: "user", content: prompt },
      ],
    });

    const jsCode = completion.choices[0].message.content.trim();
    res.json({ jsCode });
  } catch (err) {
    console.error("❌ Error generating chart:", err);
    res.status(500).json({ error: "AI chart generation failed." });
  }
});

app.listen(PORT, () =>
  console.log(`🚀 Server running at http://localhost:${PORT}`)
);
