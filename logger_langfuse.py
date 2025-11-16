from langfuse import Langfuse
from dotenv import load_dotenv
import os
from datetime import datetime

# Load env
load_dotenv()

# 환경변수 불러오기
LANGFUSE_SECRET = os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_PUBLIC = os.getenv("LANGFUSE_PUBLIC_KEY")

if not LANGFUSE_SECRET or not LANGFUSE_PUBLIC:
    raise ValueError("❌ Langfuse 키가 .env에서 로드되지 않았습니다.")

# Langfuse 초기화
langfuse = Langfuse(
    secret_key=LANGFUSE_SECRET,
    public_key=LANGFUSE_PUBLIC,
)

def log_llm_response(prompt, reply, prompt_version, model, latency_ms, total_tokens):
    """
    Langfuse 2.x (end() 없음 버전)
    LLM 입력 + 출력 + 메타데이터 기록
    """
    timestamp = datetime.now().isoformat()

    trace = langfuse.trace(
        name="llm-chat",
        input=prompt,     # user message
        output=reply,     # LLM output 추가!
        metadata={
            "timestamp": timestamp,
            "prompt_version": prompt_version,
            "model": model,
        }
    )

    trace.span(
        name="llm-call",
        metadata={
            "latency_ms": round(latency_ms, 2),
            "total_tokens": total_tokens,
            "prompt_version": prompt_version,
            "model": model,
            "output": reply,     # span에도 output 기록
        }
    )

    langfuse.flush()
    print(f"✅ Langfuse trace 기록 완료: {timestamp}")
