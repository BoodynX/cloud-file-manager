def tc(obj, cls):
    if not isinstance(obj, cls):
        raise TypeError(f'Expecting {cls} instead received {type(obj)}')