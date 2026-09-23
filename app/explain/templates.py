from ..normalize import money


def options(f):
    price = money(f["price"])
    saving = money(f["saving"])
    budget = money(f["budget"])
    opening = f'Формат «{f["event"]}» указан в профиле; цена от {price} оставляет {saving} от вашего бюджета {budget}'
    if f["lang"]:
        opening += f'; рабочий язык — {f["lang"]}'
    if f["hours"] is not None:
        opening += (f'; при запросе {f["hours"]:g} ч работа не привязана к присутствию' if f["max_hours"] is None
                    else f'; доступно до {f["max_hours"]:g} ч при запросе {f["hours"]:g} ч')
    second = f'В описании: «{f["detail"]}»' if f["detail"] else ""
    if f["more_than_cheapest"]:
        second += f'; дороже самого недорогого в этой выдаче на {money(f["more_than_cheapest"])}'
    elif f["cheaper_than_others"]:
        second += '; самая низкая начальная цена среди показанных'
    if f["indistinguishable"]:
        second += '; по доступным фактам отличий от другого показанного профиля нет'
    second = second.lstrip('; ')
    a = opening + "." + (" " + second + "." if second else "")
    b = (second + ". " if second else "") + opening + "."
    return [a, b]
