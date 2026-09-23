# Объяснения: 10 запросов

Полные выдачи с trace; текст автоматически получен из текущего кода и данных.

## Запрос 1

```json
{"city": "Алматы", "date": "2026-09-26", "event": "свадьба", "category": "Фотограф", "budget": 2000000}
```

**MATCHED** · 4.23 мс

В городе Алматы, категория «Фотограф»: всего 8, проходят 4. Подобрали 3. Исключено из-за занятости на 26.09.2026: 4.

### Сацуки Кусакабэ · Фотограф · Алматы · от 200 000 ₸

реальный · score 0.1398

Формат «свадьба» указан в профиле; цена от 200 000 ₸ оставляет 1 800 000 ₸ от вашего бюджета 2 000 000 ₸. В описании: «Люблю живые кадры, настоящие улыбки и моменты, которые невозможно повторить»; самая низкая начальная цена среди показанных.

### Альфонс Элрик · Фотограф · Алматы · от 300 000 ₸

реальный · score 0.1285

В описании: «Но география для меня не так важна, как чувства, свет и тишина внутри кадра»; дороже самого недорогого в этой выдаче на 100 000 ₸. Формат «свадьба» указан в профиле; цена от 300 000 ₸ оставляет 1 700 000 ₸ от вашего бюджета 2 000 000 ₸.

Цена проставлена при подготовке данных, уточните у подрядчика

### Леорио Паради · Фотограф · Алматы · от 350 000 ₸

реальный · score 0.0875

Формат «свадьба» указан в профиле; цена от 350 000 ₸ оставляет 1 650 000 ₸ от вашего бюджета 2 000 000 ₸. В описании: «Помимо свадеб снимаю и концерты, имею такие кейсы как: MC Kaze, Crimson Peas, Ray Nova, IL Sora, Sakura Sterling, Yumeko, Kaze Khalib, Tengri Bek,…»; дороже самого недорогого в этой выдаче на 150 000 ₸.

<details><summary>Trace и timings</summary>

```json
{
  "trace": [
    {
      "step": "load_normalize",
      "profiles": 66
    },
    {
      "step": "scope",
      "count": 8
    },
    {
      "step": "hard_filters",
      "passed": 4,
      "excluded": [
        {
          "id": "HK-16628",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-26"
            }
          ]
        },
        {
          "id": "HK-20640",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-26"
            },
            {
              "reason": "format",
              "event": "свадьба"
            }
          ]
        },
        {
          "id": "HK-35913",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-26"
            },
            {
              "reason": "format",
              "event": "свадьба"
            }
          ]
        },
        {
          "id": "HK-91112",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-26"
            }
          ]
        }
      ],
      "counts": {
        "busy": 4,
        "format": 0,
        "budget": 0,
        "language": 0,
        "hours": 0
      }
    },
    {
      "step": "scoring",
      "candidates": [
        {
          "id": "HK-76268",
          "score": 0.1398,
          "components": {
            "budget_fit": 0.1333333333333333,
            "semantic_fit": 0.1437551120641015
          },
          "data_quality_penalty": 0.0,
          "semantic_backend": "tfidf-local-v1"
        },
        {
          "id": "HK-53108",
          "score": 0.1285,
          "components": {
            "budget_fit": 0.20000000000000007,
            "semantic_fit": 0.10964736709170758
          },
          "data_quality_penalty": 0.015,
          "semantic_backend": "tfidf-local-v1"
        },
        {
          "id": "HK-30583",
          "score": 0.0875,
          "components": {
            "budget_fit": 0.2333333333333334,
            "semantic_fit": 0.0
          },
          "data_quality_penalty": 0.0,
          "semantic_backend": "tfidf-local-v1"
        },
        {
          "id": "HK-68220",
          "score": 0.0475,
          "components": {
            "budget_fit": 0.1266666666666666,
            "semantic_fit": 0.0
          },
          "data_quality_penalty": 0.0,
          "semantic_backend": "tfidf-local-v1"
        }
      ]
    },
    {
      "step": "explanation",
      "facts": [
        {
          "id": "HK-76268",
          "price": 200000,
          "budget": 2000000,
          "saving": 1800000,
          "event": "свадьба",
          "lang": null,
          "hours": null,
          "max_hours": 10.0,
          "detail": "Люблю живые кадры, настоящие улыбки и моменты, которые невозможно повторить",
          "details": [
            "Люблю живые кадры, настоящие улыбки и моменты, которые невозможно повторить",
            "Вхожу в топ 5 Алматы по версии AniWed Rating",
            "Снимаю в Алмате и Астане"
          ],
          "unique_detail": true,
          "price_unique": true,
          "more_than_cheapest": 0,
          "cheaper_than_others": true,
          "indistinguishable": false
        },
        {
          "id": "HK-53108",
          "price": 300000,
          "budget": 2000000,
          "saving": 1700000,
          "event": "свадьба",
          "lang": null,
          "hours": null,
          "max_hours": 6.0,
          "detail": "Но география для меня не так важна, как чувства, свет и тишина внутри кадра",
          "details": [
            "Но география для меня не так важна, как чувства, свет и тишина внутри кадра",
            "Я фотограф и уже около семи лет я ловлю моменты, которые обычно проходят незаметно",
            "Я снимал в разных городах и странах — Париже, Дубае, Москве, Китае"
          ],
          "unique_detail": true,
          "price_unique": true,
          "more_than_cheapest": 100000,
          "cheaper_than_others": false,
          "indistinguishable": false
        },
        {
          "id": "HK-30583",
          "price": 350000,
          "budget": 2000000,
          "saving": 1650000,
          "event": "свадьба",
          "lang": null,
          "hours": null,
          "max_hours": 8.0,
          "detail": "Помимо свадеб снимаю и концерты, имею такие кейсы как: MC Kaze, Crimson Peas, Ray Nova, IL Sora, Sakura Sterling, Yumeko, Kaze Khalib, Tengri Bek,…",
          "details": [
            "Помимо свадеб снимаю и концерты, имею такие кейсы как: MC Kaze, Crimson Peas, Ray Nova, IL Sora, Sakura Sterling, Yumeko, Kaze Khalib, Tengri Bek,…",
            "География моих съемок: Франция(fashion week), Италия, Великобритания, Турция, Грузия, ОАЭ, Азербайджан и тд",
            "Эстетика, атмосфера, детали — это все про меня"
          ],
          "unique_detail": true,
          "price_unique": true,
          "more_than_cheapest": 150000,
          "cheaper_than_others": false,
          "indistinguishable": false
        }
      ],
      "backend": "cache",
      "cache_key": "cd643e8922aadaef2412a6dd515bbbb40b4640ac23cd9aa146d38081652db038",
      "critic_errors": []
    }
  ],
  "timings_ms": {
    "filters": 0.195,
    "scoring": 2.614,
    "explanations": 1.42,
    "hints": 0.0,
    "total": 4.229
  }
}
```
</details>

