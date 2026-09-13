import re
from datetime import date


def validate_date(value, today=None):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("日期格式错误，请使用 YYYY-MM-DD 格式。")

    try:
        selected_date = date.fromisoformat(value)
    except ValueError as error:
        raise ValueError("日期不存在，请重新输入。") from error

    if selected_date < (today or date.today()):
        raise ValueError("日期已过期，请重新输入。")

    return value


def validate_station(value, stations, field_name):
    try:
        return stations[value]
    except KeyError as error:
        raise ValueError(f"{field_name}不存在，请重新输入。") from error


def prompt_date(input_func=input, output_func=print, today=None):
    while True:
        value = input_func("请输入日期（YYYY-MM-DD）:")
        try:
            return validate_date(value, today=today)
        except ValueError as error:
            output_func(str(error))


def prompt_station(stations, field_name, input_func=input, output_func=print):
    while True:
        value = input_func(f"请输入{field_name}:")
        try:
            return validate_station(value, stations, field_name)
        except ValueError as error:
            output_func(str(error))
