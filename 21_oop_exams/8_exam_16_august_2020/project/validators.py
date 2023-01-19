def name_validator(name, error_message):
    if not name or name.isspace():
        raise ValueError(error_message)
    return name


def greater_than_zero_validator(price, error_message):
    if price <= 0:
        raise ValueError(error_message)
    return price


def zero_or_positive_number_validator(num, error_message):
    if num < 0:
        raise ValueError(error_message)
    return num


def number_in_range_validator(num, min_number, max_number, error_message):
    if num < min_number or num > max_number:
        raise ValueError(error_message)
    return num


def if_item_name_exists(item, repo):
    for obj in repo:
        if obj.name == item:
            return True
    return False


def find_by_name(name, repo):
    for item in repo:
        if item.name == name:
            return item
    return None