## Запрос 2

```json
{"city": "Алматы", "category": "Декоратор", "event": "свадьба", "date": "2026-09-23", "budget": 2000000}
```

**MATCHED** · 1.89 мс

В городе Алматы, категория «Декоратор»: всего 3, проходят 1. Подобрали 1. Найдено 1 — меньше трёх: заняты на дату — 1; не проходят по бюджету (включая неизвестную цену) — 1. Исключено из-за занятости на 23.09.2026: 1.

### Уинри Рокбелл · Декоратор · Алматы · от 2 000 000 ₸

реальный · score 0.25

Формат «свадьба» указан в профиле; цена от 2 000 000 ₸ оставляет 0 ₸ от вашего бюджета 2 000 000 ₸. В описании: «индивидуальные концепции под клиента авторские эскизы перед реализацией собственное производство конструкций работа под ключ без стресса для клиента опыт крупных проектов и масштабных площадок».

Подсказка: При остальных условиях без изменений: 24.09.2026 — подходят 2; 25.09.2026 — подходят 1; 26.09.2026 — подходят 1.

Подсказка: Ещё один кандидат прошёл бы при бюджете от 2 200 000 ₸: сейчас не хватает 200 000 ₸.

Подсказка: Один из исключённых кандидатов занят 23.09.2026, но прошёл бы все условия 24.09.2026.

<details><summary>Trace и timings</summary>

```json
{
  "trace": [
    {
      "step": "load_normalize",
      "profiles": 66
    },
    {
      "step": "scope",
      "count": 3
    },
    {
      "step": "hard_filters",
      "passed": 1,
      "excluded": [
        {
          "id": "HK-90003",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-23"
            }
          ]
        },
        {
          "id": "HK-90004",
          "primary_reason": "budget",
          "all_reasons": [
            {
              "reason": "budget",
              "missing_price": false,
              "over_budget_kzt": 200000
            }
          ]
        }
      ],
      "counts": {
        "busy": 1,
        "format": 0,
        "budget": 1,
        "language": 0,
        "hours": 0
      }
    },
    {
      "step": "scoring",
      "candidates": [
        {
          "id": "HK-11484",
          "score": 0.25,
          "components": {
            "budget_fit": 0.6666666666666667,
            "semantic_fit": 0.0
          },
          "data_quality_penalty": 0.0,
          "semantic_backend": "tfidf-local-v1"
        }
      ]
    },
    {
      "step": "explanation",
      "facts": [
        {
          "id": "HK-11484",
          "price": 2000000,
          "budget": 2000000,
          "saving": 0,
          "event": "свадьба",
          "lang": null,
          "hours": null,
          "max_hours": null,
          "detail": "индивидуальные концепции под клиента авторские эскизы перед реализацией собственное производство конструкций работа под ключ без стресса для клиента опыт крупных проектов и масштабных площадок",
          "details": [
            "индивидуальные концепции под клиента авторские эскизы перед реализацией собственное производство конструкций работа под ключ без стресса для клиента опыт крупных проектов и масштабных площадок",
            "Работаем под ключ: от идеи и эскиза до монтажа и финальной реализации",
            "Более 5 лет создаём концепции свадеб, юбилеев и корпоративных событий премиум-уровня"
          ],
          "unique_detail": true,
          "price_unique": true,
          "more_than_cheapest": 0,
          "cheaper_than_others": false,
          "indistinguishable": false
        }
      ],
      "backend": "cache",
      "cache_key": "34be480ba2a03d91f74b7bd34a00e3aefda8220d0102d7bcc916ac3e64424e41",
      "critic_errors": []
    }
  ],
  "timings_ms": {
    "filters": 0.099,
    "scoring": 0.393,
    "explanations": 0.403,
    "hints": 0.99,
    "total": 1.886
  }
}
```
</details>

## Запрос 3

```json
{"city": "Алматы", "date": "2026-09-26", "event": "свадьба", "category": "Фотограф", "budget": 1}
```

**NONE_PASS_CONDITIONS** · 5.91 мс

В городе Алматы, категория «Фотограф»: всего 8, проходят 0. Ни один кандидат не проходит: заняты на дату — 4; не проходят по бюджету (включая неизвестную цену) — 4. Исключено из-за занятости на 26.09.2026: 4.

