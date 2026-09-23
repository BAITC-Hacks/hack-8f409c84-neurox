import re
from ..normalize import normalize
from ..config import CONFIG
from .templates import options


def normalize_numbers(text):
    text = re.sub(r"(?<=\d)[ \u00a0\u202f](?=\d{3}(?:\D|$))", "", text)
    return re.sub(r"(\d+(?:[.,]\d+)?)\s*тыс\.?", lambda m: str(int(float(m[1].replace(',', '.'))*1000)), text)


def numbers(text):
    return re.findall(r"\d+(?:[.,]\d+)?", normalize_numbers(text))


def sentences(text):
    # Punctuation inside a quoted source detail and decimal hours is not a sentence boundary.
    unquoted = re.sub(r"«[^»]*»", "SOURCE", text)
    return [p for p in re.split(r"(?<!\d)[.!?]+(?:\s+|$)|(?<=\d)[!?]+(?:\s+|$)", unquoted) if p.strip()]


def check(text, facts):
    errors = []
    if any(normalize(s) in normalize(text) for s in CONFIG["stop_phrases"]):
        errors.append("stop_phrase")
    if not 1 <= len(sentences(text)) <= 2:
        errors.append("sentence_count")
    # A closed, verifiable grammar: provider can reorder full grounded sentences only.
    # This rejects invented words, dates, guarantees, and relational claims, not just numbers.
    if text not in options(facts):
        errors.append("ungrounded_claim_or_number")
    if facts["event"] not in text or not numbers(text):
        errors.append("missing_request_parameter")
    if not facts["unique_detail"] and not facts["price_unique"]:
        errors.append("indistinguishable_facts")
    return errors


def pairwise_similarity(a, b):
    ta = sorted(dict.fromkeys(re.findall(r"[а-яa-z0-9]+", normalize(a))))
    tb = sorted(dict.fromkeys(re.findall(r"[а-яa-z0-9]+", normalize(b))))
    union = sorted(dict.fromkeys(ta+tb))
    return sum(t in tb for t in ta)/max(1, len(union))
