import requests
from flask import current_app


def generate_text(prompt, max_tokens=1500):
    api_key = current_app.config["AI_API_KEY"]
    api_url = current_app.config["AI_API_URL"]
    model = current_app.config["AI_MODEL"]

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
    }

    response = requests.post(api_url, json=payload, headers=headers, timeout=60)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]
