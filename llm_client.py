from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_TEMPLATES = {
    "v1": """당신은 간단하게 짧은 문장으로 대답하는 챗봇입니다.
사용자 메시지: {message}
""",
    "v2": """당신은 자세하게 단계별로 설명하는 챗봇입니다.
가능하면 예시를 1~2개 포함합니다.
사용자 메시지: {message}
""",
    "v3": """당신은 초등학생도 이해할 수 있도록 설명하는 선생님 챗봇입니다.
사용자 메시지: {message}
"""
}


def call_llm(message: str, prompt_version: str):

    template = PROMPT_TEMPLATES.get(prompt_version, PROMPT_TEMPLATES["v1"])
    
    prompt = template.format(message=message)

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "당신은 사용자 질문에 답하는 챗봇입니다."},
            {"role": "user", "content": prompt},
        ]
    )

    reply = response.choices[0].message.content
    total_tokens = response.usage.total_tokens if response.usage else -1

    return reply, "gpt-5", total_tokens
