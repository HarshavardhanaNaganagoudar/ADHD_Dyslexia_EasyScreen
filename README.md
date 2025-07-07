# ADHD_Dyslexia_EasyScreen
Interactive cognitive games and voice recording activities for ADHD and dyslexia screening

# 🧠 BrainBuddy: AI-Powered ADHD + Dyslexia Assistant

## 🚀 TL;DR
- 🧠 **AI-Powered ADHD + Dyslexia Assistant** built using **Gemma 3n** via Ollama
- 🎮 Uses cognitive games to evaluate flexibility, impulsivity, and memory
- 🧾 Generates human-friendly non-diagnostic reports in JSON and natural text
- 💻 Fully local inference (via VS Code + Ollama) and **Gradio demo on Hugging Face Spaces**
- 🛠️ Architecture, prompt engineering, scoring logic, and technical stack explained below

---

## 📝 Abstract

BrainBuddy is a cognitive companion app designed for early screening of **ADHD** and **Dyslexia** in children. It leverages **Gemma 3n**, a powerful open-weight LLM, to evaluate gameplay data from cognitive tests and deliver non-diagnostic, child-friendly reports.

The goal is to assist parents and educators by providing **friendly insights**, not medical diagnoses, based on attention, impulsivity, flexibility, and memory patterns.

---

## ❓ Problem Statement

Early signs of ADHD and Dyslexia often go unnoticed, especially in resource-limited or high-stigma environments. Tools that do exist are either:
- Clinical (complex, expensive)
- Not child-friendly
- Not privacy-respecting

There is a **need for a lightweight, local-first, friendly tool** that interprets behavior from structured cognitive activities and provides helpful reports — without cloud dependencies or diagnoses.

---

## 💡 Solution Overview

BrainBuddy is a fun, AI-enhanced tool where children play short cognitive games (task switching, memory recall, etc.). The app:
1. Collects structured gameplay metrics (reaction times, task accuracy, etc.)
2. Feeds them to a local **Gemma 3n** LLM running via **Ollama**
3. Returns JSON scores and a **friendly, explainable summary**

Optionally, users can explore the **web-based Gradio UI on Hugging Face Spaces**.

---

## 🏗️ Architecture

```plaintext
+------------------+         +----------------------+         +---------------------+
|  Cognitive Games | ----->  |  Scoring Logic (Py)  | ----->  |    Gemma 3n (LLM)   |
+------------------+         +----------------------+         +---------------------+
        │                            │                                 │
        ▼                            ▼                                 ▼
 JSON gameplay data     →   Impulsivity/Flexibility Rules   →    Friendly Report
```
---

## 🧠 How Gemma 3n Is Used

- **Model:** `Gemma 3n 2B` (via **Ollama**, fully local)

### 🧪 Prompt Engineering
Carefully designed instructions to:
- ✅ Score gameplay data using thresholds
- ✅ Explain scores **only** when thresholds are exceeded
- ✅ Generate a **JSON + natural language summary**
- ✅ Add empathetic, **kid-friendly explanations**

---

## 🚧 Challenges Faced

| Challenge | Description |
|----------|-------------|
| ⚙️ Metric Mapping | Translating raw game metrics into cognitive traits (e.g., impulsivity, attention) |
| 🔐 Local Inference | Running LLM inference offline with low memory via VS Code + Ollama |
| 🧾 Friendliness | Balancing clinical accuracy with non-diagnostic, compassionate tone |
| 🧠 Prompt Clarity | Designing prompts that reflect psychology-informed, child-safe language |

---

## 🧰 Tech Stack

| Component       | Tech                                |
|----------------|-------------------------------------|
| LLM            | **Gemma 3n (2B)** via Ollama         |
| Frontend       | Gradio                              |
| Local Inference| VS Code + Python                    |
| Deployment     | Hugging Face Spaces                 |
| Prompt Logic   | Rule-based scoring + templated JSON |
| Visualization  | Markdown + Flow Diagrams            |

---

## 🔗 Links

- 🎬 **Video Demo (3 mins):** [YouTube Link](https://your-youtube-link.com)
- 💻 **Live Gradio Demo:** [Hugging Face Space](https://huggingface.co/spaces/your-space)
- 💻 **GitHub Repo:** [GitHub Project Link](https://github.com/your-repo)
- 📄 **PDF Version of Report:** [Technical_Report.pdf](./Technical_Report.pdf)

---

## 📸 Screenshots

| 🎮 Game UI | 📄 JSON Report | 🌐 Hugging Face Demo |
|-----------|----------------|----------------------|
| ![Game UI](./assets/game_ui.png) | ![JSON](./assets/json_report.png) | ![Demo](./assets/demo_ui.png) |

---

## ❤️ Final Note

**BrainBuddy** is not a diagnostic tool, but a compassionate digital assistant for curious parents, educators, and young minds.  
Built with **love**, **science**, and **ethical AI**—to make early understanding accessible for every child.

---
