def merge(*dicts):
    result = {}
    for item in dicts:
        for key, value in item.items():
            if key in result: result[key].append(value)
            else: result[key] = [value]
    return result