Подсказка: Ещё один кандидат прошёл бы при бюджете от 190 000 ₸: сейчас не хватает 189 999 ₸.

<details><summary>Trace и timings</summary>

```json
{
  "trace": [
    {
      "step": "load_normalize",
      "profiles": 66
    },
    {
      "step": "scope",
      "count": 8
    },
    {
      "step": "hard_filters",
      "passed": 0,
      "excluded": [
        {
          "id": "HK-16628",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-26"
            },
            {
              "reason": "budget",
              "missing_price": false,
              "over_budget_kzt": 599999
            }
          ]
        },
        {
          "id": "HK-20640",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-26"
            },
            {
              "reason": "format",
              "event": "свадьба"
            },
            {
              "reason": "budget",
              "missing_price": false,
              "over_budget_kzt": 149999
            }
          ]
        },
        {
          "id": "HK-30583",
          "primary_reason": "budget",
          "all_reasons": [
            {
              "reason": "budget",
              "missing_price": false,
              "over_budget_kzt": 349999
            }
          ]
        },
        {
          "id": "HK-35913",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-26"
            },
            {
              "reason": "format",
              "event": "свадьба"
            },
            {
              "reason": "budget",
              "missing_price": false,
              "over_budget_kzt": 399999
            }
          ]
        },
        {
          "id": "HK-53108",
          "primary_reason": "budget",
          "all_reasons": [
            {
              "reason": "budget",
              "missing_price": false,
              "over_budget_kzt": 299999
            }
          ]
        },
        {
          "id": "HK-68220",
          "primary_reason": "budget",
          "all_reasons": [
            {
              "reason": "budget",
              "missing_price": false,
              "over_budget_kzt": 189999
            }
          ]
        },
        {
          "id": "HK-76268",
          "primary_reason": "budget",
          "all_reasons": [
            {
              "reason": "budget",
              "missing_price": false,
              "over_budget_kzt": 199999
            }
          ]
        },
        {
          "id": "HK-91112",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-26"
            },
            {
              "reason": "budget",
              "missing_price": false,
              "over_budget_kzt": 299999
            }
          ]
        }
      ],
      "counts": {
        "busy": 4,
        "format": 0,
        "budget": 4,
        "language": 0,
        "hours": 0
      }
    },
    {
      "step": "scoring",
      "candidates": []
    },
    {
      "step": "explanation",
      "facts": [],
      "backend": "none"
    }
  ],
  "timings_ms": {
    "filters": 0.118,
    "scoring": 0.001,
    "explanations": 0.015,
    "hints": 5.778,
    "total": 5.912
  }
}
```
</details>

## Запрос 4

```json
{"city": "Астана", "date": "2026-10-01", "event": "свадьба", "category": "Декоратор", "budget": 2000000}
```

**NO_CATEGORY_IN_CITY** · 0.15 мс

В городе Астана, категория «Декоратор»: всего 0, проходят 0. В этом городе нет ни одного профиля запрошенной категории. Исключено из-за занятости на 01.10.2026: 0.

Подсказка: Категория есть в городах: Алматы

<details><summary>Trace и timings</summary>

```json
{
  "trace": [
    {
      "step": "load_normalize",
      "profiles": 66
    },
    {
      "step": "scope",
      "count": 0
    },
    {
      "step": "hard_filters",
      "passed": 0,
      "excluded": [],
      "counts": {
        "busy": 0,
        "format": 0,
        "budget": 0,
        "language": 0,
        "hours": 0
      }
    },
    {
      "step": "scoring",
      "candidates": []
    },
    {
      "step": "explanation",
      "facts": [],
      "backend": "none"
    }
  ],
  "timings_ms": {
    "filters": 0.103,
    "scoring": 0.002,
    "explanations": 0.028,
    "hints": 0.021,
    "total": 0.154
  }
}
```
</details>

## Запрос 5

```json
{"city": "Астана", "category": "Видеограф", "event": "свадьба", "date": "2026-09-24", "budget": 1000000, "hours": 3, "lang": "русский"}
```

**MATCHED** · 5.00 мс

В городе Астана, категория «Видеограф»: всего 2, проходят 2. Подобрали 2. Найдено 2 — меньше трёх: в каталоге города всего 2 профиля этой категории. Исключено из-за занятости на 24.09.2026: 0.

### Киллуа Золдик · Видеограф · Астана · от 300 000 ₸

реальный · score 0.4169

Формат «свадьба» указан в профиле; цена от 300 000 ₸ оставляет 700 000 ₸ от вашего бюджета 1 000 000 ₸; рабочий язык — русский; доступно до 12 ч при запросе 3 ч. В описании: «Снимаю с душой и ради удовольствия»; самая низкая начальная цена среди показанных.

### Тодороки Шото · Видеограф · Астана · от 400 000 ₸

реальный · score 0.36

В описании: «TODOROKI SHOTO WEDDING VIDEOGRAPHER -colorist of the year 2025 🏆 Считаю себя счастливым человеком, так как любимое занятие стало делом моей жизни»; дороже самого недорогого в этой выдаче на 100 000 ₸. Формат «свадьба» указан в профиле; цена от 400 000 ₸ оставляет 600 000 ₸ от вашего бюджета 1 000 000 ₸; рабочий язык — русский; доступно до 12 ч при запросе 3 ч.

Подсказка: При остальных условиях без изменений: 25.09.2026 — подходят 1; 26.09.2026 — подходят 1; 27.09.2026 — подходят 2.

