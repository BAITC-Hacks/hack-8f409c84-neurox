# Проверка поставки

Дата: 23.09.2026. Windows, Python 3.12. Проверка без OpenAI-ключа.

## pytest

```text
31 passed, 1 warning in 11.01s
```

Предупреждение: устаревший alias anyio.abc.BlockingPortal в установленной версии Starlette; на работу тестов не влияет.

Проверены: контракт R1–R6, 100 дней календаря на сетке фильтров, end-to-end сетка на трёх датах, площадки и исходная синтетика, оба режима include_team, сумма причин, неизвестная цена, бюджет включительно, опциональные поля, валидация API, новый процесс с другим PYTHONHASHSEED, отказ/повтор LLM-заглушки и постоянный кэш.

В тестах запрещены внешние socket-соединения. Loopback разрешён, поскольку Windows asyncio использует его для внутренней socketpair; TestClient не вызывает внешний API.

## Браузер

Headless Chrome: успешный подбор 3 карточек, оба пустых исхода, сравнение дат, отсутствие JavaScript-ошибок. На ширине 390 px нет горизонтального переполнения. Снимок desktop сохранён в screenshot.png и просмотрен.

## Демо

```text
Плотная категория: MATCHED; cards=3
Редкая категория: MATCHED; cards=1
Никто не проходит: NONE_PASS_CONDITIONS; cards=0
Нет категории в городе: NO_CATEGORY_IN_CITY; cards=0
Comparison date: 2026-09-23; diff=6
Determinism SHA256:
6f1db3a9d86abb328259972a22e52c6d20dc806a16011aeb401ee3f1fd544f75
4/4 identical
```

Подробные объяснения и времена: demo_output.md и EXPLANATION_SAMPLES.md. Метрики на 918 запросах: EVAL.md. Реальные вызовы OpenAI, Docker и удалённый GitHub Actions не проверялись.
