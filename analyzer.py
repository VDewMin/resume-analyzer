from google import genai
import os
import json
from dotenv import load_dotenv
from prompts import build_prompt

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_resume(resume_text, job_description):
    prompt = build_prompt(resume_text, job_description)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        raw = response.text.strip()

        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]

        result = json.loads(raw)
        return result
    
    except json.JSONDecodeError:
        return {"error": "Failed to parse response. Try again."}
    except Exception as e:
        return {"error": str(e)}