<details><summary>Trace и timings</summary>

```json
{
  "trace": [
    {
      "step": "load_normalize",
      "profiles": 66
    },
    {
      "step": "scope",
      "count": 2
    },
    {
      "step": "hard_filters",
      "passed": 2,
      "excluded": [],
      "counts": {
        "busy": 0,
        "format": 0,
        "budget": 0,
        "language": 0,
        "hours": 0
      }
    },
    {
      "step": "scoring",
      "candidates": [
        {
          "id": "HK-74914",
          "score": 0.4169,
          "components": {
            "budget_fit": 0.4,
            "semantic_fit": 0.19372366371545258,
            "language_fit": 1.0,
            "hours_fit": 1.0
          },
          "data_quality_penalty": 0.0,
          "semantic_backend": "tfidf-local-v1"
        },
        {
          "id": "HK-10990",
          "score": 0.36,
          "components": {
            "budget_fit": 0.5333333333333334,
            "semantic_fit": 0.0,
            "language_fit": 1.0,
            "hours_fit": 1.0
          },
          "data_quality_penalty": 0.0,
          "semantic_backend": "tfidf-local-v1"
        }
      ]
    },
    {
      "step": "explanation",
      "facts": [
        {
          "id": "HK-74914",
          "price": 300000,
          "budget": 1000000,
          "saving": 700000,
          "event": "свадьба",
          "lang": "русский",
          "hours": 3.0,
          "max_hours": 12.0,
          "detail": "Снимаю с душой и ради удовольствия",
          "details": [
            "Снимаю с душой и ради удовольствия",
            "Я свадебный видеограф из Астаны",
            "Работаю по всему Казахстану"
          ],
          "unique_detail": true,
          "price_unique": true,
          "more_than_cheapest": 0,
          "cheaper_than_others": true,
          "indistinguishable": false
        },
        {
          "id": "HK-10990",
          "price": 400000,
          "budget": 1000000,
          "saving": 600000,
          "event": "свадьба",
          "lang": "русский",
          "hours": 3.0,
          "max_hours": 12.0,
          "detail": "TODOROKI SHOTO WEDDING VIDEOGRAPHER -colorist of the year 2025 🏆 Считаю себя счастливым человеком, так как любимое занятие стало делом моей жизни",
          "details": [
            "TODOROKI SHOTO WEDDING VIDEOGRAPHER -colorist of the year 2025 🏆 Считаю себя счастливым человеком, так как любимое занятие стало делом моей жизни",
            "Больше всего в съёмке я ценю слаженную работу в команде, где все ориентированы на качественный результат, полностью отдаваясь процессу",
            "А качественным результатом считаю благодарные отзывы моих пар и собственное удовлетворение от проделанной работы"
          ],
          "unique_detail": true,
          "price_unique": true,
          "more_than_cheapest": 100000,
          "cheaper_than_others": false,
          "indistinguishable": false
        }
      ],
      "backend": "offline",
      "cache_key": "2c6c566d8c102cfd8a88b617fdf5ed4ecac379e0064782066c85e6eaede563f6",
      "provider_errors": [],
      "critic_errors": [],
      "pairwise_similarity": [
        0.3485
      ]
    }
  ],
  "timings_ms": {
    "filters": 0.089,
    "scoring": 1.283,
    "explanations": 1.3,
    "hints": 2.333,
    "total": 5.005
  }
}
```
</details>

## Запрос 6

```json
{"city": "Алматы", "category": "Декоратор", "event": "свадьба", "date": "2026-09-23", "budget": 2000000, "hours": 3, "lang": "русский"}
```

**MATCHED** · 2.90 мс

В городе Алматы, категория «Декоратор»: всего 3, проходят 1. Подобрали 1. Найдено 1 — меньше трёх: заняты на дату — 1; не проходят по бюджету (включая неизвестную цену) — 1. Исключено из-за занятости на 23.09.2026: 1.

### Уинри Рокбелл · Декоратор · Алматы · от 2 000 000 ₸

реальный · score 0.4

Формат «свадьба» указан в профиле; цена от 2 000 000 ₸ оставляет 0 ₸ от вашего бюджета 2 000 000 ₸; рабочий язык — русский; при запросе 3 ч работа не привязана к присутствию. В описании: «индивидуальные концепции под клиента авторские эскизы перед реализацией собственное производство конструкций работа под ключ без стресса для клиента опыт крупных проектов и масштабных площадок».

Подсказка: При остальных условиях без изменений: 24.09.2026 — подходят 2; 25.09.2026 — подходят 1; 26.09.2026 — подходят 1.

Подсказка: Ещё один кандидат прошёл бы при бюджете от 2 200 000 ₸: сейчас не хватает 200 000 ₸.

Подсказка: Один из исключённых кандидатов занят 23.09.2026, но прошёл бы все условия 24.09.2026.

<details><summary>Trace и timings</summary>

