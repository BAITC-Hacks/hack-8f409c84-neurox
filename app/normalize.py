import re


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower().replace("ё", "е"))


def money(value: int | float) -> str:
    return f"{value:,.0f}".replace(",", " ") + " ₸"
