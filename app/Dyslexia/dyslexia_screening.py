import whisper
import requests
import json
import os

# -----------------------------
# Step A.1: Use existing .wav file
# -----------------------------
def transcribe_audio(filename):
    print("🧠 Loading Whisper model...")
    model = whisper.load_model("base")  # You can use "tiny", "small", etc. for faster inference
    print(f"🔍 Transcribing '{filename}'...")
    result = model.transcribe(filename)
    print("📝 Transcript:", result["text"])
    return result["text"]

# -----------------------------
# Step A.2: Analyze transcript using Gemma 3n via Ollama
# -----------------------------
def analyze_transcript_with_ollama(transcript):
    prompt = f"""
The child read:
"{transcript}"

Are there signs of dyslexia? Analyze the reading errors.
Give a likelihood score from 0 to 1 and explain briefly.
Respond only in JSON like:
{{
  "dyslexia_score": float,
  "reason": string
}}
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
        raw_result = data.get("response", "")
        print("\n📦 Raw model output:\n", raw_result)

        # Remove possible Markdown formatting
        raw_result = raw_result.strip().strip("```json").strip("```")
        parsed = json.loads(raw_result)

        print("\n✅ Dyslexia Analysis:")
        print("Dyslexia Score:", parsed.get("dyslexia_score"))
        print("Reason:", parsed.get("reason"))

    except Exception as e:
        print("❌ Error parsing response:", e)
        print("Full raw response:", response.text)

# -----------------------------
# Main Execution Flow
# -----------------------------
if __name__ == "__main__":
    # 📁 Replace this with the path to your converted .wav file
    audio_file = r"C:\Users\nhars\OneDrive\Documents\Sound Recordings\kid_dyslexia_2.wav"

    if not os.path.exists(audio_file):
        print(f"❌ File not found: {audio_file}")
    else:
        transcript = transcribe_audio(audio_file)
        if transcript:
            analyze_transcript_with_ollama(transcript)