```json
{
  "trace": [
    {
      "step": "load_normalize",
      "profiles": 66
    },
    {
      "step": "scope",
      "count": 3
    },
    {
      "step": "hard_filters",
      "passed": 1,
      "excluded": [
        {
          "id": "HK-90003",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-23"
            }
          ]
        },
        {
          "id": "HK-90004",
          "primary_reason": "budget",
          "all_reasons": [
            {
              "reason": "budget",
              "missing_price": false,
              "over_budget_kzt": 200000
            }
          ]
        }
      ],
      "counts": {
        "busy": 1,
        "format": 0,
        "budget": 1,
        "language": 0,
        "hours": 0
      }
    },
    {
      "step": "scoring",
      "candidates": [
        {
          "id": "HK-11484",
          "score": 0.4,
          "components": {
            "budget_fit": 0.6666666666666667,
            "semantic_fit": 0.0,
            "language_fit": 1.0,
            "hours_fit": 1.0
          },
          "data_quality_penalty": 0.0,
          "semantic_backend": "tfidf-local-v1"
        }
      ]
    },
    {
      "step": "explanation",
      "facts": [
        {
          "id": "HK-11484",
          "price": 2000000,
          "budget": 2000000,
          "saving": 0,
          "event": "свадьба",
          "lang": "русский",
          "hours": 3.0,
          "max_hours": null,
          "detail": "индивидуальные концепции под клиента авторские эскизы перед реализацией собственное производство конструкций работа под ключ без стресса для клиента опыт крупных проектов и масштабных площадок",
          "details": [
            "индивидуальные концепции под клиента авторские эскизы перед реализацией собственное производство конструкций работа под ключ без стресса для клиента опыт крупных проектов и масштабных площадок",
            "Работаем под ключ: от идеи и эскиза до монтажа и финальной реализации",
            "Более 5 лет создаём концепции свадеб, юбилеев и корпоративных событий премиум-уровня"
          ],
          "unique_detail": true,
          "price_unique": true,
          "more_than_cheapest": 0,
          "cheaper_than_others": false,
          "indistinguishable": false
        }
      ],
      "backend": "offline",
      "cache_key": "416f8a2ffa5650759286605dda69a5f55013e4da239b499d0049a01ea1c18ad6",
      "provider_errors": [],
      "critic_errors": [],
      "pairwise_similarity": []
    }
  ],
  "timings_ms": {
    "filters": 0.094,
    "scoring": 0.638,
    "explanations": 0.678,
    "hints": 1.488,
    "total": 2.898
  }
}
```
</details>

## Запрос 7

```json
{"city": "Алматы", "category": "Фотограф", "event": "свадьба", "date": "2026-09-23", "budget": 1000000, "hours": 3, "lang": "русский"}
```

**MATCHED** · 6.08 мс

В городе Алматы, категория «Фотограф»: всего 8, проходят 3. Подобрали 3. Исключено из-за занятости на 23.09.2026: 3.

### Нобара Кугисаки · Фотограф · Алматы · от 600 000 ₸

реальный · score 0.4738

Формат «свадьба» указан в профиле; цена от 600 000 ₸ оставляет 400 000 ₸ от вашего бюджета 1 000 000 ₸; рабочий язык — русский; доступно до 12 ч при запросе 3 ч. В описании: «Является свадебным и репортажным фотографом, умеет ловить живые эмоции и передавать атмосферу события через искренние, естественные кадры»; дороже самого недорогого в этой выдаче на 410 000 ₸.

### Мэгуми Фушигуро · Фотограф · Алматы · от 300 000 ₸

реальный · score 0.336

В описании: «Чистоте кадра, лёгкость и визуальное дыхание — мне важно, чтобы фотография возвращала вас снова и снова в важный день вашей жизни»; дороже самого недорогого в этой выдаче на 110 000 ₸. Формат «свадьба» указан в профиле; цена от 300 000 ₸ оставляет 700 000 ₸ от вашего бюджета 1 000 000 ₸; рабочий язык — русский; доступно до 10 ч при запросе 3 ч.

### Рок Ли · Фотограф · Алматы · от 190 000 ₸

реальный · score 0.276

Формат «свадьба» указан в профиле; цена от 190 000 ₸ оставляет 810 000 ₸ от вашего бюджета 1 000 000 ₸; рабочий язык — русский; доступно до 12 ч при запросе 3 ч. В описании: «Он создает яркие, живые и красиво обработанные фотографии, а работа с ним оставляет только положительные эмоции, отмечают довольные молодожены, получившие снимки в обещанные сроки»; самая низкая начальная цена среди показанных.

<details><summary>Trace и timings</summary>

