def name_validator(name, error_message):
    if not name or name.isspace():
        raise ValueError(error_message)
    return name


def greater_than_value_validator(num, value, error_message):
    if num < value:
        raise ValueError(error_message)
    return num


def find_by_name(name, repo):
    for item in repo:
        if item.name == name:
            return item
    return None


def str_len_less_than_value(string, value_min_len, error_message):
    if len(string) < value_min_len:
        raise ValueError(error_message)
    return string
