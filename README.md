# 🧠 ADHD-Dyslexia-EasyScreen: AI-Powered ADHD + Dyslexia screening for children

## 🚀 TL;DR
- 🧠 **AI-Powered ADHD + Dyslexia Screening** built using Google **Gemma 3n** via Ollama
- 🎮 Combines audio-based reading comprehension (for dyslexia) and interactive cognitive games (for ADHD: flexibility, impulsivity, and memory evaluation)
- 🧾 Produces non-diagnostic, human-friendly reports in both JSON and natural language text
- 💻 Runs entirely offline/local via VS Code + Ollama
- 🛠️ Architecture, prompt engineering, scoring logic, and technical stack explained below.

---

## 📝 Abstract

ADHD-Dyslexia-EasyScreen is a cognitive companion app designed for early screening of **ADHD** and **Dyslexia** in children. It leverages **Gemma 3n**, a powerful open-weight LLM, to evaluate gameplay data from cognitive tests and deliver non-diagnostic, child-friendly reports.

The goal is to assist parents and educators by providing **friendly insights**, not medical diagnoses, based on factors reading comprehension, attention, impulsivity, flexibility, and memory patterns.

---

## ❓ Problem Statement

Early signs of ADHD and Dyslexia often go unnoticed, especially in resource-limited or high-stigma environments. Tools that do exist are either:
- Clinical (complex, expensive)
- Not child-friendly
- Not privacy-respecting (cloud-dependent)

There is a **need for a lightweight, local-first, friendly tool** that interprets behavior from structured cognitive activities and provides helpful reports — without cloud dependencies or diagnoses.

---

## 💡 Solution Overview

ADHD-Dyslexia-EasyScreen is a fun, AI-enhanced tool where children play short cognitive games (reading aloud, task switching, memory recall, etc.). The app:
1. Collects structured gameplay metrics (reaction times, task accuracy, etc.)
2. Feeds them to a local **Gemma 3n** LLM running via **Ollama**
3. Returns JSON scores and a **friendly, explainable summary** — tailored for parents and educators.
4. Designed to be lightweight, private, and engaging — all without internet dependency or diagnostic claims.
   
---

## 🏗️ Architecture
The ADHD-Dyslexia-EasyScreen system is composed of modular components that operate **fully offline**, enabling local cognitive evaluation via games and audio transcription.

The app is designed for **100% offline use**, ensuring **maximum data privacy** and **accessibility** for children anywhere.

### 🧩 Components

- **Frontend**: Local UI (Gradio, Tkinter, or simple HTML)
- **Game Logic**: Python-based cognitive games for ADHD & Dyslexia traits
- **Prompt Layer**: Converts gameplay metrics into LLM input using scoring thresholds
- **LLM Engine**: Ollama runs `gemma3n:e4b` **fully locally** on CPU or GPU
- **Output Renderer**: JSON + friendly report displayed locally, no cloud used

### 📦 Packaging

- Can be packaged with `PyInstaller` for Windows/Mac/Linux
- Optionally run from USB drive or SD card

### 💡 Why This Matters

This architecture makes **ADHD-Dyslexia-EasyScreen**:
- 📶 **Internet-independent**
- 🔐 **Privacy-focused**
- 🎒 **Anywhere-deployable**
- 🧠 **Ethically aligned for young users**
  
### 🏛️ Architecture Diagram
![Architecture Diagram](https://github.com/HarshavardhanaNaganagoudar/ADHD_Dyslexia_EasyScreen/blob/main/ADHD_Dyslexia_EasyScreen_Architecture.png)

---
## 🧠 How Gemma 3n Is Used

- **Model:** `gemma3n:e4b` (via **Ollama**, fully local)

### 🧪 Prompt Engineering
Custom prompts are crafted to ensure:
- ✅ Structured **scoring of gameplay data** using predefined thresholds
- ✅ Explanations are included **only when thresholds are exceeded**
- ✅ Outputs are delivered in both **JSON and natural language summaries**
- ✅ Responses are written in a **friendly, empathetic tone** suitable for children and parents

---

## 🚧 Challenges Faced

| Challenge         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| ⚙️ Metric Mapping | Translating raw gameplay metrics into cognitive traits (e.g., impulsivity, attention) |
| 🔐 Local Inference | Ensuring LLM inference runs fully offline with limited memory using VS Code + Ollama |
| 🧾 Friendliness    | Balancing psychological accuracy with a non-diagnostic, compassionate tone     |
| 🧠 Prompt Clarity  | Designing prompts that are psychology-informed, child-safe, and effective      |


---

## 🧰 Tech Stack

| Component       | Tech                                |
|----------------|-------------------------------------|
| LLM            | **gemma3n:e4b** via Ollama         |
| Frontend       | Local UI                             |
| Local Inference| VS Code + Python                    |
| Prompt Logic   | Rule-based scoring + templated JSON |
| Visualization  | Markdown + Flow Diagrams            |

---

## 🔗 Links

- 🎬 **Video Demo (3 mins):** [YouTube Link](https://your-youtube-link.com)
- 💻 **GitHub Repo:** [GitHub Project Link](https://github.com/your-repo)
- 📄 **PDF Version of Report:** [Technical_Report.pdf](./Technical_Report.pdf)

---

## 📸 Screenshots

| 📄 Dyslexia Sample Output | 📄 ADHD Sample Output |
|-----------|----------------|
| ![Dyslexia Sample Output](https://github.com/HarshavardhanaNaganagoudar/ADHD_Dyslexia_EasyScreen/blob/main/Dyslexia_sample_output.png) | ![ADHD Sample Output](https://github.com/HarshavardhanaNaganagoudar/ADHD_Dyslexia_EasyScreen/blob/main/ADHD_sample_output.png) |

---

## ❤️ Final Note

**BrainBuddy** is not a diagnostic tool, but a compassionate digital assistant for curious parents, educators, and young minds.  
Built with **love**, **science**, and **ethical AI**—to make early understanding accessible for every child.

---

## 🧠 Architecture – Fully Offline Gemma 3n App



📸 See the [diagram](./architecture_offline.png) for a visual overview.
