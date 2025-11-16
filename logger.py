import csv
import os
from datetime import datetime

LOG_PATH = "logs/llm_responses.csv"

# CSV 헤더 생성 (최초 1번)
if not os.path.exists("logs"):
    os.makedirs("logs")

if not os.path.exists(LOG_PATH):
    with open(LOG_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "prompt", "prompt_version", "model", "latency_ms", "total_tokens"])


def log_llm_response(prompt, prompt_version, model, latency_ms, total_tokens):

    with open(LOG_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            prompt,
            prompt_version,
            model,
            round(latency_ms, 2),
            total_tokens,
        ])
