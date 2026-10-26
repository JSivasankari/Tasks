import os, uuid
from dotenv import load_dotenv
from flask import Flask, request, jsonify, send_from_directory
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = os.getenv("MODEL", "gemini-2.5-flash")
MAX_MESSAGES = int(os.getenv("MAX_MESSAGES", 10))   # context window: last N messages
TIMEOUT_MS = int(os.getenv("TIMEOUT_SECONDS", 20)) * 1000
SYSTEM_PROMPT = open("system_prompt.txt", encoding="utf-8").read()

app = Flask(__name__, static_folder="static")
conversations = {}  # conversation_id -> full history (list of Content)


@app.get("/")
def index():
    return send_from_directory("static", "index.html")


@app.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    text = (data.get("message") or "").strip()
    cid = data.get("conversation_id") or str(uuid.uuid4())
    if not text:
        return jsonify(error="Please type a message."), 400

    history = conversations.setdefault(cid, [])
    history.append(types.Content(role="user", parts=[types.Part(text=text)]))

    window = history[-MAX_MESSAGES:]          # truncation strategy
    if window[0].role == "model":             # API needs the window to start with user
        window = window[1:]
    try:
        res = client.models.generate_content(
            model=MODEL,
            contents=window,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                http_options=types.HttpOptions(timeout=TIMEOUT_MS),
            ),
        )
        if not res.text:
            raise ValueError("empty response")
    except Exception as e:
        history.pop()                          # don't keep the failed turn
        code = getattr(e, "code", None)
        msg = ("Too many requests. Please wait a moment and try again." if code == 429
               else "The AI service didn't respond in time or failed. Please try again.")
        return jsonify(error=msg, conversation_id=cid), 502

    history.append(types.Content(role="model", parts=[types.Part(text=res.text)]))
    return jsonify(reply=res.text, conversation_id=cid)


if __name__ == "__main__":
    app.run(debug=True)
