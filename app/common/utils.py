import calendar


def check_required_keys(keys: tuple, element: dict):
    return all(element.get(key) for key in keys)

def number_to_month(number: int):
    return calendar.month_name[number]