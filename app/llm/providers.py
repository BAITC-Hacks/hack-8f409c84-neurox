"""Optional API used only for an explanation plan; ranking never calls it."""
from typing import Protocol
import httpx


class LLMProvider(Protocol):
    def choose(self, rows: list[dict], feedback: list[str]) -> list[int]: ...


class EmbeddingProvider(Protocol):
    def embed(self, texts: list[str]) -> list[list[float]]: ...


class OfflineProvider:
    def choose(self, rows, feedback):
        return [i % 2 for i in range(len(rows))]


class OpenAIProvider:
    def __init__(self, api_key, model, timeout=3.0):
        self.api_key, self.model, self.timeout = api_key, model, timeout

    def choose(self, rows, feedback):
        import json
        schema = {"type": "object", "properties": {"choices": {"type": "array", "items": {"type": "integer", "enum": [0, 1]}}}, "required": ["choices"], "additionalProperties": False}
        with httpx.Client(timeout=self.timeout) as client:
            response = client.post("https://api.openai.com/v1/chat/completions", headers={"Authorization": f"Bearer {self.api_key}"}, json={
                "model": self.model, "temperature": 0, "seed": 79,
                "messages": [{"role": "system", "content": "Выберите вариант объяснения для каждой карточки. Верните choices в исходном порядке. Рубрика: конкретность, привязка к запросу, различимость, обоснованность, честный компромисс, 1–2 предложения. Не выдумывайте факты. Общие рекламные фразы запрещены. Вариант 1 начинает с отличительной детали, вариант 0 — с цены. Учитывайте соседние карточки."}, {"role": "user", "content": json.dumps({"rows": rows, "feedback": feedback}, ensure_ascii=False)}],
                "response_format": {"type": "json_schema", "json_schema": {"name": "explanation_plan", "strict": True, "schema": schema}}})
            response.raise_for_status()
            return json.loads(response.json()["choices"][0]["message"]["content"])["choices"]