```json
{
  "trace": [
    {
      "step": "load_normalize",
      "profiles": 66
    },
    {
      "step": "scope",
      "count": 8
    },
    {
      "step": "hard_filters",
      "passed": 3,
      "excluded": [
        {
          "id": "HK-20640",
          "primary_reason": "format",
          "all_reasons": [
            {
              "reason": "format",
              "event": "свадьба"
            }
          ]
        },
        {
          "id": "HK-30583",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-23"
            }
          ]
        },
        {
          "id": "HK-35913",
          "primary_reason": "format",
          "all_reasons": [
            {
              "reason": "format",
              "event": "свадьба"
            }
          ]
        },
        {
          "id": "HK-53108",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-23"
            }
          ]
        },
        {
          "id": "HK-76268",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-23"
            }
          ]
        }
      ],
      "counts": {
        "busy": 3,
        "format": 2,
        "budget": 0,
        "language": 0,
        "hours": 0
      }
    },
    {
      "step": "scoring",
      "candidates": [
        {
          "id": "HK-16628",
          "score": 0.4738,
          "components": {
            "budget_fit": 0.7999999999999999,
            "semantic_fit": 0.06754056680814166,
            "language_fit": 1.0,
            "hours_fit": 1.0
          },
          "data_quality_penalty": 0.0,
          "semantic_backend": "tfidf-local-v1"
        },
        {
          "id": "HK-91112",
          "score": 0.336,
          "components": {
            "budget_fit": 0.4,
            "semantic_fit": 0.03194014984601427,
            "language_fit": 1.0,
            "hours_fit": 1.0
          },
          "data_quality_penalty": 0.0,
          "semantic_backend": "tfidf-local-v1"
        },
        {
          "id": "HK-68220",
          "score": 0.276,
          "components": {
            "budget_fit": 0.2533333333333333,
            "semantic_fit": 0.0,
            "language_fit": 1.0,
            "hours_fit": 1.0
          },
          "data_quality_penalty": 0.0,
          "semantic_backend": "tfidf-local-v1"
        }
      ]
    },
    {
      "step": "explanation",
      "facts": [
        {
          "id": "HK-16628",
          "price": 600000,
          "budget": 1000000,
          "saving": 400000,
          "event": "свадьба",
          "lang": "русский",
          "hours": 3.0,
          "max_hours": 12.0,
          "detail": "Является свадебным и репортажным фотографом, умеет ловить живые эмоции и передавать атмосферу события через искренние, естественные кадры",
          "details": [
            "Является свадебным и репортажным фотографом, умеет ловить живые эмоции и передавать атмосферу события через искренние, естественные кадры",
            "Работает по всему Казахстану и за рубежом, создавая эстетичные и живые истории"
          ],
          "unique_detail": true,
          "price_unique": true,
          "more_than_cheapest": 410000,
          "cheaper_than_others": false,
          "indistinguishable": false
        },
        {
          "id": "HK-91112",
          "price": 300000,
          "budget": 1000000,
          "saving": 700000,
          "event": "свадьба",
          "lang": "русский",
          "hours": 3.0,
          "max_hours": 10.0,
          "detail": "Чистоте кадра, лёгкость и визуальное дыхание — мне важно, чтобы фотография возвращала вас снова и снова в важный день вашей жизни",
          "details": [
            "Чистоте кадра, лёгкость и визуальное дыхание — мне важно, чтобы фотография возвращала вас снова и снова в важный день вашей жизни",
            "Я люблю честные эмоции, лёгкость и кадры с воздухом — когда фотография не кричит, а чувствуется",
            "Моя сила не в «шаблонной красоте», а в умении видеть человека: взгляд, паузу, напряжение, нежность"
          ],
          "unique_detail": true,
          "price_unique": true,
          "more_than_cheapest": 110000,
          "cheaper_than_others": false,
          "indistinguishable": false
        },
        {
          "id": "HK-68220",
          "price": 190000,
          "budget": 1000000,
          "saving": 810000,
          "event": "свадьба",
          "lang": "русский",
          "hours": 3.0,
          "max_hours": 12.0,
          "detail": "Он создает яркие, живые и красиво обработанные фотографии, а работа с ним оставляет только положительные эмоции, отмечают довольные молодожены, получившие снимки в обещанные сроки",
          "details": [
            "Он создает яркие, живые и красиво обработанные фотографии, а работа с ним оставляет только положительные эмоции, отмечают довольные молодожены, получившие снимки в обещанные сроки",
            "Его стиль — это сочетание репортажной съемки(захват моментов) и постановочных кадров, а главная цель — передать атмосферу и эмоции дня свадьбы",
            "Ключевые моменты: Профессионализм и качество: Высокие оценки за обработку и своеобразный стиль фотографий"
          ],
          "unique_detail": true,
          "price_unique": true,
          "more_than_cheapest": 0,
          "cheaper_than_others": true,
          "indistinguishable": false
        }
      ],
      "backend": "offline",
      "cache_key": "4d8bddf4b8758bdf3c49cc08373453f12efd0c5f774145b72d26246fac9ff678",
      "provider_errors": [],
      "critic_errors": [],
      "pairwise_similarity": [
        0.4265,
        0.3514,
        0.2949
      ]
    }
  ],
  "timings_ms": {
    "filters": 0.129,
    "scoring": 1.916,
    "explanations": 4.04,
    "hints": 0.0,
    "total": 6.085
  }
}
```
</details>

## Запрос 8

```json
{"city": "Алматы", "category": "Национальный ансамбль", "event": "той", "date": "2026-09-23", "budget": 1000000, "hours": 3, "lang": "казахский"}
```

**NONE_PASS_CONDITIONS** · 2.94 мс

В городе Алматы, категория «Национальный ансамбль»: всего 4, проходят 0. Ни один кандидат не проходит: заняты на дату — 2; не хватает длительности — 2. Исключено из-за занятости на 23.09.2026: 2.

<details><summary>Trace и timings</summary>

```json
{
  "trace": [
    {
      "step": "load_normalize",
      "profiles": 66
    },
    {
      "step": "scope",
      "count": 4
    },
    {
      "step": "hard_filters",
      "passed": 0,
      "excluded": [
        {
          "id": "HK-19103",
          "primary_reason": "hours",
          "all_reasons": [
            {
              "reason": "hours",
              "missing_hours": 1.0
            }
          ]
        },
        {
          "id": "HK-36965",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-23"
            },
            {
              "reason": "hours",
              "missing_hours": 1.0
            }
          ]
        },
        {
          "id": "HK-39301",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-23"
            },
            {
              "reason": "hours",
              "missing_hours": 1.0
            }
          ]
        },
        {
          "id": "HK-92824",
          "primary_reason": "hours",
          "all_reasons": [
            {
              "reason": "hours",
              "missing_hours": 1.0
            }
          ]
        }
      ],
      "counts": {
        "busy": 2,
        "format": 0,
        "budget": 0,
        "language": 0,
        "hours": 2
      }
    },
    {
      "step": "scoring",
      "candidates": []
    },
    {
      "step": "explanation",
      "facts": [],
      "backend": "none"
    }
  ],
  "timings_ms": {
    "filters": 0.108,
    "scoring": 0.001,
    "explanations": 0.015,
    "hints": 2.812,
    "total": 2.937
  }
}
```
</details>

