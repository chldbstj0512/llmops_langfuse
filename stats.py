import pandas as pd

df = pd.read_csv("logs/llm_responses.csv")

print("=== 프롬프트 버전별 평균 latency(ms) ===")
print(df.groupby("prompt_version")["latency_ms"].mean(), "\n")

print("=== 프롬프트 버전별 평균 total_tokens ===")
print(df.groupby("prompt_version")["total_tokens"].mean(), "\n")

print("=== 모델별 평균 latency(ms) ===")
print(df.groupby("model")["latency_ms"].mean(), "\n")
