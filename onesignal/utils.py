def merge_dicts(first_dict, *dicts):
    """
    Merge several dicts

    This function is needed for Python 2 support. It will be REMOVED on January 1, 2020.
    Python 3 alternative: x = {**a, **b}
    """
    new_dict = first_dict.copy()
    for dict_ in dicts:
        new_dict.update(dict_)
    return new_dict