## Запрос 9

```json
{"city": "Алматы", "category": "Фотограф", "event": "день рождения", "date": "2026-09-23", "budget": 1000000, "hours": 3, "lang": "русский"}
```

**MATCHED** · 6.14 мс

В городе Алматы, категория «Фотограф»: всего 8, проходят 1. Подобрали 1. Найдено 1 — меньше трёх: заняты на дату — 3; не берут формат — 4. Исключено из-за занятости на 23.09.2026: 3.

### Шикамару Нара · Фотограф · Алматы · от 150 000 ₸

реальный · score 0.2946

Формат «день рождения» указан в профиле; цена от 150 000 ₸ оставляет 850 000 ₸ от вашего бюджета 1 000 000 ₸; рабочий язык — русский; доступно до 4 ч при запросе 3 ч. В описании: «Его работы — это внимание к деталям, живые эмоции и аккуратная, эстетичная подача, которая сохраняет атмосферу события и его настроение».

Подсказка: При остальных условиях без изменений: 24.09.2026 — подходят 1; 26.09.2026 — подходят 1; 27.09.2026 — подходят 1.

<details><summary>Trace и timings</summary>

```json
{
  "trace": [
    {
      "step": "load_normalize",
      "profiles": 66
    },
    {
      "step": "scope",
      "count": 8
    },
    {
      "step": "hard_filters",
      "passed": 1,
      "excluded": [
        {
          "id": "HK-16628",
          "primary_reason": "format",
          "all_reasons": [
            {
              "reason": "format",
              "event": "день рождения"
            }
          ]
        },
        {
          "id": "HK-30583",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-23"
            },
            {
              "reason": "format",
              "event": "день рождения"
            }
          ]
        },
        {
          "id": "HK-35913",
          "primary_reason": "format",
          "all_reasons": [
            {
              "reason": "format",
              "event": "день рождения"
            }
          ]
        },
        {
          "id": "HK-53108",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-23"
            }
          ]
        },
        {
          "id": "HK-68220",
          "primary_reason": "format",
          "all_reasons": [
            {
              "reason": "format",
              "event": "день рождения"
            }
          ]
        },
        {
          "id": "HK-76268",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-23"
            },
            {
              "reason": "format",
              "event": "день рождения"
            }
          ]
        },
        {
          "id": "HK-91112",
          "primary_reason": "format",
          "all_reasons": [
            {
              "reason": "format",
              "event": "день рождения"
            }
          ]
        }
      ],
      "counts": {
        "busy": 3,
        "format": 4,
        "budget": 0,
        "language": 0,
        "hours": 0
      }
    },
    {
      "step": "scoring",
      "candidates": [
        {
          "id": "HK-20640",
          "score": 0.2946,
          "components": {
            "budget_fit": 0.20000000000000007,
            "semantic_fit": 0.0692566759446345,
            "language_fit": 1.0,
            "hours_fit": 1.0
          },
          "data_quality_penalty": 0.0,
          "semantic_backend": "tfidf-local-v1"
        }
      ]
    },
    {
      "step": "explanation",
      "facts": [
        {
          "id": "HK-20640",
          "price": 150000,
          "budget": 1000000,
          "saving": 850000,
          "event": "день рождения",
          "lang": "русский",
          "hours": 3.0,
          "max_hours": 4.0,
          "detail": "Его работы — это внимание к деталям, живые эмоции и аккуратная, эстетичная подача, которая сохраняет атмосферу события и его настроение",
          "details": [
            "Его работы — это внимание к деталям, живые эмоции и аккуратная, эстетичная подача, которая сохраняет атмосферу события и его настроение"
          ],
          "unique_detail": true,
          "price_unique": true,
          "more_than_cheapest": 0,
          "cheaper_than_others": false,
          "indistinguishable": false
        }
      ],
      "backend": "offline",
      "cache_key": "35cb1099c85921994a6208dd6666f76e8dfa69bd1c389afd2b93eb33c11d514e",
      "provider_errors": [],
      "critic_errors": [],
      "pairwise_similarity": []
    }
  ],
  "timings_ms": {
    "filters": 0.117,
    "scoring": 0.652,
    "explanations": 0.517,
    "hints": 4.852,
    "total": 6.138
  }
}
```
</details>

## Запрос 10

```json
{"city": "Алматы", "category": "Лайв-бэнд", "event": "свадьба", "date": "2026-09-23", "budget": 1150000, "hours": 3, "lang": "казахский"}
```

**MATCHED** · 5.44 мс

В городе Алматы, категория «Лайв-бэнд»: всего 5, проходят 2. Подобрали 2. Найдено 2 — меньше трёх: заняты на дату — 1; не берут формат — 1; не проходят по бюджету (включая неизвестную цену) — 1. Исключено из-за занятости на 23.09.2026: 1.

### Дзэнъицу Агацума · Лайв-бэнд · Алматы · от 1 150 000 ₸

реальный · score 0.4

Формат «свадьба» указан в профиле; цена от 1 150 000 ₸ оставляет 0 ₸ от вашего бюджета 1 150 000 ₸; рабочий язык — казахский; доступно до 6 ч при запросе 3 ч. В описании: «Расширенный состав Thunder Breath Band: 🎤 два вокалиста 🎤 вокалистка 🥁 барабанщик 🎸 бас-гитарист 🎸 соло-гитарист 🎺 труба 🎷 саксофон 🎵 тромбон Репертуар включает…».

