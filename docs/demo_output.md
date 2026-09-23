# Живое демо

Источник: 66 профилей организаторов; собственная синтетика не добавлена.

## Плотная категория

```json
{"city": "Алматы", "date": "2026-09-26", "event": "свадьба", "category": "Фотограф", "budget": 2000000}
```

**MATCHED** · 4.11 мс

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
    "filters": 0.161,
    "scoring": 2.574,
    "explanations": 1.371,
    "hints": 0.0,
    "total": 4.106
  }
}
```
</details>

## Редкая категория

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
    "filters": 0.079,
    "scoring": 0.387,
    "explanations": 0.405,
    "hints": 1.022,
    "total": 1.893
  }
}
```
</details>

## Никто не проходит

```json
{"city": "Алматы", "date": "2026-09-26", "event": "свадьба", "category": "Фотограф", "budget": 1}
```

**NONE_PASS_CONDITIONS** · 5.80 мс

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
    "filters": 0.124,
    "scoring": 0.001,
    "explanations": 0.015,
    "hints": 5.656,
    "total": 5.796
  }
}
```
</details>

## Нет категории в городе

```json
{"city": "Астана", "date": "2026-10-01", "event": "свадьба", "category": "Декоратор", "budget": 2000000}
```

**NO_CATEGORY_IN_CITY** · 0.11 мс

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
    "filters": 0.078,
    "scoring": 0.001,
    "explanations": 0.017,
    "hints": 0.016,
    "total": 0.113
  }
}
```
</details>

## Две даты

В городе Алматы, категория «Фотограф»: всего 8, проходят 4. Подобрали 3. Исключено из-за занятости на 26.09.2026: 4.

В городе Алматы, категория «Фотограф»: всего 8, проходят 3. Подобрали 3. Исключено из-за занятости на 23.09.2026: 3.

```json
[
  {
    "id": "HK-76268",
    "anon_name": "Сацуки Кусакабэ",
    "change": "выпал",
    "reason": "занят 23.09.2026"
  },
  {
    "id": "HK-53108",
    "anon_name": "Альфонс Элрик",
    "change": "выпал",
    "reason": "занят 23.09.2026"
  },
  {
    "id": "HK-30583",
    "anon_name": "Леорио Паради",
    "change": "выпал",
    "reason": "занят 23.09.2026"
  },
  {
    "id": "HK-16628",
    "anon_name": "Нобара Кугисаки",
    "change": "появился",
    "reason": "занят 26.09.2026"
  },
  {
    "id": "HK-91112",
    "anon_name": "Мэгуми Фушигуро",
    "change": "появился",
    "reason": "занят 26.09.2026"
  },
  {
    "id": "HK-68220",
    "anon_name": "Рок Ли",
    "change": "появился",
    "reason": "изменился состав top-3 из-за доступности других кандидатов"
  }
]
```

## Детерминизм

Три вызова и новый процесс без API-ключа: четыре одинаковых SHA-256 списка id.

```
6f1db3a9d86abb328259972a22e52c6d20dc806a16011aeb401ee3f1fd544f75
6f1db3a9d86abb328259972a22e52c6d20dc806a16011aeb401ee3f1fd544f75
6f1db3a9d86abb328259972a22e52c6d20dc806a16011aeb401ee3f1fd544f75
6f1db3a9d86abb328259972a22e52c6d20dc806a16011aeb401ee3f1fd544f75
```
