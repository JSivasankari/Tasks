# CodeBuddy – LLM Chatbot (Gemini + Flask)

Multi-turn chatbot with per-conversation memory, last-N-messages context window, system prompt, and error handling.

## Run
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # then paste your key from https://aistudio.google.com/apikey
python app.py               # open http://127.0.0.1:5000
```

## How it works
- `POST /chat` takes `{message, conversation_id}` and returns `{reply, conversation_id}`.
- History is stored per `conversation_id`; only the last `MAX_MESSAGES` are sent to the model.
- Persona lives in `system_prompt.txt`; all settings live in `.env`.
- API failures/timeouts/rate limits return a clear message shown in the UI.