### Рей Аянами · Лайв-бэнд · Алматы · от 1 150 000 ₸

реальный · score 0.4

В описании: «Большой музыкальный состав: 4 вокалиста, струнный квартет, духовой брасс, перкуссионист, клавишник, барабанщик, гитарист и бас-гитарист». Формат «свадьба» указан в профиле; цена от 1 150 000 ₸ оставляет 0 ₸ от вашего бюджета 1 150 000 ₸; рабочий язык — казахский; доступно до 6 ч при запросе 3 ч.

Подсказка: При остальных условиях без изменений: 24.09.2026 — подходят 1; 25.09.2026 — подходят 2; 27.09.2026 — подходят 2.

<details><summary>Trace и timings</summary>

```json
{
  "trace": [
    {
      "step": "load_normalize",
      "profiles": 66
    },
    {
      "step": "scope",
      "count": 5
    },
    {
      "step": "hard_filters",
      "passed": 2,
      "excluded": [
        {
          "id": "HK-25279",
          "primary_reason": "busy",
          "all_reasons": [
            {
              "reason": "busy",
              "date": "2026-09-23"
            },
            {
              "reason": "format",
              "event": "свадьба"
            },
            {
              "reason": "language",
              "language": "казахский"
            }
          ]
        },
        {
          "id": "HK-31819",
          "primary_reason": "format",
          "all_reasons": [
            {
              "reason": "format",
              "event": "свадьба"
            },
            {
              "reason": "language",
              "language": "казахский"
            }
          ]
        },
        {
          "id": "HK-57480",
          "primary_reason": "budget",
          "all_reasons": [
            {
              "reason": "budget",
              "missing_price": false,
              "over_budget_kzt": 350000
            },
            {
              "reason": "language",
              "language": "казахский"
            }
          ]
        }
      ],
      "counts": {
        "busy": 1,
        "format": 1,
        "budget": 1,
        "language": 0,
        "hours": 0
      }
    },
    {
      "step": "scoring",
      "candidates": [
        {
          "id": "HK-23752",
          "score": 0.4,
          "components": {
            "budget_fit": 0.6666666666666667,
            "semantic_fit": 0.0,
            "language_fit": 1.0,
            "hours_fit": 1.0
          },
          "data_quality_penalty": 0.0,
          "semantic_backend": "tfidf-local-v1"
        },
        {
          "id": "HK-83709",
          "score": 0.4,
          "components": {
            "budget_fit": 0.6666666666666667,
            "semantic_fit": 0.0,
            "language_fit": 1.0,
            "hours_fit": 1.0
          },
          "data_quality_penalty": 0.0,
          "semantic_backend": "tfidf-local-v1"
        }
      ]
    },
    {
      "step": "explanation",
      "facts": [
        {
          "id": "HK-23752",
          "price": 1150000,
          "budget": 1150000,
          "saving": 0,
          "event": "свадьба",
          "lang": "казахский",
          "hours": 3.0,
          "max_hours": 6.0,
          "detail": "Расширенный состав Thunder Breath Band: 🎤 два вокалиста 🎤 вокалистка 🥁 барабанщик 🎸 бас-гитарист 🎸 соло-гитарист 🎺 труба 🎷 саксофон 🎵 тромбон Репертуар включает…",
          "details": [
            "Расширенный состав Thunder Breath Band: 🎤 два вокалиста 🎤 вокалистка 🥁 барабанщик 🎸 бас-гитарист 🎸 соло-гитарист 🎺 труба 🎷 саксофон 🎵 тромбон Репертуар включает…",
            "В репертуаре группы большой выбор казахских песен, ретро-шлягеров, хитов 80-х, 90-х, 2000-х, а так же, современные хиты",
            "Начиная от модных ивэнтов до масштабных свадеб, «Thunder Breath Band» идеально впишется в любой формат мероприятия"
          ],
          "unique_detail": true,
          "price_unique": false,
          "more_than_cheapest": 0,
          "cheaper_than_others": false,
          "indistinguishable": false
        },
        {
          "id": "HK-83709",
          "price": 1150000,
          "budget": 1150000,
          "saving": 0,
          "event": "свадьба",
          "lang": "казахский",
          "hours": 3.0,
          "max_hours": 6.0,
          "detail": "Большой музыкальный состав: 4 вокалиста, струнный квартет, духовой брасс, перкуссионист, клавишник, барабанщик, гитарист и бас-гитарист",
          "details": [
            "В репертуаре группы большой выбор казахских песен, ретро-шлягеров, хитов 80-х, 90-х, 2000-х, а так же, современные хиты",
            "Большой музыкальный состав: 4 вокалиста, струнный квартет, духовой брасс, перкуссионист, клавишник, барабанщик, гитарист и бас-гитарист",
            "Начиная от модных ивэнтов до масштабных свадеб, «Eva Sound» идеально впишется в любой формат мероприятия"
          ],
          "unique_detail": true,
          "price_unique": false,
          "more_than_cheapest": 0,
          "cheaper_than_others": false,
          "indistinguishable": false
        }
      ],
      "backend": "offline",
      "cache_key": "600c54473d9c7345e932c25e13f155a36bb97965b169b6be8200f294f0352212",
      "provider_errors": [],
      "critic_errors": [],
      "pairwise_similarity": [
        0.5769
      ]
    }
  ],
  "timings_ms": {
    "filters": 0.095,
    "scoring": 1.295,
    "explanations": 1.803,
    "hints": 2.244,
    "total": 5.438
  }
}
```
</details>

