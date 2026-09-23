from collections import Counter
from datetime import date, timedelta
from app.data import load_profiles
from app.config import ROOT

def main():
    profiles = load_profiles()
    lines = ["# Отчёт по данным", "", f"Профилей: {len(profiles)}; синтетических в исходном датасете: {sum(p.synthetic for p in profiles)}.",
             f"Без цены: {sum(p.price_from_kzt is None for p in profiles)}; без max_hours: {sum(p.max_hours is None for p in profiles)}.",
             f"Восстановленный город: {sum(p.city_imputed for p in profiles)}; восстановленная цена: {sum(p.price_imputed for p in profiles)}.", ""]
    for key in ("city", "categories", "event_formats", "languages"):
        values = Counter(v for p in profiles for v in (getattr(p, key) if isinstance(getattr(p, key), list) else [getattr(p, key)]))
        lines += [f"## {key}", "", *[f"- {k}: {v}" for k,v in sorted(values.items())], ""]
    cities = sorted(dict.fromkeys(p.city for p in profiles))
    cats = sorted(dict.fromkeys(c for p in profiles for c in p.categories))
    lines += ["## Город × категория", "", "|Категория|"+"|".join(cities)+"|", "|---|"+"---:|"*len(cities)]
    for c in cats:
        lines += ["|"+c+"|"+"|".join(str(sum(p.city==city and c in p.categories for p in profiles)) for city in cities)+"|"]
    lines += ["", "## Календари", "", "Даты ISO YYYY-MM-DD; окно 2026-09-23–2026-12-31.", "", "|Месяц|Занятых дней / доступных профиль-дней|Доля|", "|---|---:|---:|"]
    for month, days in [(9,8),(10,31),(11,30),(12,31)]:
        busy = sum(d.month==month for p in profiles for d in p.busy_dates)
        lines.append(f"|2026-{month:02}|{busy} / {days*len(profiles)}|{busy/(days*len(profiles)):.1%}|")
    (ROOT/"docs").mkdir(exist_ok=True)
    (ROOT/"docs/DATA_REPORT.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    print("\n".join(lines))

if __name__ == "__main__":
    main()
