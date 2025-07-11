import json
import requests
import os

# -----------------------------
# Load results from each game
# -----------------------------
def load_json_results(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return {}

# -----------------------------
# Map ADHD score to likelihood level
# -----------------------------
def get_likelihood_level(score):
    if score is None:
        return "Unknown"
    if score < 0.3:
        return "Low"
    elif score >= 0.3 and score < 0.7:
        return "Moderate"
    else:
        return "High"

# -----------------------------
# Format & send to Gemma 3n
# -----------------------------
def analyze_adhd_with_ollama(go_nogo, memory, task_switch):
    prompt = f"""
The following are the results of a child's performance in three cognitive games used to assess ADHD traits:

### Go/No-Go Task (Impulsivity)
- Hits: {go_nogo.get('hits')}
- Misses: {go_nogo.get('misses')}
- False Alarms: {go_nogo.get('false_alarms')}
- Reaction Times (ms): {go_nogo.get('reaction_times_ms')}

### Memory Game (Attention Span)
- Rounds Played: {memory.get('rounds')}
- Mistakes: {memory.get('mistakes')}
- Max Sequence Recalled: {memory.get('max_sequence_recalled')}
- Click Times (ms): {memory.get('click_times_ms')}

### Task Switching Game (Cognitive Flexibility)
- Reaction Times (ms): {task_switch.get('reaction_times_ms')}
- Errors: {task_switch.get('errors')}
- Task Switch Accuracy: {task_switch.get('task_switch_accuracy')}

---

Use this strict scoring rubric to assess ADHD likelihood (score between 0.0 and 1.0). Only apply points if thresholds are exceeded. Base this on behavioral markers, not diagnoses.

---

**Impulsivity (Go/No-Go):**
- Measures tendency to act without thinking.
- Add +0.3 ONLY IF (misses > 3 OR false alarms > 3)
- Add +0.2 ONLY IF average reaction time > 1000ms (suggests delayed inhibition)

**Inattention (Memory Game):**
- Measures sustained attention and working memory.
- Add +0.2 ONLY IF max sequence recalled < 3
- Add +0.2 ONLY IF total mistakes > 3

**Cognitive Flexibility (Task Switching):**
- Measures ability to adapt to changing rules.
- Add +0.2 ONLY IF task switch accuracy < 0.6
- Add +0.1 ONLY IF average reaction time > 1500ms

---

**Total ADHD Score = sum of above (clip between 0 and 1)**

Then classify:
- Score < 0.3 → "Low likelihood of ADHD traits"
- 0.3 ≤ Score < 0.7 → "Moderate likelihood"
- Score ≥ 0.7 → "High likelihood"

Use empathetic, child-friendly explanations when presenting results.

### OUTPUT FORMAT (JSON only):
{{
  "impulsivity_score": float,
  "attention_score": float,
  "flexibility_score": float,
  "adhd_score": float,
  "likelihood_level": string,
  "reason": string
}}

Explain the reasoning clearly, justifying each score **only if** threshold was exceeded.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3n:e4b",
            "prompt": prompt,
            "stream": False
        }
    )

    try:
        data = response.json()
        raw = data.get("response", "")
        print("\n📦 Raw model output:\n", raw)

        # Clean markdown formatting if present
        raw = raw.strip().removeprefix("```json").removesuffix("```").strip()
        parsed = json.loads(raw)

        adhd_score = parsed.get("adhd_score")
        likelihood_level = parsed.get("likelihood_level") or get_likelihood_level(adhd_score)

        result = {
            "impulsivity_score": parsed.get("impulsivity_score"),
            "attention_score": parsed.get("attention_score"),
            "flexibility_score": parsed.get("flexibility_score"),
            "adhd_score": adhd_score,
            "likelihood_level": likelihood_level,
            "reason": parsed.get("reason")
        }

        print("\n✅ ADHD Analysis:")
        print(json.dumps(result, indent=2))

    except Exception as e:
        print("❌ Error parsing response:", e)
        print("Full raw response:", response.text)

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    go_nogo = load_json_results("go_nogo_results.json")
    memory = load_json_results("memory_game_results.json")
    task_switch = load_json_results("task_switch_results.json")

    analyze_adhd_with_ollama(go_nogo, memory, task_switch)